# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: jchzhou <zhoujiacheng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%ifarch riscv64
#!BuildConstraint: hardware:jobs 32
%endif

%define _slibdir  %{_libdir}
%define slibdir   %{_prefix}/lib
%define slibdir64 %{_prefix}/lib64
%define usrmerged 1

%bcond_without bootstrap

%define quadmath_arch x86_64
%define tsan_arch x86_64 riscv64
%define asan_arch x86_64 riscv64
%define hwasan_arch x86_64
%define itm_arch x86_64 riscv64
%define atomic_arch x86_64 riscv64
%define lsan_arch x86_64 riscv64
%define ubsan_arch x86_64 riscv64

# If we want to enable this we need to explicitly enable it
%if 0%{?build_libvtv:1}
%define vtv_arch x86_64
%endif

%define build_fortran 1
%define build_objcp 1
%define build_go 1
%define build_d 0
%define build_m2 1
%if %{build_objcp}
%define build_cp 1
%define build_objc 1
%endif

# rust is still experimental
%define build_rust 0

%define use_lto_bootstrap 0
%ifarch x86_64
%define use_lto_bootstrap %{with bootstrap}
%endif

# Bruh please make it work in the future?
%define build_ada 0

%define enable_plugins 1
%define build_jit 0

%define hostsuffix %{nil}

%define binsuffix -16
# libFOO runtime package suffix
%define libsuffix -gcc16
# libFOO-devel package suffix
%define libdevel_suffix -gcc16
%define biarch_targets x86_64

%define gcc_dir_version %(echo %version |  sed 's/+.*//' | cut -d '.' -f 1)
%define gcc_snapshot_revision %(echo %version | sed 's/[3-9]\.[0-9]\.[0-6]//' | sed 's/+/-/')


Name:           gcc16
URL:            https://gcc.gnu.org/
Version:        16.1.0
Release:        %autorelease
License:        GPL-3.0-or-later
Summary:        The GNU C Compiler and Support Files
#!RemoteAsset:  sha256:50efb4d94c3397aff3b0d61a5abd748b4dd31d9d3f2ab7be05b171d36a510f79
Source:         https://ftpmirror.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz

BuildRequires:  xz
BuildRequires:  pkgconfig(libzstd)
# With generated files in src we could drop the following
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext-devel
BuildRequires:  texinfo
# until here, but at least renaming and patching info files breaks this
BuildRequires:  gcc-c++
BuildRequires:  mpc-devel
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  perl
BuildRequires:  pkgconfig(zlib)
# for SDT markers in the C++ unwinder and gdb breakpoints on exceptions
BuildRequires:  systemtap-sdt-devel
BuildRequires:  pkgconfig(isl)

%if %{build_ada}
%if 0%{?gcc_version:%{gcc_version}} > 14
%define hostsuffix %{binsuffix}
BuildRequires:  gcc16-ada
BuildRequires:  gcc16-c++
%else
%define hostsuffix %{nil}
BuildRequires:  gcc-ada
%endif
%endif
%if %{build_d}
BuildRequires:  gcc-d
%endif
#!BuildIgnore: gcc-PIE

%ifarch x86_64 riscv64
# 64-bit is primary build target
%define build_primary_64bit 1
%else
%define build_primary_64bit 0
%endif

# TODO: Revisit here
Requires:       binutils
Requires:       cpp16 = %{version}-%{release}
Requires:       glibc-devel
Requires:       libgomp%{libsuffix} >= %{version}-%{release}
%ifarch %{asan_arch}
Requires:       libasan%{libsuffix} >= %{version}-%{release}
%endif
%ifarch %{tsan_arch}
%if %{build_primary_64bit}
Requires:       libtsan%{libsuffix} >= %{version}-%{release}
%endif
%endif
%ifarch %{hwasan_arch}
Requires:       libhwasan%{libsuffix} >= %{version}-%{release}
%endif
%ifarch %{atomic_arch}
Requires:       libatomic%{libsuffix} >= %{version}-%{release}
%endif
%ifarch %{itm_arch}
Requires:       libitm%{libsuffix} >= %{version}-%{release}
%endif
%ifarch %{lsan_arch}
%if %{build_primary_64bit}
Requires:       liblsan%{libsuffix} >= %{version}-%{release}
%endif
%endif
%ifarch %{ubsan_arch}
Requires:       libubsan%{libsuffix} >= %{version}-%{release}
%endif
%ifarch %{vtv_arch}
Requires:       libvtv%{libsuffix} >= %{version}-%{release}
%endif
Suggests:       gcc16-doc

Patch2000:      2000-textdomain.patch
Patch2001:      2001-rename-info-files.patch

%description
Core package for the GNU Compiler Collection, including the C language
frontend.

Language frontends other than C are split to different sub-packages,
namely gcc-ada, gcc-c++, gcc-fortran, gcc-obj, gcc-obj-c++, gcc-go,
gcc-rust and gcc-m2.

%package        devel
Summary:        GCC plugins development enviroment
Requires:       gcc16 = %{version}-%{release}
Requires:       pkgconfig(gmp)
Requires:       mpc-devel

%description    devel
Files required for developing and compiling GCC plugins.

%package        c++
Summary:        The GNU C++ Compiler
Requires:       gcc16 = %{version}-%{release}
Requires:       gcc16-c++ = %{version}-%{release}
Requires:       libstdc++-devel%{libdevel_suffix} = %{version}-%{release}

%description    c++
This package contains the GNU compiler for C++.

%package        lib
Summary:        C compiler runtime library

%description    lib
This package is needed for dynamically linked C programs.

%package     -n libstdc++%{libsuffix}
Summary:        The standard C++ shared library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
# The std::chrono timezone database is provided by timezone
# (/usr/share/zoneinfo/tzdata.zi), without that the tzdb is empty and
# will only provide UTC.  We don't want a Requires here though, instead
# the overall product needs to decide what to provide,

%description -n libstdc++%{libsuffix}
The standard C++ library, needed for dynamically linked C++ programs.

%package     -n libstdc++-devel%{libdevel_suffix}
Summary:        Include Files and Libraries mandatory for Development
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       glibc-devel
Requires:       libstdc++%{libsuffix} >= %{version}-%{release}

%description -n libstdc++-devel%{libdevel_suffix}
This package contains all the headers and libraries of the standard C++
library. It is needed for compiling C++ code.

%package     -n libgomp%{libsuffix}
Summary:        The GNU compiler collection OpenMP runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1

%description -n libgomp%{libsuffix}
This is the OpenMP runtime library needed by OpenMP enabled programs
that were built with the -fopenmp compiler option and by programs that
were auto-parallelized via the -ftree-parallelize-loops compiler
option.

%package        doc
Summary:        Documentation for the GNU compiler collection
License:        GFDL-1.2-only
PreReq:         texinfo
BuildArch:      noarch

%description    doc
GNU info-pages for the GNU compiler collection covering both user-level
and internals documentation.

%package        objc
Summary:        GNU Objective C Compiler
License:        GPL-3.0-or-later
Requires:       gcc16 = %{version}-%{release}
Requires:       gcc16-objc = %{version}-%{release}
Requires:       libobjc%{libsuffix} >= %{version}-%{release}

%description    objc
This package contains the GNU Objective C compiler. Objective C is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package     -n libobjc%{libsuffix}
Summary:        Library for the GNU Objective C Compiler
License:        GPL-3.0-or-later WITH GCC-exception-3.1

%description -n libobjc%{libsuffix}
The library for the GNU Objective C compiler.

%package        obj-c++
Summary:        GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Requires:       gcc16-c++ = %{version}-%{release}
Requires:       gcc16-obj-c++ = %{version}-%{release}
Requires:       gcc16-objc = %{version}-%{release}

%description    obj-c++
This package contains the GNU Objective C++ compiler. Objective C++ is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package     -n cpp16
Summary:        The GCC Preprocessor
License:        GPL-3.0-or-later

%description -n cpp16
This Package contains just the preprocessor that is used by the X11
packages.

%package        ada
Summary:        GNU Ada Compiler Based on GCC (GNAT)
License:        GPL-3.0-or-later
Requires:       gcc16 = %{version}-%{release}
Requires:       gcc16-ada = %{version}-%{release}

%description    ada
This package contains an Ada compiler and associated development
tools based on the GNU GCC technology.

%package        fortran
Summary:        The GNU Fortran Compiler and Support Files
License:        GPL-3.0-or-later
Requires:       gcc16 = %{version}-%{release}
Requires:       gcc16-fortran = %{version}-%{release}
Requires:       libgfortran%{libsuffix} >= %{version}-%{release}
%ifarch %{quadmath_arch}
Requires:       libquadmath-devel%{libdevel_suffix} = %{version}-%{release}
%endif

%description    fortran
This is the Fortran compiler of the GNU Compiler Collection (GCC).

%package     -n libgfortran%{libsuffix}
Summary:        The GNU Fortran Compiler Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%ifarch %{quadmath_arch}
Requires:       libquadmath%{libsuffix} >= %{version}-%{release}
%endif

%description -n libgfortran%{libsuffix}
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC).

%package     -n libquadmath%{libsuffix}
Summary:        The GNU Fortran Compiler Quadmath Runtime Library
License:        LGPL-2.1-only

%description -n libquadmath%{libsuffix}
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC) and quadruple precision floating point
operations.

%package     -n libquadmath-devel%{libdevel_suffix}
Summary:        The GNU Fortran Compiler Quadmath Runtime Library Development Files
License:        LGPL-2.1-only
Requires:       libquadmath%{libsuffix} >= %{version}-%{release}

%description -n libquadmath-devel%{libdevel_suffix}
The libquadmatah runtime library development files.

%package     -n libitm%{libsuffix}
Summary:        The GNU Compiler Transactional Memory Runtime Library
License:        MIT

%description -n libitm%{libsuffix}
The runtime library needed to run programs compiled with the
-fgnu-tm option of the GNU Compiler Collection (GCC).

%package     -n libasan%{libsuffix}
Summary:        The GNU Compiler Address Sanitizer Runtime Library
License:        MIT

%description -n libasan%{libsuffix}
The runtime library needed to run programs compiled with the
-fsanitize=address option of the GNU Compiler Collection (GCC).

%package     -n libtsan%{libsuffix}
Summary:        The GNU Compiler Thread Sanitizer Runtime Library
License:        MIT

%description -n libtsan%{libsuffix}
The runtime library needed to run programs compiled with the
-fsanitize=thread option of the GNU Compiler Collection (GCC).

%package     -n libhwasan%{libsuffix}
Summary:        The GNU Compiler Hardware-assisted Address Sanitizer Runtime Library
License:        MIT

%description -n libhwasan%{libsuffix}
The runtime library needed to run programs compiled with the
-fsanitize=hwaddress option of the GNU Compiler Collection (GCC).

%package     -n libatomic%{libsuffix}
Summary:        The GNU Compiler Atomic Operations Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1

%description -n libatomic%{libsuffix}
The runtime library for atomic operations of the GNU Compiler Collection (GCC).

%package     -n liblsan%{libsuffix}
Summary:        The GNU Compiler Leak Sanitizer Runtime Library
License:        MIT

%description -n liblsan%{libsuffix}
The runtime library needed to run programs compiled with the
-fsanitize=leak option of the GNU Compiler Collection (GCC).

%package     -n libubsan%{libsuffix}
Summary:        The GNU Compiler Undefined Sanitizer Runtime Library
License:        MIT

%description -n libubsan%{libsuffix}
The runtime library needed to run programs compiled with the
-fsanitize=undefined option of the GNU Compiler Collection (GCC).

%package     -n libvtv%{libsuffix}
Summary:        The GNU Compiler Vtable Verifier Runtime Library
License:        MIT

%description -n libvtv%{libsuffix}
The runtime library needed to run programs compiled with the
-fvtable-verify option of the GNU Compiler Collection (GCC).

%package        go
Summary:        GNU Go Compiler
License:        GPL-3.0-or-later
Requires:       gcc16 = %{version}-%{release}
Requires:       gcc16-go = %{version}-%{release}
Requires:       libgo%{libsuffix} >= %{version}-%{release}

%description    go
This package contains a Go compiler and associated development
files based on the GNU GCC technology.

%package     -n libgo%{libsuffix}
Summary:        GNU Go compiler runtime library
License:        BSD-3-Clause

%description -n libgo%{libsuffix}
Runtime library for the GNU Go language.

%package        d
Summary:        GNU D Compiler
License:        GPL-3.0-or-later
Requires:       gcc16 = %{version}-%{release}
Requires:       gcc16-d = %{version}-%{release}

%description   d
This package contains a D compiler and associated development
files based on the GNU GCC technology.

%package     -n libgccjit%{libsuffix}
Summary:        The GNU Compiler Collection JIT library
License:        GPL-3.0-or-later
# At runtime the JIT needs to be able to invoke the assembler and
# linker and find startfiles and libgcc.  The built-in driver knows
# the compilers version install directory only so we require the
# respective compiler libgccjit was built from.
Requires:       gcc16

%description -n libgccjit%{libsuffix}
Support for embedding GCC inside programs and libraries

%package     -n libgccjit-devel%{libdevel_suffix}
Summary:        Support for embedding GCC inside programs and libraries
License:        GPL-3.0-or-later
Requires:       libgccjit%{libsuffix} >= %{version}-%{release}

%description -n libgccjit-devel%{libdevel_suffix}
Package contains header files and documentation for GCC JIT front-end.

%package        rust
Summary:        GNU Rust Compiler
License:        GPL-3.0-or-later
Requires:       gcc16 = %{version}-%{release}
Requires:       gcc16-rust = %{version}-%{release}

%description    rust
This package contains a Rust compiler.

%package        m2
Summary:        GNU Modula-2 Compiler
License:        GPL-3.0-or-later
Requires:       gcc16 = %{version}-%{release}
Requires:       gcc16-m2 = %{version}-%{release}
Requires:       libm2%{libsuffix} >= %{version}-%{release}
Requires:       libstdc++-devel%{libdevel_suffix} = %{version}-%{release}

%description    m2
This package contains a Modula-2 compiler.

%package     -n libm2%{libsuffix}
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0

%description -n libm2%{libsuffix}
Runtime library for the GNU Modula-2 language.


%define TARGET_ARCH %(echo %{_target_cpu})
%define HOST_ARCH %(echo %{_target_cpu})

%define GCCDIST %{HOST_ARCH}-openruyi-linux

%define libsubdir %{_libdir}/gcc/%{GCCDIST}/%{gcc_dir_version}
%define gxxinclude %{_prefix}/include/c++/%{gcc_dir_version}
%define versmainlibdir %{libsubdir}
%define mainlibdir %{_libdir}

# Synchronize output by lines, useful for configure output
%define make_output_sync -Oline

%prep
%setup -q -n gcc-%{version}

#test patching start
%patch -p1 -P 2000 -P 2001
#test patching end

%build
%define _lto_cflags %{nil}
# Avoid rebuilding of generated files
contrib/gcc_update --touch

rm -rf obj-%{GCCDIST}
mkdir obj-%{GCCDIST}
cd obj-%{GCCDIST}
# Filter out unwanted flags from $RPM_OPT_FLAGS
optflags=
optflags_d=
for flag in $RPM_OPT_FLAGS; do
  add_flag=
  case $flag in
    -U_FORTIFY_SOURCE|-D_FORTIFY_SOURCE=*) ;;
    -fno-rtti|-fno-exceptions|-Wmissing-format-attribute|-fstack-protector*) ;;
    -ffortify=*|-Wall|-m32|-m64) ;;
    -Werror=format-security) ;;
  *) add_flag=$flag ;;
  esac
  if test -n "$add_flag"; then
    optflags+=" $add_flag"
    case $add_flag in
      # Filter out -Werror=return-type for D (only valid for C and C++)
      -Werror=return-type) ;;
      *) optflags_d+=" $add_flag" ;;
    esac
  fi
done

languages=c
%if %{build_cp}
languages=$languages,c++
%endif
%if %{build_objc}
languages=$languages,objc
%endif
%if %{build_fortran}
languages=$languages,fortran
%endif
%if %{build_objcp}
languages=$languages,obj-c++
%endif
%if %{build_ada}
languages=$languages,ada
%endif
%if %{build_go}
languages=$languages,go
%endif
%if %{build_d}
languages=$languages,d
%endif
%if %{build_jit}
languages=$languages,jit
%endif
%if %{build_rust}
languages=$languages,rust
%endif
%if %{build_m2}
languages=$languages,m2
%endif

# In general we want to ship release checking enabled compilers
# which is the default for released compilers
ENABLE_CHECKING="--enable-checking=release"

# Work around tail/head -1 changes
export _POSIX2_VERSION=199209

%if "%{hostsuffix}" != ""
mkdir -p host-tools/bin
# Using the host gnatmake like
#   CC="gcc%%{hostsuffix}" GNATBIND="gnatbind%%{hostsuffix}"
#   GNATMAKE="gnatmake%%{hostsuffix}"
%if %{build_ada}
cp -a /usr/bin/gnatmake%{hostsuffix} host-tools/bin/gnatmake
cp -a /usr/bin/gnatlink%{hostsuffix} host-tools/bin/gnatlink
cp -a /usr/bin/gnatbind%{hostsuffix} host-tools/bin/gnatbind
%endif
cp -a /usr/bin/gcc%{hostsuffix} host-tools/bin/gcc
cp -a /usr/bin/g++%{hostsuffix} host-tools/bin/g++
ln -sf /usr/%{_lib} host-tools/%{_lib}
export PATH="`pwd`/host-tools/bin:$PATH"
%endif

export CARGO=/bin/true

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
%if %{build_jit}
  --enable-host-shared \
%endif
  $ENABLE_CHECKING \
  --disable-werror \
  --with-gxx-include-dir=%{_prefix}/include/c++/%{gcc_dir_version} \
  --with-libstdcxx-zoneinfo=%{_datadir}/zoneinfo \
  --enable-ssp \
  --disable-libssp \
%if 0%{!?build_libvtv:1}
  --disable-libvtv \
%endif
  --enable-cet=auto \
  --disable-libcc1 \
%if %{enable_plugins}
  --enable-plugin \
%else
  --disable-plugin \
%endif
  --with-bugurl="%{_vendor_bug_url}" \
  --with-pkgversion="%{_vendor_name}" \
%if 0%{?sysroot:1}
  --with-slibdir=%{sysroot}/%{_lib} \
%else
  --with-slibdir=/%{_lib} \
%endif
  --enable-default-pie \
  --with-system-zlib \
  --enable-libstdcxx-allocator=new \
  --disable-libstdcxx-pch \
%if %{build_d}
  --enable-libphobos \
%endif
  --enable-version-specific-runtime-libs \
  --with-gcc-major-version-only \
  --enable-linker-build-id \
  --enable-linux-futex \
%ifarch x86_64
  --enable-gnu-indirect-function \
%endif
  --program-suffix=%{binsuffix} \
  --without-system-libunwind \
%if "%{TARGET_ARCH}" == "x86_64"
  --disable-multilib \
  --with-arch=x86-64-v2 \
  --with-tune=generic \
%endif
%if "%{TARGET_ARCH}" == "riscv64"
  --disable-multilib \
%endif
%if %{with bootstrap}
%if %{use_lto_bootstrap} && !0%{?building_testsuite:1}
  --with-build-config=bootstrap-lto-lean \
%endif
%else
  --disable-bootstrap \
%endif
  --enable-link-serialization \
  $CONFARGS \
  --build=%{GCCDIST} \
  --host=%{GCCDIST} || \
  {
    rc=$?;
    echo "------- BEGIN config.log ------";
    %{__cat} config.log;
    echo "------- END config.log ------";
    exit $rc;
  }

STAGE1_FLAGS="-g -O2"

make %{?make_output_sync} STAGE1_CFLAGS="$STAGE1_FLAGS" BOOT_CFLAGS="$optflags" %{?_smp_mflags}
make info

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
cd obj-%{GCCDIST}
# Work around tail/head -1 changes
export _POSIX2_VERSION=199209
export LIBRARY_PATH=%{buildroot}/%{libsubdir}

%make_install

# Remove some useless .la files
for lib in libobjc libgfortran libquadmath libcaf_single \
    libgomp libgomp-plugin-hsa libstdc++ libsupc++ \
    libgo libasan libhwasan libatomic libitm libtsan liblsan libubsan libvtv \
    libstdc++fs libgdruntime libgphobos libstdc++exp \
    libm2cor libm2iso libm2log libm2min libm2pim; do
  rm -f %{buildroot}/%{versmainlibdir}/$lib.la
done

mkdir -p %{buildroot}/%{_libdir}

%if %{build_cp}
# Merge multilib c++config.h to allow omitting the duplicate and
# identical other arch specific headers
dir_ml=
cxxconfig="`find %{GCCDIST}/libstdc++-v3/include -name c++config.h`"
for i in `find %{GCCDIST}/[36]*/libstdc++-v3/include -name c++config.h 2>/dev/null`; do
  if ! diff -up $cxxconfig $i; then
    file_32=x
    file_64=x
    case $i in
      %{GCCDIST}/32/*)
        file_32=$i
        file_64=$cxxconfig
        dir_ml=32
  ;;
      %{GCCDIST}/64/*)
        file_32=$cxxconfig
  file_64=$i
        dir_ml=64
  ;;
    esac
    if ! ( test -f "$file_32" && test -f "$file_64" ); then
      echo "Urgs?"
      exit 1
    fi

    cat > %{buildroot}/%{_prefix}/include/c++/%{gcc_dir_version}/%{GCCDIST}/bits/c++config.h <<EOF
#ifndef _CPP_CPPCONFIG_WRAPPER
#define _CPP_CPPCONFIG_WRAPPER 1
#include <bits/wordsize.h>
#if __WORDSIZE == 32
`cat $file_32`
#else
`cat $file_64`
#endif
#endif
EOF
    break
  fi
done
rm -rf %{buildroot}/%{_prefix}/include/c++/%{gcc_dir_version}/%{GCCDIST}/[36]*
if ! test -z "$dir_ml"; then
  ln -s . %{buildroot}/%{_prefix}/include/c++/%{gcc_dir_version}/%{GCCDIST}/$dir_ml
fi
%endif

# move shared libs from versionspecific dir to main libdir
for libname in \
%if %{build_fortran}
  libgfortran \
%endif
%ifarch %{quadmath_arch}
  libquadmath \
%endif
%if %{build_objc}
  libobjc \
%endif
%if %{build_cp}
  libstdc++ \
%endif
%if %{build_go}
  libgo \
%endif
%if %{build_d}
  libgdruntime \
  libgphobos \
%endif
  libgomp \
%if %{build_m2}
  libm2log \
  libm2cor \
  libm2iso \
  libm2pim \
  libm2min \
%endif
%ifarch %{atomic_arch}
  libatomic \
%endif
%ifarch %{itm_arch}
  libitm \
%endif
%ifarch %{asan_arch}
  libasan \
%endif
%ifarch %{tsan_arch}
  libtsan \
%endif
%ifarch %{lsan_arch}
  liblsan \
%endif
%ifarch %{ubsan_arch}
  libubsan \
%endif
%ifarch %{hwasan_arch}
  libhwasan \
%endif
%ifarch %{vtv_arch}
  libvtv \
%endif
    ; do
  for lib in `find %{buildroot}/%{versmainlibdir} -maxdepth 1 -name $libname.so.*`; do
    mv $lib %{buildroot}/%{mainlibdir}/
  done
  if test -L %{buildroot}/%{versmainlibdir}/$libname.so; then
    ln -sf %{mainlibdir}/`readlink %{buildroot}/%{versmainlibdir}/$libname.so | sed -e 's/\(.*\.so\.[^\.]*\).*/\1/'`  \
         %{buildroot}/%{versmainlibdir}/$libname.so
  fi
done
%if %{build_cp}
# And we want to move the shlib gdb pretty printers to a more sane
# place so ldconfig does not complain
mkdir -p %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdir}
mv %{buildroot}/%{mainlibdir}/libstdc++.so.*-gdb.py %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdir}/
sed -i -e '/^libdir/s/\/gcc\/%{GCCDIST}\/%{gcc_dir_version}//g' %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdir}/libstdc++.so.*-gdb.py
%endif

# Do something about libgcc_s
chmod a+x %{buildroot}/%{_lib}/libgcc_s.so.1
if test -L %{buildroot}/%{_lib}/libgcc_s.so; then
  rm -f %{buildroot}/%{_lib}/libgcc_s.so
  cp %{buildroot}/%{_lib}/libgcc_s.so.1 %{buildroot}/%{versmainlibdir}/libgcc_s.so
  strip -g %{buildroot}/%{versmainlibdir}/libgcc_s.so
else
  mv %{buildroot}/%{_lib}/libgcc_s.so %{buildroot}/%{versmainlibdir}/
fi
mv %{buildroot}/%{_lib}/libgcc_s.so.1 %{buildroot}/%{_slibdir}/libgcc_s.so.1
mv %{buildroot}/%{_lib}/libgcc_s_asneeded.so %{buildroot}/%{_slibdir}/libgcc_s_asneeded.so

%if %{build_ada}
mv %{buildroot}/%{libsubdir}/adalib/lib*-*.so %{buildroot}/%{_libdir}
ln -sf %{_libdir}/libgnarl%{binsuffix}.so %{buildroot}/%{libsubdir}/adalib/libgnarl.so
ln -sf %{_libdir}/libgnat%{binsuffix}.so %{buildroot}/%{libsubdir}/adalib/libgnat.so
chmod a+x %{buildroot}/%{_libdir}/libgna*-*.so
%endif

rm -f %{buildroot}/%{_prefix}/bin/c++%{binsuffix}

# Remove some crap from the .la files:
for l in `find %{buildroot} -name '*.la'`; do
  echo "changing $l"
  sed -e '/^dependency_libs/s| -L%{_builddir}/[^ ]*||g' \
      -e '/^dependency_libs/s| -L/usr/%{GCCDIST}/bin||g' \
      -e '/^dependency_libs/s|-lm \(-lm \)*|-lm |' \
      -e '/^dependency_libs/s|-L[^ ]* ||g' \
      < $l  > $l.new
  mv $l.new $l
done

# Remove files that we do not need to clean up filelist

# Preserve %{GCCDIST}-gcc%{binsuffix} binary for libgccjit as it is used as a driver
mv %{buildroot}/%{_prefix}/bin/%{GCCDIST}-gcc%{binsuffix} %{buildroot}
rm -f %{buildroot}/%{_prefix}/bin/%{GCCDIST}-*
mv %{buildroot}/%{GCCDIST}-gcc%{binsuffix} %{buildroot}/%{_prefix}/bin/

rm -rf %{buildroot}/%{libsubdir}/install-tools
rm -f %{buildroot}/%{libsubdir}/include-fixed/zutil.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/linux/a.out.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/linux/vt.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/asm-generic/socket.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/bits/mathdef.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/bits/unistd_ext.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/sys/ucontext.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/bits/statx.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/pthread.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/sys/rseq.h
echo > ../floatn-fixes.list
# Whether floatn.h is fixed depends on the glibc version and architecture.
# For now keep it if it's there but in the end we want to fix glibc itself
# everywhere.
if test -f %{buildroot}/%{libsubdir}/include-fixed/bits/floatn.h; then
  cat >> ../floatn-fixes.list <<EOF
%dir %{libsubdir}/include-fixed/bits
%{libsubdir}/include-fixed/bits/floatn.h
EOF
fi
if test -f %{buildroot}/%{libsubdir}/include-fixed/bits/floatn-common.h; then
  cat >> ../floatn-fixes.list <<EOF
%dir %{libsubdir}/include-fixed/bits
%{libsubdir}/include-fixed/bits/floatn-common.h
EOF
fi

%if !%{enable_plugins}
# no plugins
rm -rf %{buildroot}/%{libsubdir}/plugin
%endif
rm -f  %{buildroot}/%{_infodir}/dir

rm -f %{buildroot}/%{_mandir}/man7/fsf-funding.7
rm -f %{buildroot}/%{_mandir}/man7/gfdl.7
rm -f %{buildroot}/%{_mandir}/man7/gpl.7
rm -f %{buildroot}/%{_libdir}/libiberty.a
rm -f %{buildroot}/%{libsubdir}/liblto_plugin.a
rm -f %{buildroot}/%{libsubdir}/liblto_plugin.la
%if %{build_go}
# gccgo.info isn't properly versioned
rm %{buildroot}/%{_infodir}/gccgo.info*
rm -f %{buildroot}/%{libsubdir}/test2json
rm -f %{buildroot}/%{libsubdir}/vet
%endif

# For regular build, some info files do not get renamed properly.
# Do so here.
mv %{buildroot}/%{_infodir}/libgomp.info %{buildroot}/%{_infodir}/libgomp%{binsuffix}.info
%ifarch %itm_arch
mv %{buildroot}/%{_infodir}/libitm.info %{buildroot}/%{_infodir}/libitm%{binsuffix}.info
%endif
%if %{build_fortran}
%ifarch %quadmath_arch
mv %{buildroot}/%{_infodir}/libquadmath.info %{buildroot}/%{_infodir}/libquadmath%{binsuffix}.info
%endif
rm -f %{buildroot}/%{_infodir}/libquadmath.info
%endif
%if %{build_ada}
mv %{buildroot}/%{_infodir}/gnat-style.info %{buildroot}/%{_infodir}/gnat-style%{binsuffix}.info
mv %{buildroot}/%{_infodir}/gnat_rm.info %{buildroot}/%{_infodir}/gnat_rm%{binsuffix}.info
mv %{buildroot}/%{_infodir}/gnat_ugn.info %{buildroot}/%{_infodir}/gnat_ugn%{binsuffix}.info
%endif
%if %{build_m2}
mv %{buildroot}/%{_infodir}/m2.info %{buildroot}/%{_infodir}/m2%{binsuffix}.info
%endif

cd ..
%find_lang gcc%{binsuffix} --generate-subpackages
# Will output gcc16-langpack-be already exists error
%find_lang cpplib%{binsuffix}
%find_lang libstdc++

%files -f floatn-fixes.list
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%dir %{libsubdir}/include
%dir %{libsubdir}/include-fixed
%{_prefix}/bin/gcc%{binsuffix}
%{_prefix}/bin/%{GCCDIST}-gcc%{binsuffix}
%{_prefix}/bin/gcov%{binsuffix}
%{_prefix}/bin/gcov-dump%{binsuffix}
%{_prefix}/bin/gcov-tool%{binsuffix}
%{_prefix}/bin/gcc-ar%{binsuffix}
%{_prefix}/bin/gcc-nm%{binsuffix}
%{_prefix}/bin/gcc-ranlib%{binsuffix}
%{_prefix}/bin/lto-dump%{binsuffix}
%{libsubdir}/collect2
%{libsubdir}/lto1
%{libsubdir}/lto-wrapper
%{libsubdir}/liblto_plugin.so*
%{libsubdir}/include/limits.h
%{libsubdir}/include/syslimits.h
%{libsubdir}/include-fixed/README
%{libsubdir}/include/omp.h
%{libsubdir}/include/float.h
%{libsubdir}/include/iso646.h
%{libsubdir}/include/stdarg.h
%{libsubdir}/include/stdbool.h
%{libsubdir}/include/stdfix.h
%{libsubdir}/include/stddef.h
%{libsubdir}/include/unwind.h
%{libsubdir}/include/varargs.h
%{libsubdir}/include/stdint.h
%{libsubdir}/include/stdint-gcc.h
%{libsubdir}/include/stdckdint.h
%{libsubdir}/include/stdcountof.h
%{libsubdir}/include/stdnoreturn.h
%{libsubdir}/include/stdalign.h
%{libsubdir}/include/stdatomic.h
%{libsubdir}/include/openacc.h
%{libsubdir}/include/gcov.h
%{libsubdir}/include/acc_prof.h
%ifarch aarch64
%{libsubdir}/include/arm_neon.h
%{libsubdir}/include/arm_acle.h
%{libsubdir}/include/arm_fp16.h
%{libsubdir}/include/arm_bf16.h
%{libsubdir}/include/arm_sve.h
%{libsubdir}/include/arm_sme.h
%{libsubdir}/include/arm_neon_sve_bridge.h
%endif
%ifarch riscv64
%{libsubdir}/include/andes_vector.h
%{libsubdir}/include/riscv_vector.h
%{libsubdir}/include/riscv_bitmanip.h
%{libsubdir}/include/riscv_crypto.h
%{libsubdir}/include/riscv_th_vector.h
%{libsubdir}/include/sifive_vector.h
%endif
%ifarch x86_64
%{libsubdir}/include/cross-stdarg.h
%{libsubdir}/include/cpuid.h
%{libsubdir}/include/mm3dnow.h
%{libsubdir}/include/mmintrin.h
%{libsubdir}/include/ammintrin.h
%{libsubdir}/include/bmmintrin.h
%{libsubdir}/include/emmintrin.h
%{libsubdir}/include/immintrin.h
%{libsubdir}/include/avxintrin.h
%{libsubdir}/include/pmmintrin.h
%{libsubdir}/include/xmmintrin.h
%{libsubdir}/include/tmmintrin.h
%{libsubdir}/include/nmmintrin.h
%{libsubdir}/include/smmintrin.h
%{libsubdir}/include/wmmintrin.h
%{libsubdir}/include/x86intrin.h
%{libsubdir}/include/ia32intrin.h
%{libsubdir}/include/mm_malloc.h
%{libsubdir}/include/fma4intrin.h
%{libsubdir}/include/xopintrin.h
%{libsubdir}/include/lwpintrin.h
%{libsubdir}/include/popcntintrin.h
%{libsubdir}/include/bmiintrin.h
%{libsubdir}/include/tbmintrin.h
%{libsubdir}/include/avx2intrin.h
%{libsubdir}/include/bmi2intrin.h
%{libsubdir}/include/fmaintrin.h
%{libsubdir}/include/lzcntintrin.h
%{libsubdir}/include/f16cintrin.h
%{libsubdir}/include/adxintrin.h
%{libsubdir}/include/fxsrintrin.h
%{libsubdir}/include/prfchwintrin.h
%{libsubdir}/include/rdseedintrin.h
%{libsubdir}/include/rtmintrin.h
%{libsubdir}/include/xsaveintrin.h
%{libsubdir}/include/xsaveoptintrin.h
%{libsubdir}/include/xtestintrin.h
%{libsubdir}/include/avx512cdintrin.h
%{libsubdir}/include/amxavx512intrin.h
%{libsubdir}/include/amxfp8intrin.h
%{libsubdir}/include/amxmovrsintrin.h
%{libsubdir}/include/amxtf32intrin.h
%{libsubdir}/include/avx10_2bf16intrin.h
%{libsubdir}/include/avx10_2convertintrin.h
%{libsubdir}/include/avx10_2copyintrin.h
%{libsubdir}/include/avx10_2mediaintrin.h
%{libsubdir}/include/avx10_2minmaxintrin.h
%{libsubdir}/include/avx10_2satcvtintrin.h
%{libsubdir}/include/movrsintrin.h
%{libsubdir}/include/avx512bmmintrin.h
%{libsubdir}/include/avx512bmmvlintrin.h
%{libsubdir}/include/avx512fintrin.h
%{libsubdir}/include/shaintrin.h
%{libsubdir}/include/avx512bwintrin.h
%{libsubdir}/include/avx512dqintrin.h
%{libsubdir}/include/avx512vlbwintrin.h
%{libsubdir}/include/avx512vldqintrin.h
%{libsubdir}/include/avx512vlintrin.h
%{libsubdir}/include/avx512ifmaintrin.h
%{libsubdir}/include/avx512ifmavlintrin.h
%{libsubdir}/include/avx512vbmiintrin.h
%{libsubdir}/include/avx512vbmivlintrin.h
%{libsubdir}/include/avx512vpopcntdqintrin.h
%{libsubdir}/include/avx512vbmi2intrin.h
%{libsubdir}/include/avx512vbmi2vlintrin.h
%{libsubdir}/include/avx512vnniintrin.h
%{libsubdir}/include/avx512vnnivlintrin.h
%{libsubdir}/include/avx512bitalgintrin.h
%{libsubdir}/include/avx512vpopcntdqvlintrin.h
%{libsubdir}/include/avx512bf16intrin.h
%{libsubdir}/include/avx512bf16vlintrin.h
%{libsubdir}/include/avx512vp2intersectintrin.h
%{libsubdir}/include/avx512vp2intersectvlintrin.h
%{libsubdir}/include/vpclmulqdqintrin.h
%{libsubdir}/include/enqcmdintrin.h
%{libsubdir}/include/cet.h
%{libsubdir}/include/vaesintrin.h
%{libsubdir}/include/clwbintrin.h
%{libsubdir}/include/clflushoptintrin.h
%{libsubdir}/include/xsavecintrin.h
%{libsubdir}/include/xsavesintrin.h
%{libsubdir}/include/mwaitxintrin.h
%{libsubdir}/include/clzerointrin.h
%{libsubdir}/include/pkuintrin.h
%{libsubdir}/include/sgxintrin.h
%{libsubdir}/include/cetintrin.h
%{libsubdir}/include/gfniintrin.h
%{libsubdir}/include/pconfigintrin.h
%{libsubdir}/include/wbnoinvdintrin.h
%{libsubdir}/include/movdirintrin.h
%{libsubdir}/include/cldemoteintrin.h
%{libsubdir}/include/waitpkgintrin.h
%{libsubdir}/include/serializeintrin.h
%{libsubdir}/include/tsxldtrkintrin.h
%{libsubdir}/include/amxbf16intrin.h
%{libsubdir}/include/amxint8intrin.h
%{libsubdir}/include/amxtileintrin.h
%{libsubdir}/include/x86gprintrin.h
%{libsubdir}/include/hresetintrin.h
%{libsubdir}/include/uintrintrin.h
%{libsubdir}/include/keylockerintrin.h
%{libsubdir}/include/avxvnniintrin.h
%{libsubdir}/include/mwaitintrin.h
%{libsubdir}/include/avx512fp16intrin.h
%{libsubdir}/include/avx512fp16vlintrin.h
%{libsubdir}/include/avxifmaintrin.h
%{libsubdir}/include/avxvnniint8intrin.h
%{libsubdir}/include/avxneconvertintrin.h
%{libsubdir}/include/amxfp16intrin.h
%{libsubdir}/include/cmpccxaddintrin.h
%{libsubdir}/include/prfchiintrin.h
%{libsubdir}/include/raointintrin.h
%{libsubdir}/include/amxcomplexintrin.h
%{libsubdir}/include/avxvnniint16intrin.h
%{libsubdir}/include/sha512intrin.h
%{libsubdir}/include/sm3intrin.h
%{libsubdir}/include/sm4intrin.h
%{libsubdir}/include/avx512bitalgvlintrin.h
%{libsubdir}/include/usermsrintrin.h
%endif
%ifarch %{asan_arch}
%{libsubdir}/include/sanitizer
%endif
%if %{build_fortran}
%{libsubdir}/include/ISO_Fortran_binding.h
%endif
%{versmainlibdir}/*crt*.o
%{versmainlibdir}/libgcc*.a
%{versmainlibdir}/libgcov.a
%{versmainlibdir}/libgcc_s*.so
%{versmainlibdir}/libgomp.so
%{versmainlibdir}/libgomp.a
%{versmainlibdir}/libgomp.spec
%ifarch %{itm_arch}
%{versmainlibdir}/libitm.so
%{versmainlibdir}/libitm.a
%{versmainlibdir}/libitm.spec
%endif
%ifarch %{atomic_arch}
%{versmainlibdir}/libatomic.a
%{versmainlibdir}/libatomic.so
%{versmainlibdir}/libatomic_asneeded.a
%{versmainlibdir}/libatomic_asneeded.so
%endif
%ifarch %{asan_arch}
%{versmainlibdir}/libasan.so
%{versmainlibdir}/libasan.a
%{versmainlibdir}/libasan_preinit.o
%endif
%ifarch %{tsan_arch}
%if %{build_primary_64bit}
%{versmainlibdir}/libtsan.so
%{versmainlibdir}/libtsan.a
%{versmainlibdir}/libtsan_preinit.o
%endif
%endif
%ifarch %{lsan_arch}
%if %{build_primary_64bit}
%{versmainlibdir}/liblsan.so
%{versmainlibdir}/liblsan.a
%{versmainlibdir}/liblsan_preinit.o
%endif
%endif
%ifarch %{ubsan_arch}
%{versmainlibdir}/libubsan.so
%{versmainlibdir}/libubsan.a
%endif
%ifarch %{hwasan_arch}
%{versmainlibdir}/libhwasan.so
%{versmainlibdir}/libhwasan.a
%{versmainlibdir}/libhwasan_preinit.o
%endif
%ifarch %{asan_arch} %{ubsan_arch} %{tsan_arch} %{lsan_arch} %{hwasan_arch}
%{versmainlibdir}/libsanitizer.spec
%endif
%ifarch %{vtv_arch}
%{versmainlibdir}/libvtv.so
%{versmainlibdir}/libvtv.a
%endif
%doc %{_mandir}/man1/gcc%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov-dump%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov-tool%{binsuffix}.1.gz
%doc %{_mandir}/man1/lto-dump%{binsuffix}.1.gz

%if %{enable_plugins}
%files devel
%defattr(-,root,root)
%dir %{libsubdir}/plugin
%{libsubdir}/plugin
%if %{build_m2}
%exclude %{libsubdir}/plugin/m2rte.so
%endif
%endif

%if %{build_cp}
%files c++
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%{_prefix}/bin/g++%{binsuffix}
%doc %{_mandir}/man1/g++%{binsuffix}.1.gz
%{libsubdir}/cc1plus
%{libsubdir}/g++-mapper-server

%files -n libstdc++%{libsuffix} -f libstdc++.lang
%defattr(-,root,root)
%{mainlibdir}/libstdc++.so.*
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load%{_prefix}
%dir %{_datadir}/gdb/auto-load/%{mainlibdir}
%{_datadir}/gdb/auto-load/%{mainlibdir}/libstdc++.so.*-gdb.py
%{_datadir}/gcc%{binsuffix}

%files lib
%defattr(-,root,root)
%{_slibdir}/libgcc_s.so.1
%{_slibdir}/libgcc_s_asneeded.so

%files -n libstdc++-devel%{libdevel_suffix}
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%{versmainlibdir}/libstdc++.a
%{versmainlibdir}/libstdc++fs.a
%{versmainlibdir}/libstdc++exp.a
%{versmainlibdir}/libstdc++.so
%{versmainlibdir}/libsupc++.a
%{versmainlibdir}/libstdc++.modules.json
%{_prefix}/include/c++
%endif

%files -n libgomp%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libgomp.so.*

%ifarch %{asan_arch}
%files -n libasan%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libasan.so.*
%endif

%ifarch %{lsan_arch}
%if %{build_primary_64bit}
%files -n liblsan%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/liblsan.so.*
%endif
%endif

%ifarch %{tsan_arch}
%if %{build_primary_64bit}
%files -n libtsan%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libtsan.so.*
%endif
%endif

%ifarch %{hwasan_arch}
%files -n libhwasan%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libhwasan.so.*
%endif

%ifarch %{atomic_arch}
%files -n libatomic%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libatomic.so.*
%endif

%ifarch %{itm_arch}
%files -n libitm%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libitm.so.*
%endif

%ifarch %{ubsan_arch}
%files -n libubsan%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libubsan.so.*
%endif

%ifarch %{vtv_arch}
%files -n libvtv%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libvtv.so.*
%endif

%if %{build_fortran}
%files fortran
%defattr(-,root,root)
%dir %{libsubdir}/finclude
%{_prefix}/bin/gfortran%{binsuffix}
%{libsubdir}/f951
%{libsubdir}/finclude/*
%{versmainlibdir}/libgfortran.a
%{versmainlibdir}/libgfortran.so
%{versmainlibdir}/libgfortran.spec
%{versmainlibdir}/libcaf_single.a
%{versmainlibdir}/libcaf_shmem.a
%doc %{_mandir}/man1/gfortran%{binsuffix}.1.gz

%files -n libgfortran%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libgfortran.so.*
%endif

%ifarch %{quadmath_arch}
%files -n libquadmath%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libquadmath.so.*

%files -n libquadmath-devel%{libdevel_suffix}
%defattr(-,root,root)
%{libsubdir}/include/quadmath.h
%{libsubdir}/include/quadmath_weak.h
%{versmainlibdir}/libquadmath.a
%{versmainlibdir}/libquadmath.so
%endif

%files doc
%defattr(-,root,root)
%doc %{_infodir}/cpp%{binsuffix}.info*.gz
%doc %{_infodir}/cppinternals%{binsuffix}.info*.gz
%doc %{_infodir}/gcc%{binsuffix}.info*.gz
%doc %{_infodir}/gccint%{binsuffix}.info*.gz
%doc %{_infodir}/gccinstall%{binsuffix}.info*.gz
%doc %{_infodir}/libgomp%{binsuffix}.info*.gz
%ifarch %{itm_arch}
%doc %{_infodir}/libitm%{binsuffix}.info*.gz
%endif
%if %{build_fortran}
%doc %{_infodir}/gfortran%{binsuffix}.info*.gz
%ifarch %{quadmath_arch}
%doc %{_infodir}/libquadmath%{binsuffix}.info*.gz
%endif
%endif
%if %{build_ada}
%doc %{_infodir}/gnat-style%{binsuffix}.info*gz
%doc %{_infodir}/gnat_rm%{binsuffix}.info*gz
%doc %{_infodir}/gnat_ugn%{binsuffix}.info*gz
%endif
%if %{build_d}
%doc %{_infodir}/gdc%{binsuffix}.info*gz
%endif
%if %{build_m2}
%doc %{_infodir}/m2%{binsuffix}.info*gz
%endif

%files -n cpp16 -f cpplib%{binsuffix}.lang
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%{_prefix}/bin/cpp%{binsuffix}
%{libsubdir}/cc1
%doc %{_mandir}/man1/cpp%{binsuffix}.1.gz

%if %{build_objc}
%files objc
%defattr(-,root,root)
%{libsubdir}/cc1obj
%{libsubdir}/include/objc
%{versmainlibdir}/libobjc.a
%{versmainlibdir}/libobjc.so

%files -n libobjc%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libobjc.so.*
%endif

%if %{build_objcp}
%files obj-c++
%defattr(-,root,root)
%{libsubdir}/cc1objplus
%endif

%if %{build_ada}
%files ada
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%{_prefix}/bin/gnat*
%dir %{versmainlibdir}/adalib
%{mainlibdir}/libgnarl%{binsuffix}.so
%{mainlibdir}/libgnat%{binsuffix}.so
%{versmainlibdir}/adainclude
%{versmainlibdir}/adalib/*.ali
%{versmainlibdir}/adalib/*.a
%{versmainlibdir}/adalib/libgnarl.so
%{versmainlibdir}/adalib/libgnat.so
%{versmainlibdir}/gnat1
%{versmainlibdir}/ada_target_properties
%endif

%if %{build_go}
%files go
%defattr(-,root,root)
%{_prefix}/bin/gccgo%{binsuffix}
%{_prefix}/bin/go%{binsuffix}
%{_prefix}/bin/gofmt%{binsuffix}
%{libsubdir}/go1
%{versmainlibdir}/libgo.a
%{versmainlibdir}/libgo.so
%{versmainlibdir}/libgobegin.a
%{versmainlibdir}/libgolibbegin.a
%{versmainlibdir}/buildid
%{versmainlibdir}/cgo
%dir %{mainlibdir}/go
%dir %{mainlibdir}/go/%{gcc_dir_version}
%{mainlibdir}/go/%{gcc_dir_version}/%{GCCDIST}
%doc %{_mandir}/man1/gccgo%{binsuffix}.1.gz
%doc %{_mandir}/man1/go%{binsuffix}.1.gz
%doc %{_mandir}/man1/gofmt%{binsuffix}.1.gz

%files -n libgo%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libgo.so.*
%endif

%if %{build_d}
%files d
%defattr(-,root,root)
%{_prefix}/bin/gdc%{binsuffix}
%{libsubdir}/d21
%{versmainlibdir}/libgphobos.a
%{versmainlibdir}/libgphobos.so
%{versmainlibdir}/libgdruntime.a
%{versmainlibdir}/libgdruntime.so
%{versmainlibdir}/libgphobos.spec
%{versmainlibdir}/include/d
%doc %{_mandir}/man1/gdc%{binsuffix}.1.gz
%{mainlibdir}/libgphobos.so.*
%{mainlibdir}/libgdruntime.so.*
%endif

%if %{build_jit}
%files -n libgccjit%{libsuffix}
%defattr(-,root,root)
%{_prefix}/%{_lib}/libgccjit.so.*

%files -n libgccjit-devel%{libdevel_suffix}
%defattr(-,root,root)
%doc gcc/jit/docs/examples
%{_prefix}/%{_lib}/libgccjit.so
%{_prefix}/include/libgccjit.h
%{_prefix}/include/libgccjit++.h
%{_infodir}/libgccjit.info.gz
%endif

%if %{build_rust}
%files rust
%defattr(-,root,root)
%{_prefix}/bin/gccrs%{binsuffix}
%{libsubdir}/crab1
%endif

%if %{build_m2}
%files m2
%defattr(-,root,root)
%{_prefix}/bin/gm2%{binsuffix}
%{libsubdir}/cc1gm2
%if %{enable_plugins}
%{libsubdir}/plugin/m2rte.so
%endif
%{versmainlibdir}/m2
%{versmainlibdir}/libm2log.a
%{versmainlibdir}/libm2log.so
%{versmainlibdir}/libm2cor.a
%{versmainlibdir}/libm2cor.so
%{versmainlibdir}/libm2iso.a
%{versmainlibdir}/libm2iso.so
%{versmainlibdir}/libm2pim.a
%{versmainlibdir}/libm2pim.so
%{versmainlibdir}/libm2min.a
%{versmainlibdir}/libm2min.so
%doc %{_mandir}/man1/gm2%{binsuffix}.1.gz

%files -n libm2%{libsuffix}
%defattr(-,root,root)
%{mainlibdir}/libm2log.so.*
%{mainlibdir}/libm2cor.so.*
%{mainlibdir}/libm2iso.so.*
%{mainlibdir}/libm2pim.so.*
%{mainlibdir}/libm2min.so.*
%endif

%changelog
%autochangelog
