# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define cross_target riscv64-openruyi-linux
%define cross_sysroot %{_prefix}/%{cross_target}/sys-root
%define host_triple x86_64-openruyi-linux
%define binsuffix -16

%global _lto_cflags %{nil}

Name:           cross-riscv64-glibc
Summary:        GNU C Library for %{cross_target} (sysroot)
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Version:        2.44
Release:        %autorelease
URL:            https://www.gnu.org/software/libc/libc.html
VCS:            git:https://forge.sourceware.org/glibc/glibc-mirror.git
#!RemoteAsset:  sha256:37f600f2bef3c5e8300147059568b2a2e40a7ad6ccc65ce942556d49429cc667
Source0:        https://ftpmirror.gnu.org/gnu/glibc/glibc-%{version}.tar.xz

# openRuyi patch
Patch2000:      glibc-2.4-china.diff

ExclusiveArch:  x86_64

BuildRequires:  cross-riscv64-gcc-bootstrap
BuildRequires:  cross-riscv64-linux-headers
BuildRequires:  bison
BuildRequires:  texinfo
BuildRequires:  python3
BuildRequires:  xz
BuildRequires:  pkgconfig(zlib)

# The whole target sysroot (glibc headers, startup objects, shared and static
# libraries) is shipped in this single package so that cross compilers always
# see a consistent sysroot. Downstream packages can build-depend on either
# this package or its -devel alias.
Provides:       cross-riscv64-glibc-devel = %{version}-%{release}

%description
GNU C Library for %{cross_target}, installed into %{cross_sysroot}.
This package provides the shared libraries, static archives and header
files required for linking cross-compiled RISC-V userspace programs.

%prep
%autosetup -n glibc-%{version} -p1

%build
# We do not want configure to pick up host tools mistakenly
target="%{cross_target}"
build="%{host_triple}"

enable_stack_protector=
BuildFlags=
tmp="%{build_cflags}"
for opt in $tmp; do
  case $opt in
    -fstack-protector-*) enable_stack_protector=${opt#-fstack-protector-} ;;
    -fstack-protector) enable_stack_protector=yes ;;
    -D_FORTIFY_SOURCE=*) enable_fortify_source=${opt#-D_FORTIFY_SOURCE=} ;;
    -ffortify=* | *_FORTIFY_SOURCE*) ;;
    *) BuildFlags+=" $opt" ;;
  esac
done

mkdir build-cross
cd build-cross

# Use the stage1 cross compiler and target binutils. The cross binutils
# installs unprefixed tool names under %{_prefix}/%{cross_target}/bin.
CC="%{cross_target}-gcc%{binsuffix}"
# Stage1 cross-gcc only builds the C frontend, so use the C driver as CXX
# too; glibc itself is C-only and configure accepts this gracefully.
CXX="%{cross_target}-gcc%{binsuffix}"
AR="%{_prefix}/%{cross_target}/bin/ar"
AS="%{_prefix}/%{cross_target}/bin/as"
LD="%{_prefix}/%{cross_target}/bin/ld"
NM="%{_prefix}/%{cross_target}/bin/nm"
OBJCOPY="%{_prefix}/%{cross_target}/bin/objcopy"
OBJDUMP="%{_prefix}/%{cross_target}/bin/objdump"
RANLIB="%{_prefix}/%{cross_target}/bin/ranlib"
STRIP="%{_prefix}/%{cross_target}/bin/strip"

../configure \
    CC="${CC}" \
    CXX="${CXX}" \
    CFLAGS="$BuildFlags" BUILD_CFLAGS="$BuildFlags" \
    AR="${AR}" AS="${AS}" LD="${LD}" NM="${NM}" \
    OBJCOPY="${OBJCOPY}" OBJDUMP="${OBJDUMP}" \
    RANLIB="${RANLIB}" STRIP="${STRIP}" \
    --build=%{host_triple} \
    --host=${target} \
    --prefix=%{_prefix} \
    --libexecdir=%{_libexecdir} \
    --infodir=%{_infodir} \
    libdir=%{_prefix}/lib64 \
    slibdir=%{_prefix}/lib64 \
    --enable-stackguard-randomization \
    --enable-tunables \
    --enable-kernel=4.15 \
    --with-headers=%{cross_sysroot}/usr/include \
    --with-bugurl="%{_vendor_bug_url}" \
    --enable-bind-now \
    --disable-timezone-tools \
    --disable-build-nscd \
    --disable-nscd \
    --disable-crypt

%make_build

%install
export NO_BRP_STRIP_DEBUG=true
export STRIP_KEEP_SYMTAB=*.so*
mkdir -p %{buildroot}/%{cross_sysroot}
%make_install install_root=%{buildroot}/%{cross_sysroot} -C build-cross \
    libdir=%{_prefix}/lib64 slibdir=%{_prefix}/lib64

# Drop host-side artifacts that must not live in the cross sysroot.
rm -rf %{buildroot}/%{cross_sysroot}/%{_infodir}
rm -rf %{buildroot}/%{cross_sysroot}/%{_datadir}
rm -rf %{buildroot}/%{cross_sysroot}/%{_libexecdir}
rm -rf %{buildroot}/%{cross_sysroot}/%{_bindir}
rm -rf %{buildroot}/%{cross_sysroot}/%{_sbindir}
rm -rf %{buildroot}/%{cross_sysroot}/etc
rm -rf %{buildroot}/%{cross_sysroot}/var
rm -rf %{buildroot}/%{cross_sysroot}/run
rm -rf %{buildroot}/%{cross_sysroot}/sbin
rm -rf %{buildroot}/%{cross_sysroot}/usr/sbin

# On riscv64 openRuyi keeps shared libraries in /usr/lib64 while the
# dynamic linker lives in /usr/lib (mirrors the native, usrmerged glibc
# package). glibc may install the loader into slibdir; move it to usr/lib.
mkdir -p %{buildroot}/%{cross_sysroot}/usr/lib64
mkdir -p %{buildroot}/%{cross_sysroot}/usr/lib
for d in lib usr/lib64; do
    if [ -e "%{buildroot}/%{cross_sysroot}/$d/ld-linux-riscv64-lp64d.so.1" ]; then
        mv "%{buildroot}/%{cross_sysroot}/$d/ld-linux-riscv64-lp64d.so.1" \
           %{buildroot}/%{cross_sysroot}/usr/lib/
    fi
done
# openRuyi is usrmerged: /lib is a symlink to usr/lib. Replace any real
# lib/ directory with that symlink so /lib/... references resolve.
rm -rf %{buildroot}/%{cross_sysroot}/lib
ln -sfn usr/lib %{buildroot}/%{cross_sysroot}/lib
# The lp64d -> . symlink is expected by some programs doing path lookups.
ln -sf . %{buildroot}/%{cross_sysroot}/usr/lib64/lp64d

%files
%defattr(-,root,root)
%license COPYING.LIB
%dir %{cross_sysroot}/usr
%dir %{cross_sysroot}/usr/lib
%dir %{cross_sysroot}/usr/lib64
%dir %{cross_sysroot}/usr/include
%{cross_sysroot}/lib
%{cross_sysroot}/usr/lib/
%{cross_sysroot}/usr/lib64/
%{cross_sysroot}/usr/include/

%changelog
%autochangelog
