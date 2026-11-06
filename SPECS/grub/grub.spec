# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# GCC 16 crashes during LTO of the freestanding zstd EFI module.
%global _lto_cflags %{nil}

# We have to set _libdir to /usr/lib for grub - 251
%global _libdir %{_exec_prefix}/lib

%global grub_cpu riscv64
%global kernel_module linux

%ifarch x86_64
%global grub_cpu x86_64
%endif

%global grub_platforms %{grub_cpu}-efi

Name:           grub
Version:        2.16
Release:        %autorelease
Summary:        Bootloader with support for Linux, Multiboot and more
License:        GPL-3.0-or-later AND GFDL-1.2-no-invariants-or-later AND CC-BY-SA-3.0
URL:            https://www.gnu.org/software/grub/
VCS:            git:https://gitlab.freedesktop.org/gnu-grub/grub.git
#!RemoteAsset:  sha256:f0db0104927df0b9a48bc41b735c702936190d17eb2d73d3018fa77474a0cabe
Source0:        https://gitlab.freedesktop.org/api/v4/projects/26558/packages/generic/source-assets/grub-%{version}/grub-%{version}.tar.xz
Source1:        grub.default

BuildSystem:    autotools

# Distribution FORTIFY flags expose warnings outside the upstream build.
# Keep userspace architecture flags out of the freestanding EFI code.
BuildOption(conf):  CFLAGS=""
BuildOption(conf):  HOST_CFLAGS="%{optflags}"
BuildOption(conf):  --disable-werror
BuildOption(conf):  --with-grubdir=grub
BuildOption(conf):  --with-platform=efi
BuildOption(conf):  --target=%{grub_cpu}
BuildOption(conf):  --enable-boot-time
BuildOption(conf):  --enable-cache-stats
BuildOption(conf):  --enable-stack-protector=strong
BuildOption(conf):  --with-sbat-file=$PWD/vendor-sbat.csv
BuildOption(install):  bashcompletiondir=%{bash_completions_dir}
# Filesystem tests need privileged mounts; firmware tests need QEMU and EFI firmware.
BuildOption(check):  TESTS='$(check_PROGRAMS_native) grub_script_blanklines grub_script_final_semicolon grub_script_dollar grub_script_no_commands grub_mkconfig_bootnext_test grub_mkconfig_bootnext_self_test'

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  texinfo
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  fonts-dejavu
BuildRequires:  flex
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  python3
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  fonts-unifont
BuildRequires:  squashfs-tools
BuildRequires:  bash-completion

Recommends:     efibootmgr

%description
The GRand Unified Bootloader (GRUB) is a highly configurable and
customizable bootloader with modular architecture.  It supports a rich
variety of kernel formats, file systems, computer architectures and
hardware devices.

%package        unsigned
Summary:        GRand Unified Bootloader unsigned monolithic efi image
License:        GPL-3.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    unsigned
The GRand Unified Bootloader (GRUB) is a highly configurable and
customizable bootloader with modular architecture.  It supports a rich
variety of kernel formats, file systems, computer architectures and
hardware devices.

This package contains an unsigned monolithic EFI image.

%conf -p
autoreconf -fiv
# Give shim a separate SBAT generation for revoking vulnerable openRuyi
# GRUB EFI images.
echo "grub.or,1,openRuyi,%{name},%{version},https://openruyi.cn/" > vendor-sbat.csv

%build -a
# Make fonts here
mkdir -p ./fonts
./grub-mkfont -s 24 -o unicode.pf2 %{_datadir}/fonts/opentype/unifont/unifont.otf
cp ./unicode.pf2 ./fonts
tar --sort=name -cf - ./fonts | mksquashfs - memdisk.sqsh -tar -comp xz -quiet -no-progress

FS_MODULES="btrfs ext2 xfs jfs reiserfs"
CD_MODULES="all_video blsuki boot cat configfile echo true \
        font gfxmenu gfxterm gzio halt iso9660 \
        jpeg minicmd normal part_apple part_msdos part_gpt \
        password password_pbkdf2 png reboot search search_fs_uuid \
        search_fs_file search_label sleep test video fat loadenv loopback"
PXE_MODULES="tftp http"
CRYPTO_MODULES="luks luks2 gcry_rijndael gcry_sha1 gcry_sha256 gcry_sha512"

CD_MODULES="${CD_MODULES} chain efifwsetup efinet read tpm tss2 tpm2_key_protector memdisk tar squash4 xzio"
PXE_MODULES="${PXE_MODULES} efinet"

CD_MODULES="$CD_MODULES %{kernel_module}"

# Final GRUB modules list
GRUB_MODULES="$CD_MODULES $FS_MODULES $PXE_MODULES $CRYPTO_MODULES mdraid09 mdraid1x lvm serial"
mkdir monolithic
echo configfile \${cmdpath}/grub.cfg > grub.cfg
case "%{grub_platforms}" in
    x86_64-efi) arch=x64 ;;
    riscv64-efi) arch=riscv64 ;;
esac
./grub-mkstandalone \
    -O "%{grub_platforms}" \
    -o monolithic/grub${arch}.efi \
    --sbat grub-core/sbat.csv \
    -d grub-core \
    --modules="${GRUB_MODULES}" \
    "/boot/grub/grub.cfg=./grub.cfg"

%install -a
rm -f %{buildroot}%{_libdir}/grub/%{grub_platforms}/*.module
rm -f %{buildroot}%{_libdir}/grub/%{grub_platforms}/*.image
rm -f %{buildroot}%{_libdir}/grub/%{grub_platforms}/{kernel.exec,gdb_grub,gmodule.pl}
install -D -m 0644 -t %{buildroot}%{_libdir}/grub/%{grub_platforms}/monolithic monolithic/*.efi

install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/default/grub

%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING docs/fdl.texi themes/starfield/COPYING.CC-BY-SA-3.0
%dir %{_sysconfdir}/grub.d
%dir %{_libdir}/grub/
%dir %{_datadir}/grub/
%dir %{_datadir}/grub/themes
%attr(0644,root,root) %ghost %config(noreplace) %{_sysconfdir}/default/grub
%config(noreplace) %{_sysconfdir}/grub.d/00_header
%config(noreplace) %{_sysconfdir}/grub.d/10_linux
%config(noreplace) %{_sysconfdir}/grub.d/20_linux_xen
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/grub.d/25_bli
%config(noreplace) %{_sysconfdir}/grub.d/30_os-prober
%config(noreplace) %{_sysconfdir}/grub.d/30_uefi-firmware
%config(noreplace) %{_sysconfdir}/grub.d/31_efi_bootnext
%config(noreplace) %{_sysconfdir}/grub.d/40_custom
%config(noreplace) %{_sysconfdir}/grub.d/41_custom
%{_sysconfdir}/grub.d/README
%{_bindir}/grub-file
%{_bindir}/grub-menulst2cfg
%{_bindir}/grub-mkimage
%{_bindir}/grub-mkrelpath
%{_bindir}/grub-script-check
%{_bindir}/grub-fstest
%{_bindir}/grub-kbdcomp
%{_bindir}/grub-mkfont
%{_bindir}/grub-mklayout
%{_bindir}/grub-mknetdir
%{_bindir}/grub-editenv
%{_bindir}/grub-mkpasswd-argon2
%{_bindir}/grub-mkpasswd-pbkdf2
%{_bindir}/grub-mount
%{_bindir}/grub-mkrescue
%{_bindir}/grub-mkstandalone
%{_bindir}/grub-render-label
%{_bindir}/grub-syslinux2cfg
%{_bindir}/grub-protect
%{_bindir}/grub-glue-efi
%{_sbindir}/grub-probe
%{_sbindir}/grub-set-default
%{_sbindir}/grub-macbless
%{_sbindir}/grub-install
%{_sbindir}/grub-mkconfig
%{_sbindir}/grub-reboot
%ifarch x86_64
%{_sbindir}/grub-bios-setup
%else
%exclude %{_sbindir}/grub-bios-setup
%endif
%exclude %{_sbindir}/grub-sparc64-setup
%exclude %{_sbindir}/grub-ofpathname
%{_libdir}/%{name}/%{grub_platforms}/*.mod
%{_libdir}/%{name}/%{grub_platforms}/modinfo.sh
%{_libdir}/%{name}/%{grub_platforms}/*.img
%{_libdir}/%{name}/%{grub_platforms}/*.lst
%{_libdir}/%{name}/%{grub_platforms}/gdb_helper.py
%{_libdir}/%{name}/%{grub_platforms}/config.h
%{_libdir}/%{name}/%{grub_platforms}/sbat.csv
%{_datadir}/%{name}/*.pf2
%{_datadir}/%{name}/grub-mkconfig_lib
%{_datadir}/%{name}/ascii.h
%{_datadir}/%{name}/widthspec.h
%{_datadir}/%{name}/themes/starfield
%{bash_completions_dir}/grub*
%{_datadir}/info/%{name}.info*
%{_datadir}/info/grub-dev.info*
%{_mandir}/man1/grub-*.1*
%{_mandir}/man8/grub-*.8*

%files unsigned
%{_libdir}/grub/%{grub_platforms}/monolithic/*.efi

%changelog
%autochangelog
