# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libguestfs
Version:        1.60.1
Release:        %autorelease
Summary:        Library and tools for accessing and modifying VM disk images
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://libguestfs.org/
VCS:            git:https://github.com/libguestfs/libguestfs.git
#!RemoteAsset:  sha256:6311c686700c293c92a9e804074040f4ae536fcbcef0a69973f418c77d3441e9
Source0:        https://download.libguestfs.org/1.60-stable/%{name}-%{version}.tar.gz
Source2000:     test-python-fuse.py
#!RemoteAsset:  sha256:30c36c4c57547bc4253d438b63f0ac89602e508870b73918646f3d840532a188
Source2001:     https://raw.githubusercontent.com/libfuse/libfuse/fuse-3.18.2/example/hello.c
BuildSystem:    autotools

# Downstream openRuyi appliance package names and RPM conditional.
Patch2000:      2000-add-openruyi-appliance.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-appliance
BuildOption(conf):  --enable-daemon
BuildOption(conf):  --with-supermin-extra-options=--use-installed
BuildOption(conf):  --disable-ocaml
BuildOption(conf):  --disable-perl
BuildOption(conf):  --enable-python
BuildOption(conf):  --disable-ruby
BuildOption(conf):  --disable-haskell
BuildOption(conf):  --disable-php
BuildOption(conf):  --disable-erlang
BuildOption(conf):  --disable-lua
BuildOption(conf):  --disable-golang
BuildOption(conf):  --without-java
BuildOption(conf):  --enable-fuse
BuildOption(conf):  --with-distro=OPENRUYI
BuildOption(conf):  --with-extra='openruyi'
BuildOption(conf):  --with-default-backend=direct

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  ocaml
BuildRequires:  ocaml-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-augeas
BuildRequires:  ocaml-hivex
BuildRequires:  acl-devel
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  supermin
BuildRequires:  pkgconfig(fuse)
# Independent host-permission probe; not used to build libguestfs.
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  python3-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python-libvirt
# Additional appliance dependencies beyond the standard build environment.
BuildRequires:  acl
BuildRequires:  attr
BuildRequires:  augeas
BuildRequires:  btrfs-progs
BuildRequires:  cryptsetup
BuildRequires:  dhcpcd
BuildRequires:  dosfstools
BuildRequires:  e2fsprogs
BuildRequires:  exfatprogs
BuildRequires:  f2fs-tools
BuildRequires:  gptfdisk
BuildRequires:  hivex
BuildRequires:  iproute2
BuildRequires:  iputils
BuildRequires:  json-c
BuildRequires:  kmod
BuildRequires:  less
BuildRequires:  libcap
BuildRequires:  libtirpc
BuildRequires:  libxml2
BuildRequires:  linux
BuildRequires:  lsof
BuildRequires:  lsscsi
BuildRequires:  lvm2
BuildRequires:  lzop
BuildRequires:  mdadm
BuildRequires:  ntfs-3g
BuildRequires:  openssh-clients
BuildRequires:  parted
BuildRequires:  pciutils
BuildRequires:  pcre2
BuildRequires:  procps-ng
BuildRequires:  psmisc
BuildRequires:  rsync
BuildRequires:  squashfs-tools
BuildRequires:  strace
BuildRequires:  systemd
BuildRequires:  systemd-udev
BuildRequires:  xfsprogs
BuildRequires:  zstd
BuildRequires:  pkgconfig(augeas)
BuildRequires:  pkgconfig(hivex)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  rpcgen
BuildRequires:  xorriso
BuildRequires:  perl
BuildRequires:  qemu
# qemu Requires qemu-user, also provided by qemu-user-static; pick one.
BuildRequires:  qemu-user
%ifarch x86_64
BuildRequires:  seabios
%endif

Requires:       qemu
Requires:       supermin
Requires:       xorriso
%ifarch x86_64
Requires:       seabios
%endif
# Keep these installed for supermin reconstruction, including the
# shared libraries used by guestfsd inside daemon.tar.gz.
Requires:       acl
Requires:       attr
Requires:       augeas
Requires:       bash
Requires:       binutils
Requires:       btrfs-progs
Requires:       bzip2
Requires:       coreutils
Requires:       cpio
Requires:       cryptsetup
Requires:       dhcpcd
Requires:       diffutils
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       exfatprogs
Requires:       f2fs-tools
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       gptfdisk
Requires:       grep
Requires:       gzip
Requires:       hivex
Requires:       iproute2
Requires:       iputils
Requires:       json-c
Requires:       kmod
Requires:       less
Requires:       libcap
Requires:       libtirpc
Requires:       libxml2
Requires:       linux
Requires:       lsof
Requires:       lsscsi
Requires:       lvm2
Requires:       lzop
Requires:       mdadm
Requires:       ntfs-3g
Requires:       openssh-clients
Requires:       parted
Requires:       pciutils
Requires:       pcre2
Requires:       procps-ng
Requires:       psmisc
Requires:       rpm
Requires:       rsync
Requires:       sed
Requires:       squashfs-tools
Requires:       strace
Requires:       systemd
Requires:       systemd-udev
Requires:       tar
Requires:       util-linux
Requires:       xfsprogs
Requires:       xz
Requires:       zstd

%description
Libguestfs is a set of tools for accessing and modifying virtual
machine disk images. It can inspect guests, copy files in and out, and
run commands in the guest. This build ships the C library and
command-line tools, including a supermin appliance with guestfsd.
The bootable appliance is assembled and cached on first use.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the headers and linker files needed to build
software against %{name}.

%package     -n python-%{name}
Summary:        Python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3
Provides:       python3-%{name} = %{version}-%{release}

%description -n python-%{name}
The guestfs Python module provides access to the libguestfs API for
inspecting and modifying virtual machine disk images.

%prep -a
# Regenerate the RPM distro conditional changed by Patch2000.
autoconf

%install -a
# Bindings were disabled; drop leftover man pages if the build still
# installed them.
rm -f %{buildroot}%{_mandir}/man3/guestfs-ocaml.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-perl.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-ruby.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-golang.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-java.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-lua.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-php.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-haskell.3*
rm -f %{buildroot}%{_mandir}/man3/guestfs-erlang.3*

# Generate packaged bytecode during installation, even with --nocheck.
%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}

%check
# Probe the existing FUSE 3 stack before testing our FUSE 2 integration.
# Some OBS hosts expose /dev/fuse but prohibit the mount operation.
%{__cc} %{build_cflags} %{SOURCE2001} -o fuse3-host-probe $(pkg-config --cflags --libs fuse3) %{build_ldflags}
probe_status=0
python3 %{SOURCE2000} --probe-host ./fuse3-host-probe || probe_status=$?
case "$probe_status" in
    0) ;;
    77) export SKIP_TEST_FUSE_SH=1 OPENRUYI_SKIP_HOST_FUSE=1 ;;
    *) exit "$probe_status" ;;
esac

# Run library and daemon unit tests, then boot the appliance using TCG
# so validation does not require nested KVM in OBS workers.
%make_build -C lib check
%make_build -C daemon check
export LIBGUESTFS_BACKEND=direct
export LIBGUESTFS_BACKEND_SETTINGS=force_tcg
# Python libvirt tests need only this empty fixture, not all guest images.
%make_build -C test-data/phony-guests blank-disk.img
%make_build -C python check
# Run upstream FUSE tests which do not require the optional Fedora fixture.
%make_build -C fuse check TESTS="test-docs.sh test-guestunmount-fd test-guestunmount-not-mounted.sh test-fuse"
# Exercise the installed payload, including its packaged appliance.
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export LIBGUESTFS_PATH=%{buildroot}%{_libdir}/guestfs
%{buildroot}%{_bindir}/libguestfs-test-tool --timeout 600

# Check that a file survives shutdown and reopening the disk image.
%{buildroot}%{_bindir}/guestfish -N appliance-test.img=fs:ext4 -m /dev/sda1 <<'EOF'
write /openruyi-test "libguestfs appliance works"
sync
EOF
result=$(%{buildroot}%{_bindir}/guestfish --ro -a appliance-test.img -m /dev/sda1 cat /openruyi-test)
test "$result" = "libguestfs appliance works"
rm -f appliance-test.img

# Import the staged Python module, then exercise Python and host FUSE I/O.
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PATH=%{buildroot}%{_bindir}:$PATH
python3 %{SOURCE2000}

%files
%doc README
%license COPYING COPYING.LIB
%config(noreplace) %{_sysconfdir}/libguestfs-tools.conf
%{_bindir}/guestfish
%{_bindir}/guestmount
%{_bindir}/guestunmount
%{_bindir}/libguestfs-test-tool
%{_bindir}/libguestfs-make-fixed-appliance
%{_bindir}/virt-copy-in
%{_bindir}/virt-copy-out
%{_bindir}/virt-tar-in
%{_bindir}/virt-tar-out
%{_bindir}/virt-rescue
%{_libdir}/libguestfs.so.*
%{_libdir}/guestfs/
%{_datadir}/locale/*/LC_MESSAGES/libguestfs.mo
%{_mandir}/man1/guestfish.1*
%{_mandir}/man1/guestmount.1*
%{_mandir}/man1/guestunmount.1*
%{_mandir}/man1/libguestfs-test-tool.1*
%{_mandir}/man1/libguestfs-make-fixed-appliance.1*
%{_mandir}/man1/virt-copy-in.1*
%{_mandir}/man1/virt-copy-out.1*
%{_mandir}/man1/virt-tar-in.1*
%{_mandir}/man1/virt-tar-out.1*
%{_mandir}/man1/virt-rescue.1*
%{_mandir}/man1/guestfs-*.1*
%{_mandir}/man5/libguestfs-tools.conf.5*
%{bash_completions_dir}/*

%files devel
%{_includedir}/guestfs.h
%{_libdir}/libguestfs.so
%{_libdir}/pkgconfig/libguestfs.pc
%{_mandir}/man3/guestfs.3*
%{_mandir}/man3/guestfs-examples.3*
%{_mandir}/man3/libguestfs.3*

%files -n python-%{name}
%{python3_sitearch}/guestfs.py
%{python3_sitearch}/libguestfsmod*.so
%{python3_sitearch}/__pycache__/guestfs.*.pyc
%{_mandir}/man3/guestfs-python.3*

%changelog
%autochangelog
