# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define cross_target riscv64-openruyi-linux
%define cross_sysroot %{_prefix}/%{cross_target}/sys-root
%define cross_arch riscv64

%define vermajor 16
%define binsuffix -%{vermajor}
%define gcc_dir_version %(echo %{version} | sed 's/+.*//' | cut -d '.' -f 1)
%define host_triple x86_64-openruyi-linux

Name:           cross-riscv64-gcc-bootstrap
Version:        16.2.0
Release:        %autorelease
Summary:        Stage1 GNU Compiler Collection (bootstrap) targeting %{cross_target}
License:        GPL-3.0-or-later AND GPL-3.0-or-later WITH GCC-exception-3.1
URL:            https://gcc.gnu.org/
#!RemoteAsset:  sha256:e6738e29597f733270731aa90600f37ffdc045079dfc27ec7e8192cc81085c3e
Source:         https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz

# Patches from native gcc16
Patch1001:      1001-UPSTREAM-RISC-V-PR-target-127306-Fix-two-bugs-in-ADDI-AND-CTZ.patch
Patch1002:      1002-UPSTREAM-RISC-V-Fix-problems-with-bclr-variable-bit-optimizat.patch
Patch2000:      2000-textdomain.patch
Patch2001:      2001-rename-info-files.patch

ExclusiveArch:  x86_64

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext-devel
BuildRequires:  texinfo
BuildRequires:  perl
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  mpc-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(isl)
BuildRequires:  cross-riscv64-binutils
Requires:       cross-riscv64-binutils

%description
Stage 1 cross-compiler (bootstrap) targeting %{cross_target}.
This package produces a minimal C compiler sufficient to compile a
cross glibc. It is NOT intended for general use — install the
cross-riscv64-gcc package instead for a fully-featured cross compiler.

%prep
%autosetup -p1 -n gcc-%{version}

%build
%define _lto_cflags %{nil}
contrib/gcc_update --touch

rm -rf obj-bootstrap
mkdir obj-bootstrap
cd obj-bootstrap

optflags=
for flag in $RPM_OPT_FLAGS; do
  case $flag in
    -U_FORTIFY_SOURCE|-D_FORTIFY_SOURCE=*) ;;
    -fno-rtti|-fno-exceptions|-Wmissing-format-attribute|-fstack-protector*) ;;
    -ffortify=*|-Wall|-m32|-m64|-Werror=format-security) ;;
    *) optflags="$optflags $flag" ;;
  esac
done

export _POSIX2_VERSION=199209

../configure \
    CFLAGS="$optflags" \
    CXXFLAGS="$optflags" \
    --prefix=%{_prefix} \
    --infodir=%{_infodir} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libdir} \
    --enable-languages=c \
    --disable-checking \
    --disable-werror \
    --enable-ssp \
    --disable-libssp \
    --disable-libvtv \
    --disable-libcc1 \
    --disable-plugin \
    --with-bugurl="%{_vendor_bug_url}" \
    --with-pkgversion="%{_vendor_name}" \
    --with-slibdir=%{_libdir} \
    --with-system-zlib \
    --enable-version-specific-runtime-libs \
    --with-gcc-major-version-only \
    --program-prefix=%{cross_target}- \
    --program-suffix=%{binsuffix} \
    --target=%{cross_target} \
    --build=%{host_triple} \
    --host=%{host_triple} \
    --with-build-time-tools=%{_prefix}/%{cross_target}/bin \
    --without-headers \
    --with-newlib \
    --disable-gcov \
    --disable-threads \
    --disable-shared \
    --disable-libgomp \
    --disable-libquadmath \
    --disable-libatomic \
    --disable-libsanitizer \
    --disable-nls \
    --disable-multilib \
%if "%{?openruyi_riscv_arch}" == "-march=rva20u64"
    --with-arch=rva20u64 \
%else
    --with-arch=rva23u64 \
%endif
    --with-abi=lp64d

make %{?_smp_mflags}

%install
cd obj-bootstrap
make DESTDIR=%{buildroot} install

# Strip host parts that conflict with native gcc
rm -f %{buildroot}/%{_infodir}/dir
rm -rf %{buildroot}/%{_mandir}
rm -rf %{buildroot}/%{_infodir}
rm -f %{buildroot}/%{_libdir}/libiberty.a
# Remove everything but the cross compiler (keep gcc and cpp)
find %{buildroot}%{_bindir} -maxdepth 1 -type f | while read f; do
  name=$(basename "$f")
  case "$name" in
    %{cross_target}-gcc%{binsuffix}) ;;
    %{cross_target}-cpp%{binsuffix}) ;;
    *) rm -f "$f" ;;
  esac
done

%files
%defattr(-,root,root)
%{_bindir}/%{cross_target}-*
%dir %{_libdir}/gcc/%{cross_target}
%{_libdir}/gcc/%{cross_target}

%changelog
%autochangelog
