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
%define build_cp 1

Name:           cross-riscv64-gcc
Version:        16.2.0
Release:        %autorelease
Summary:        The GNU Compiler Collection targeting %{cross_target}
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
BuildRequires:  cross-riscv64-linux-headers
BuildRequires:  cross-riscv64-glibc-devel
Requires:       cross-riscv64-binutils
Requires:       cross-riscv64-linux-headers
Requires:       cross-riscv64-glibc-devel
# The stage1 bootstrap shares libexec/gcc paths and must not be installed
# alongside this final compiler. Users install only the final package; only
# the glibc build consumes the bootstrap.
Conflicts:      cross-riscv64-gcc-bootstrap

%description
The GNU Compiler Collection as a cross-compiler targeting %{cross_target},
built against a RISC-V glibc sysroot. Supports C (and C++ with the
cross-riscv64-gcc-c++ subpackage).

%package        c++
Summary:        The GNU C++ Compiler for %{cross_target}
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       cross-riscv64-glibc-devel
# The generic (non-target) libstdc++ headers come from the host compiler.
Requires:       libstdc++-devel-gcc%{vermajor}

%description    c++
This package contains the GNU C++ compiler for cross-development
targeting %{cross_target}.

%prep
%autosetup -p1 -n gcc-%{version}

%build
%define _lto_cflags %{nil}
contrib/gcc_update --touch

rm -rf obj-cross
mkdir obj-cross
cd obj-cross

optflags=
optflags_d=
for flag in $RPM_OPT_FLAGS; do
  add_flag=
  case $flag in
    -U_FORTIFY_SOURCE|-D_FORTIFY_SOURCE=*) ;;
    -fno-rtti|-fno-exceptions|-Wmissing-format-attribute|-fstack-protector*) ;;
    -ffortify=*|-Wall|-m32|-m64|-Werror=format-security) ;;
    -march=*|-mtune=*|-mcpu=*) ;;
    *) add_flag=$flag ;;
  esac
  if test -n "$add_flag"; then
    optflags="$optflags $add_flag"
    case $add_flag in
      -Werror=return-type) ;;
      *) optflags_d="$optflags_d $add_flag" ;;
    esac
  fi
done

languages=c
%if %{build_cp}
languages=$languages,c++
%endif

export _POSIX2_VERSION=199209

../configure \
    CFLAGS="$optflags" \
    CXXFLAGS="$optflags" \
    XCFLAGS="$optflags" \
    TCFLAGS="$optflags" \
    GDCFLAGS="$optflags_d" \
    --prefix=%{_prefix} \
    --infodir=%{_infodir} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libdir} \
    --enable-languages=$languages \
    --enable-checking=release \
    --disable-werror \
    --with-gxx-include-dir=%{_prefix}/include/c++/%{gcc_dir_version} \
    --with-libstdcxx-zoneinfo=%{_datadir}/zoneinfo \
    --enable-ssp \
    --disable-libssp \
    --disable-libvtv \
    --disable-libcc1 \
    --disable-plugin \
    --with-bugurl="%{_vendor_bug_url}" \
    --with-pkgversion="%{_vendor_name}" \
    --with-slibdir=%{cross_sysroot}/usr/lib64 \
    --with-system-zlib \
    --enable-libstdcxx-allocator=new \
    --disable-libstdcxx-pch \
    --enable-version-specific-runtime-libs \
    --with-gcc-major-version-only \
    --enable-linker-build-id \
    --enable-linux-futex \
    --disable-libsanitizer \
    --program-prefix=%{cross_target}- \
    --program-suffix=%{binsuffix} \
    --target=%{cross_target} \
    --with-sysroot=%{cross_sysroot} \
    --with-build-time-tools=%{_prefix}/%{cross_target}/bin \
%if "%{?openruyi_riscv_arch}" == "-march=rva20u64"
    --with-arch=rva20u64 \
%else
    --with-arch=rva23u64 \
%endif
    --with-abi=lp64d \
    --disable-multilib \
    --disable-bootstrap \
    --enable-link-serialization \
    --build=%{host_triple} \
    --host=%{host_triple}

make %{?_smp_mflags}

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
cd obj-cross

make DESTDIR=%{buildroot} install-host
rm -rf %{buildroot}/%{_libdir}/gcc/%{cross_target}/%{gcc_dir_version}/install-tools
rm -f %{buildroot}/%{_libdir}/gcc/%{cross_target}/%{gcc_dir_version}/liblto_plugin.la
rm -f %{buildroot}/%{_libdir}/libiberty.a

# install target parts (libgcc, libstdc++ runtimes land in sysroot)
mkdir -p %{buildroot}/%{cross_sysroot}
make DESTDIR=%{buildroot} install-target

# Because of --enable-version-specific-runtime-libs the target shared
# runtimes (libstdc++, libgomp, ...) are installed into the compiler-private
# directory. Move them into the sysroot so the cross toolchain is
# self-contained, matching the usual cross layout (e.g. Debian ships
# <sysroot>/usr/lib64/libstdc++.so.6). sysroot/usr/lib64 is already part of the
# default library search path; libgcc_s is placed in the sysroot by
# --with-slibdir.
privlib=%{buildroot}/%{_libdir}/gcc/%{cross_target}/%{gcc_dir_version}
syslib=%{buildroot}/%{cross_sysroot}/usr/lib64
mkdir -p "$syslib"
for libname in libstdc++ libgomp libatomic libitm; do
    for f in "$privlib/$libname".so "$privlib/$libname".so.*; do
        [ -e "$f" ] || [ -L "$f" ] || continue
        mv "$f" "$syslib/"
    done
done

%if %{build_cp}
# The generic libstdc++ headers are shared with the native gcc and are owned
# by libstdc++-devel-gcc16 (see Requires below); keep only the
# target-specific subdirectory to avoid file conflicts with the native gcc.
find %{buildroot}/%{_prefix}/include/c++/%{gcc_dir_version} -mindepth 1 -maxdepth 1 \
    -type d -not -name %{cross_target} -prune -exec rm -rf {} +
find %{buildroot}/%{_prefix}/include/c++/%{gcc_dir_version} -maxdepth 1 -type f -delete
%endif

# remove docs and host-side locale/pretty-printer data
rm -rf %{buildroot}/%{_mandir}
rm -rf %{buildroot}/%{_infodir}
rm -rf %{buildroot}/%{_datadir}/locale
rm -rf %{buildroot}/%{_datadir}/gcc-%{vermajor}

%files
%defattr(-,root,root)
%{_bindir}/%{cross_target}-*
%dir %{_libdir}/gcc/%{cross_target}
%{_libdir}/gcc/%{cross_target}/
%dir %{cross_sysroot}/usr/lib64
%{cross_sysroot}/usr/lib64/libgcc_s.so*
%{cross_sysroot}/usr/lib64/libgcc_s_asneeded.so
%{cross_sysroot}/usr/lib64/libstdc++.so*
%{cross_sysroot}/usr/lib64/libgomp.so*
%{cross_sysroot}/usr/lib64/libatomic.so*
%{cross_sysroot}/usr/lib64/libitm.so*

%files c++
%defattr(-,root,root)
%dir %{_prefix}/include/c++/%{gcc_dir_version}
%{_prefix}/include/c++/%{gcc_dir_version}/%{cross_target}

%changelog
%autochangelog
