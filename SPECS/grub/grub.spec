# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# We have to set _libdir to /usr/lib for grub - 251
%global _libdir %{_exec_prefix}/lib

%global grub_platforms riscv64-efi
%global kernel_module linux

%ifarch x86_64
%global grub_platforms x86_64-efi
%endif

Name:           grub
Version:        2.14
Release:        %autorelease
Summary:        Bootloader with support for Linux, Multiboot and more
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/grub/
VCS:            git:https://https.git.savannah.gnu.org/git/grub.git
#!RemoteAsset:  sha256:bc8d3c73535b8838d8c8e2654d73edc4e6ae8c8acdb45d5df5dc9a1547446d43
Source0:        https://ftpmirror.gnu.org/gnu/grub/grub-%{version}.tar.xz
Source1:        grub.default

# https://gitlab.freedesktop.org/gnu-grub/grub/-/merge_requests/10
Patch0:         skip-efi_uga.patch

# https://gitlab.freedesktop.org/gnu-grub/grub/-/merge_requests/14
Patch1:         blsuki-append-version.patch

# https://lists.gnu.org/archive/html/grub-devel/2026-02/msg00078.html
Patch2:         grub-c23-string-func-handling-updates.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  libtool
BuildRequires:  device-mapper-devel
BuildRequires:  fonts-dejavu
BuildRequires:  flex
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  python3
BuildRequires:  xz-devel
BuildRequires:  fonts-unifont
BuildRequires:  squashfs-tools
BuildRequires:  bash-completion

Recommends:     efibootmgr

%description
The GRand Unified Bootloader (GRUB) is a highly configurable and
customizable bootloader with modular architecture.  It supports a rich
variety of kernel formats, file systems, computer architectures and
hardware devices.

%package       unsigned
Summary:       GRand Unified Bootloader unsigned monolithic efi image
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description unsigned
The GRand Unified Bootloader (GRUB) is a highly configurable and
customizable bootloader with modular architecture.  It supports a rich
variety of kernel formats, file systems, computer architectures and
hardware devices.

This package contains an unsigned monolithic EFI image.

%prep
%autosetup -n %{name}-%{version} -p1

%conf
for plat in %{grub_platforms}; do
    echo "==> configure for $plat"
    src="$PWD"
    bdir="$PWD/../%{name}-%{version}-$plat"
    rm -rf -- "$bdir"

    # Copy source files to build directory
    ( set +x; cp -a "$src" "$bdir" >/dev/null 2>&1; set -x )
    pushd "$bdir"

    case "$plat" in
        x86_64-efi) extra="--with-platform=efi --target=x86_64"                  ;;
        riscv64-efi) extra="--with-platform=efi --target=riscv64"                ;;
    esac

    # Do Out of tree build
    CFLAGS="$CFLAGS -Wno-error=unterminated-string-initialization -Wno-unterminated-string-initialization" \
    %configure \
        --with-grubdir=grub \
        --with-rpm-version=%{version}-%{release} \
        --enable-boot-time \
        --enable-cache-stats \
        $extra
    popd
done

%build
for plat in %{grub_platforms}; do
    echo "==> build for $plat"
    pushd "$PWD/../%{name}-%{version}-$plat"

    if [ "$plat" = x86_64-efi ] || [ "$plat" = riscv64-efi ]; then
        make -j1 po/
    else
        sed -i -e 's#po docs##' Makefile
    fi
    %make_build

    echo "sbat,1,SBAT Version,sbat,1,https://github.com/rhboot/shim/blob/main/SBAT.md" > sbat.csv
    echo "grub,5,Free Software Foundation,grub,%{version},https://www.gnu.org/software/grub/" >> sbat.csv
    echo "grub.or,1,openRuyi,%{name},%{version},https://www.openruyi.org/" >> sbat.csv

    # Make fonts here
    mkdir -p ./fonts
    ./grub-mkfont -s 24 -o unicode.pf2 %{_datadir}/fonts/opentype/unifont/unifont.otf
    cp ./unicode.pf2 ./fonts
    tar --sort=name -cf - ./fonts | mksquashfs - memdisk.sqsh -tar -comp xz -quiet -no-progress

    FS_MODULES="btrfs ext2 xfs jfs reiserfs"
    CD_MODULES="all_video boot cat configfile echo true \
            font gfxmenu gfxterm gzio halt iso9660 \
            jpeg minicmd normal part_apple part_msdos part_gpt \
            password password_pbkdf2 png reboot search search_fs_uuid \
            search_fs_file search_label sleep test video fat loadenv loopback"
    PXE_MODULES="tftp http"
    CRYPTO_MODULES="luks luks2 gcry_rijndael gcry_sha1 gcry_sha256 gcry_sha512"

    # Add efi related modules
    %ifarch x86_64
    CD_MODULES="${CD_MODULES} efi_uga"
    %endif
    CD_MODULES="${CD_MODULES} chain efifwsetup efinet read tpm tss2 tpm2_key_protector memdisk tar squash4 xzio"
    PXE_MODULES="${PXE_MODULES} efinet"

    CD_MODULES="$CD_MODULES %{kernel_module}"

    # Final GRUB modules list
    GRUB_MODULES="$CD_MODULES $FS_MODULES $PXE_MODULES $CRYPTO_MODULES mdraid09 mdraid1x lvm serial"
    PRESENT_MODS=""
    for m in $GRUB_MODULES; do
        if [ -f grub-core/$m.mod ] || [ -f grub-core/$m.image ] || ls grub-core/$m.mo* >/dev/null 2>&1; then
            PRESENT_MODS="$PRESENT_MODS $m"
        fi
    done

    mkdir monolithic
    echo configfile \${cmdpath}/grub.cfg > grub.cfg
    case "$plat" in
        x86_64-efi) arch=x64 ;;
        riscv64-efi) arch=riscv64 ;;
    esac
    ./grub-mkstandalone \
        -O "$plat" \
        -o monolithic/grub${arch}.efi \
        --sbat sbat.csv \
        -d grub-core \
        --modules="${GRUB_MODULES}" \
        "/boot/grub/grub.cfg=./grub.cfg"
    popd
done

%install
for plat in %{grub_platforms}; do
    echo "==> install for $plat"
    pushd "$PWD/../%{name}-%{version}-$plat"
    %make_install bashcompletiondir=%{bash_completions_dir}
    rm -f %{buildroot}%{_libdir}/grub/$plat/*.module
    rm -f %{buildroot}%{_libdir}/grub/$plat/*.image
    rm -f %{buildroot}%{_libdir}/grub/$plat/{kernel.exec,gdb_grub,gmodule.pl}
    for efi_file in $(ls monolithic/*.efi); do
        install -D -m 644 $efi_file %{buildroot}%{_libdir}/grub/$plat/$efi_file
    done
    popd
done

install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/default/grub

# TODO: Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%dir %{_sysconfdir}/grub.d
%dir %{_libdir}/%{name}/
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/themes
%attr(0644,root,root) %ghost %config(noreplace) %{_sysconfdir}/default/grub
%config(noreplace) %{_sysconfdir}/grub.d/00_header
%config(noreplace) %{_sysconfdir}/grub.d/10_linux
%config(noreplace) %{_sysconfdir}/grub.d/20_linux_xen
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/grub.d/25_bli
%config(noreplace) %{_sysconfdir}/grub.d/30_os-prober
%config(noreplace) %{_sysconfdir}/grub.d/30_uefi-firmware
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
%{_datadir}/%{name}/*.pf2
%{_datadir}/%{name}/grub-mkconfig_lib
%{_datadir}/%{name}/ascii.h
%{_datadir}/%{name}/widthspec.h
%{_datadir}/%{name}/themes/starfield
%{bash_completions_dir}/grub*
%{_datadir}/info/%{name}.info*
%{_datadir}/info/grub-dev.info*

%files unsigned
%{_libdir}/%{name}/%{grub_platforms}/monolithic/*.efi

%changelog
%autochangelog
