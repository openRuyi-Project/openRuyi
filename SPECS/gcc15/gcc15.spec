# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
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

# Ada currently fails to build on a few platforms, enable it only
# on those that work
%define ada_arch x86_64 aarch64 riscv64

%ifarch %ada_arch
%define build_ada 0
%else
%define build_ada 0
%endif

%define quadmath_arch x86_64
%define tsan_arch x86_64 aarch64 riscv64
%define asan_arch x86_64 aarch64 riscv64
%define hwasan_arch aarch64 x86_64
%define itm_arch x86_64 aarch64 riscv64
%define atomic_arch x86_64 aarch64 riscv64
%define lsan_arch x86_64 aarch64 riscv64
%define ubsan_arch x86_64 aarch64 riscv64
%if 0%{?build_libvtv:1}
%define vtv_arch x86_64
%endif

%define build_cp 1
%define build_fortran 1
%define build_objc 1
%define build_objcp 1
%define build_go 1
%ifarch x86_64 aarch64 riscv64
%define build_d 0
%else
%define build_d 0
%endif

%define build_m2 1

%if %{build_objcp}
%define build_cp 1
%define build_objc 1
%endif

# rust is still experimental
%define build_rust 0

# For optional compilers only build C, C++, Fortran, Ada and Go
%if 0%{?build_optional_compiler_languages:1}
%define build_objc 0
%define build_objcp 0
%define build_d 0
%define build_rust 0
%define build_m2 0
%endif

%define use_lto_bootstrap 0
%ifarch x86_64 aarch64
%define use_lto_bootstrap %{with bootstrap}
%endif

%define enable_plugins 0
%define build_jit 0

# Shared library SONAME versions
%define libgcc_s 1
%define libgomp_sover 1
%define libstdcxx_sover 6
%define libobjc_sover 4
%define libgfortran_sover 5
%define libquadmath_sover 0
%define libasan_sover 8
%define libtsan_sover 2
%define libhwasan_sover 0
%define libatomic_sover 1
%define libitm_sover 1
%define libubsan_sover 1
%define liblsan_sover 0
%define libvtv_sover 0
%define libgo_sover 24
%define libgphobos_sover 5
%define libgdruntime_sover 5
%define libgccjit_sover 0
%define libm2_sover 20

# Shared library package suffix
# This is used for the "non-standard" set of libraries, the standard
# being defined by %%product_libs_gcc_ver, the GCC version that should
# provide un-suffixed shared library packages following the shared-library
# policy.  Even suffixed variants should provide the shared-library policy
# mandated names and ensure they conflict with each other.
# Individual shared libraries can be directed to be built from individual
# gcc versions by defining %%product_libs_gcc_ver_libgcc_s1 for example,
# generally %%product_libs_gcc_ver_%%name%%sover, similarly.

%define itsme15 1
%define plv_ %{!?product_libs_gcc_ver:15}%{?product_libs_gcc_ver}
%define plv() %{expand:%%{!?itsme%{expand:%%{!?product_libs_gcc_ver_%{1}%{2}:%%{plv_}}%%{?product_libs_gcc_ver_%{1}%{2}}}:-gcc15}}

%define libgcc_s_suffix %{plv libgcc_s %{libgcc_s}}
%define libgomp_suffix %{plv libgomp %{libgomp_sover}}
%define libstdcxx_suffix %{plv libstdcxx %{libstdcxx_sover}}
%define libobjc_suffix %{plv libobjc %{libobjc_sover}}
%define libgfortran_suffix %{plv libgfortran %{libgfortran_sover}}
%define libquadmath_suffix %{plv libquadmath %{libquadmath_sover}}
%define libasan_suffix %{plv libasan %{libasan_sover}}
%define libtsan_suffix %{plv libtsan %{libtsan_sover}}
%define libhwasan_suffix %{plv libhwasan %{libhwasan_sover}}
%define libatomic_suffix %{plv libatomic %{libatomic_sover}}
%define libitm_suffix %{plv libitm %{libitm_sover}}
%define libubsan_suffix %{plv libubsan %{libubsan_sover}}
%define liblsan_suffix %{plv liblsan %{liblsan_sover}}
%define libvtv_suffix %{plv libvtv %{libvtv_sover}}
%define libgo_suffix %{plv libgo %{libgo_sover}}
%define libgphobos_suffix %{plv libgphobos %{libgphobos_sover}}
%define libgdruntime_suffix %{plv libgdruntime %{libgdruntime_sover}}
%define libgccjit_suffix %{plv libgccjit %{libgccjit_sover}}
%define libm2_suffix %{plv libm2 %{libm2_sover}}

# libFOO-devel package suffix
%define libdevel_suffix -gcc15
%global disable_32bit 1
%define biarch_targets x86_64

URL:            https://gcc.gnu.org/
Version:        15.2.0
Release:        %autorelease
%define gcc_dir_version %(echo %version |  sed 's/+.*//' | cut -d '.' -f 1)
%define gcc_snapshot_revision %(echo %version | sed 's/[3-9]\.[0-9]\.[0-6]//' | sed 's/+/-/')
%define binsuffix -15

Name:           gcc15
BuildRequires:  xz
BuildRequires:  libzstd-devel
# With generated files in src we could drop the following
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext-devel
BuildRequires:  texinfo
# until here, but at least renaming and patching info files breaks this
BuildRequires:  gcc-c++
BuildRequires:  mpc-devel
BuildRequires:  mpfr-devel
BuildRequires:  perl
BuildRequires:  zlib-devel
# for SDT markers in the C++ unwinder and gdb breakpoints on exceptions
BuildRequires:  (systemtap-headers or systemtap-sdt-devel)
BuildRequires:  isl-devel
%define hostsuffix %{nil}
%if %{build_ada}
%if 0%{?gcc_version:%{gcc_version}} > 14
%define hostsuffix %{binsuffix}
BuildRequires:  gcc15-ada
BuildRequires:  gcc15-c++
%else
%define hostsuffix %{nil}
BuildRequires:  gcc-ada
%endif
%endif
%if %{build_d}
BuildRequires:  gcc-d
%endif
%if 0%{?run_tests:1}
BuildRequires:  dejagnu
BuildRequires:  expect
BuildRequires:  gdb
BuildRequires:  timezone
%if %{build_go}
BuildRequires:  netcfg
BuildRequires:  procps
%endif
%endif
#!BuildIgnore: gcc-PIE

%define separate_bi32 0
%define separate_bi64 0
%if 0%{!?disable_32bit:1}
%ifarch x86_64
%define separate_bi32 1
%endif
%define disable_multilib_arch %{nil}
%else
%define disable_multilib_arch x86_64
%endif

# Define two macros to trigger -32bit or -64bit package variants
%define separate_biarch 0
%if %{separate_bi32}
%define separate_biarch 1
%define separate_biarch_suffix -32bit
%endif
%if %{separate_bi64}
%define separate_biarch 1
%define separate_biarch_suffix -64bit
%endif

%ifarch aarch64 x86_64 riscv64
# 64-bit is primary build target
%define build_primary_64bit 1
%else
%define build_primary_64bit 0
%endif

%if !0%{?building_testsuite:1}
Requires:       binutils
Requires:       cpp15 = %{version}-%{release}
Requires:       glibc-devel
Requires:       libgcc_s%{libgcc_s} >= %{version}-%{release}
Requires:       libgomp%{libgomp_sover} >= %{version}-%{release}
%ifarch %asan_arch
Requires:       libasan%{libasan_sover} >= %{version}-%{release}
%endif
%ifarch %tsan_arch
%if %{build_primary_64bit}
Requires:       libtsan%{libtsan_sover} >= %{version}-%{release}
%endif
%endif
%ifarch %hwasan_arch
Requires:       libhwasan%{libhwasan_sover} >= %{version}-%{release}
%endif
%ifarch %atomic_arch
Requires:       libatomic%{libatomic_sover} >= %{version}-%{release}
%endif
%ifarch %itm_arch
Requires:       libitm%{libitm_sover} >= %{version}-%{release}
%endif
%ifarch %lsan_arch
%if %{build_primary_64bit}
Requires:       liblsan%{liblsan_sover} >= %{version}-%{release}
%endif
%endif
%ifarch %ubsan_arch
Requires:       libubsan%{libubsan_sover} >= %{version}-%{release}
%endif
%ifarch %vtv_arch
Requires:       libvtv%{libvtv_sover} >= %{version}-%{release}
%endif
Suggests:       gcc15-info gcc15-locale
%endif

#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
Patch2:         gcc-add-defaultsspec.diff
Patch60:        gcc44-textdomain.patch
Patch61:        gcc44-rename-info-files.patch

# RVA23 Enablement Patches
# Rebased against 15.2, 20250910
Patch1001:      0001-PATCH-RISC-V-Imply-C-from-Zca-whenever-possible-PR11.patch
Patch1002:      0002-RISC-V-Fix-missing-implied-Zicsr-from-Zve32x.patch
Patch1003:      0003-RISC-V-Add-new-option-param-gpr2vr-cost-for-rvv-insn.patch
Patch1004:      0004-PATCH-RISC-V-Recognized-svadu-and-svade-extension.patch
Patch1005:      0005-PATCH-RISC-V-Minimal-support-for-sdtrig-and-ssstrict.patch
Patch1006:      0006-PATCH-RISC-V-Minimal-support-for-zama16b-extension.patch
Patch1007:      0007-RISC-V-Support-RISC-V-Profiles-20-22.patch
Patch1008:      0008-RISC-V-Support-RISC-V-Profiles-23.patch
Patch1009:      0009-RISC-V-Support-for-zilsd-and-zclsd-extensions.patch
Patch1010:      0010-RISC-V-Minimal-support-for-ssnpm-smnpm-and-smmpm-ext.patch
Patch1011:      0011-RISC-V-Introduce-riscv-ext-.def-to-define-extensions.patch
Patch1012:      0012-RISC-V-Use-riscv-ext.def-to-generate-target-options-.patch
Patch1013:      0013-RISC-V-Generate-extension-table-in-documentation-fro.patch
Patch1014:      0014-RISC-V-Adjust-riscv_can_inline_p.patch
Patch1015:      0015-RISC-V-Introduce-riscv_ext_info_t-to-hold-extension-.patch
Patch1016:      0016-RISC-V-Drop-riscv_implied_info-and-riscv_combine_inf.patch
Patch1017:      0017-RISC-V-Drop-riscv_ext_version_table-in-favor-of-risc.patch
Patch1018:      0018-RISC-V-Drop-riscv_ext_flag_table-in-favor-of-riscv_e.patch
Patch1019:      0019-RISC-V-Add-augmented-hypervisor-series-extensions.patch
Patch1020:      0020-RISC-V-Support-CPUs-in-march.patch
Patch1021:      0021-RISC-V-Add-minimal-support-of-double-trap-extension-.patch
Patch1022:      0022-PATCH-RISC-V-Add-smcntrpmf-extension.patch
Patch1023:      0023-RISC-V-Add-Shlcofideleg-extension.patch
Patch1024:      0024-PATCH-v2-RISC-V-Add-svbare-extension.patch
Patch1025:      0025-PATCH-RISC-V-Imply-zicsr-for-svade-and-svadu-extensi.patch
Patch1026:      0026-RISC-V-Update-extension-defination.patch
Patch1027:      0027-RISC-V-Support-Sm-scsrind-extensions.patch
Patch1028:      0028-RISC-V-Support-Smrnmi-extension.patch
Patch1029:      0029-RISC-V-Support-Ssccptr-extension.patch
Patch1030:      0030-RISC-V-Support-Sscounterenw-extension.patch
Patch1031:      0031-RISC-V-Support-Sstvala-extension.patch
Patch1032:      0032-RISC-V-Support-Sstvecd-extension.patch
Patch1033:      0033-RISC-V-Support-Ssu64xl-extension.patch
Patch1034:      0034-RISC-V-Update-Profiles-string-in-RV23.patch
Patch1035:      0035-RISC-V-Add-Profiles-RVA-B23S64-support.patch
Patch1036:      0036-RISC-V-check-if-we-can-vec_extract.patch

License:        GPL-3.0-or-later
Summary:        The GNU C Compiler and Support Files

%description
Core package for the GNU Compiler Collection, including the C language
frontend.

Language frontends other than C are split to different sub-packages,
namely gcc-ada, gcc-c++, gcc-fortran, gcc-obj, gcc-obj-c++, gcc-go,
gcc-rust and gcc-m2.

%package -n gcc15-32bit
Summary:        The GNU C Compiler 32bit support
Requires:       gcc15 = %{version}-%{release}
Requires:       libgcc_s%{libgcc_s}-32bit >= %{version}-%{release}
Requires:       libgomp%{libgomp_sover}-32bit >= %{version}-%{release}
%ifarch %asan_arch
Requires:       libasan%{libasan_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %atomic_arch
Requires:       libatomic%{libatomic_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %itm_arch
Requires:       libitm%{libitm_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %ubsan_arch
Requires:       libubsan%{libubsan_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %vtv_arch
Requires:       libvtv%{libvtv_sover}-32bit >= %{version}-%{release}
%endif
Requires:       glibc-devel-32bit glibc-32bit

%description -n gcc15-32bit
This package contains 32bit support for the GNU Compiler Collection.

%package -n gcc15-64bit
Summary:        The GNU C Compiler 64bit support
Requires:       gcc15 = %{version}-%{release}
Requires:       libgcc_s%{libgcc_s}-64bit >= %{version}-%{release}
Requires:       libgomp%{libgomp_sover}-64bit >= %{version}-%{release}
%ifarch %asan_arch
Requires:       libasan%{libasan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %tsan_arch
Requires:       libtsan%{libtsan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %hwasan_arch
Requires:       libhwasan%{libhwasan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %atomic_arch
Requires:       libatomic%{libatomic_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %itm_arch
Requires:       libitm%{libitm_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %lsan_arch
Requires:       liblsan%{liblsan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %ubsan_arch
Requires:       libubsan%{libubsan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %vtv_arch
Requires:       libvtv%{libvtv_sover}-64bit >= %{version}-%{release}
%endif
Requires:       glibc-devel-64bit

%description -n gcc15-64bit
This package contains 64bit support for the GNU Compiler Collection.

%package devel
Summary:        GCC plugins development enviroment
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}
Requires:       gmp-devel
Requires:       mpc-devel

%description devel
Files required for developing and compiling GCC plugins.

%package locale
Summary:        Locale Data for the GNU Compiler Collection
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}

%description locale
Locale data for the GNU Compiler Collection (GCC) to give error message
in the current locale.

%package PIE
Summary:        A default configuration to build all binaries in PIE mode
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}

%description PIE
This package contains a configuration file (spec) that changes the
compilers default setting to build all ELF binaries in the Position
Independend Executable (PIE) variant. This enables better address
space randomization (ASLR).

%package c++
Summary:        The GNU C++ Compiler
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}
Requires:       gcc15-c++ = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix} = %{version}-%{release}

%description c++
This package contains the GNU compiler for C++.

%package c++-32bit
Summary:        The GNU C++ Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-32bit = %{version}-%{release}
Requires:       gcc15-c++ = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-32bit = %{version}-%{release}

%description c++-32bit
This package contains the GNU compiler for C++.

%package c++-64bit
Summary:        The GNU C++ Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-64bit = %{version}-%{release}
Requires:       gcc15-c++ = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-64bit = %{version}-%{release}

%description c++-64bit
This package contains the GNU compiler for C++.

%package -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}
Summary:        Include Files and Libraries mandatory for Development
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       glibc-devel
Requires:       libstdc++%{libstdcxx_sover} >= %{version}-%{release}

%description -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}
This package contains all the headers and libraries of the standard C++
library. It is needed for compiling C++ code.

%package -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-32bit
Summary:        Include Files and Libraries mandatory for Development
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       glibc-devel-32bit glibc-32bit
Requires:       libstdc++%{libstdcxx_sover}-32bit >= %{version}-%{release}

%description -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-32bit
This package contains all the headers and libraries of the standard C++
library. It is needed for compiling C++ code.

%package -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-64bit
Summary:        Include Files and Libraries mandatory for Development
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       glibc-devel-64bit
Requires:       libstdc++%{libstdcxx_sover}-64bit >= %{version}-%{release}

%description -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-64bit
This package contains all the headers and libraries of the standard C++
library. It is needed for compiling C++ code.

%package -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}
Summary:        GDB pretty printers for the C++ standard library
License:        GPL-3.0-or-later
# The -pp packages are tied to a specific shared library
Requires:       libstdc++%{libstdcxx_sover} = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix} = %{version}-%{release}
Provides:       libstdc++%{libstdcxx_sover}-pp = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libstdc++%{libstdcxx_sover}-pp
# packageand() does not work with versioned specifications so the fallback
# is a Requires from libstdc++-devel to preserve previous behavior.
Supplements:    (gdb and libstdc++%{libstdcxx_sover} = %{version}-%{release})

%description -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}
This package contains pretty printers for the C++ standard library usable
from GDB.

%package -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}-32bit
Summary:        GDB pretty printers for the C++ standard library
License:        GPL-3.0-or-later
# The -pp packages are tied to a specific shared library
Requires:       libstdc++%{libstdcxx_sover}-32bit = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix} = %{version}-%{release}
Provides:       libstdc++%{libstdcxx_sover}-pp-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libstdc++%{libstdcxx_sover}-pp-32bit
# packageand() does not work with versioned specifications so the fallback
# is a Requires from libstdc++-devel to preserve previous behavior.
Supplements:    (gdb and libstdc++%{libstdcxx_sover}-32bit = %{version}-%{release})

%description -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}-32bit
This package contains pretty printers for the C++ standard library usable
from GDB.

%package -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}-64bit
Summary:        GDB pretty printers for the C++ standard library
License:        GPL-3.0-or-later
# The -pp packages are tied to a specific shared library
Requires:       libstdc++%{libstdcxx_sover}-64bit = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix} = %{version}-%{release}
Provides:       libstdc++%{libstdcxx_sover}-pp-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libstdc++%{libstdcxx_sover}-pp-64bit
# packageand() does not work with versioned specifications so the fallback
# is a Requires from libstdc++-devel to preserve previous behavior.
Supplements:    (gdb and libstdc++%{libstdcxx_sover}-64bit = %{version}-%{release})

%description -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}-64bit
This package contains pretty printers for the C++ standard library usable
from GDB.

%package -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}
Summary:        C compiler runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libgcc_s%{libgcc_s} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgcc_s%{libgcc_s}

%description -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}
Libgcc is needed for dynamically linked C programs.

%package -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-32bit
Summary:        C compiler runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libgcc_s%{libgcc_s}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgcc_s%{libgcc_s}-32bit

%description -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-32bit
Libgcc is needed for dynamically linked C programs.

%package -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-64bit
Summary:        C compiler runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libgcc_s%{libgcc_s}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgcc_s%{libgcc_s}-64bit

%description -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-64bit
Libgcc is needed for dynamically linked C programs.

%package -n libgomp%{libgomp_sover}%{libgomp_suffix}
Summary:        The GNU compiler collection OpenMP runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libgomp%{libgomp_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgomp%{libgomp_sover}

%description -n libgomp%{libgomp_sover}%{libgomp_suffix}
This is the OpenMP runtime library needed by OpenMP enabled programs
that were built with the -fopenmp compiler option and by programs that
were auto-parallelized via the -ftree-parallelize-loops compiler
option.

%package -n libgomp%{libgomp_sover}%{libgomp_suffix}-32bit
Summary:        The GNU compiler collection OpenMP runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libgomp%{libgomp_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgomp%{libgomp_sover}-32bit

%description -n libgomp%{libgomp_sover}%{libgomp_suffix}-32bit
This is the OpenMP runtime library needed by OpenMP enabled programs
that were built with the -fopenmp compiler option and by programs that
were auto-parallelized via the -ftree-parallelize-loops compiler
option.


%package -n libgomp%{libgomp_sover}%{libgomp_suffix}-64bit
Summary:        The GNU compiler collection OpenMP runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libgomp%{libgomp_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgomp%{libgomp_sover}-64bit

%description -n libgomp%{libgomp_sover}%{libgomp_suffix}-64bit
This is the OpenMP runtime library needed by OpenMP enabled programs
that were built with the -fopenmp compiler option and by programs that
were auto-parallelized via the -ftree-parallelize-loops compiler
option.

%package -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}
Summary:        The standard C++ shared library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Suggests:       libstdc++%{libstdcxx_sover}-locale
Provides:       libstdc++%{libstdcxx_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libstdc++%{libstdcxx_sover}
# The std::chrono timezone database is provided by timezone
# (/usr/share/zoneinfo/tzdata.zi), without that the tzdb is empty and
# will only provide UTC.  We don't want a Requires here though, instead
# the overall product needs to decide what to provide,

%description -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}
The standard C++ library, needed for dynamically linked C++ programs.


%package -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-32bit
Summary:        The standard C++ shared library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Suggests:       libstdc++%{libstdcxx_sover}-locale
Provides:       libstdc++%{libstdcxx_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libstdc++%{libstdcxx_sover}-32bit
# The std::chrono timezone database is provided by timezone
# (/usr/share/zoneinfo/tzdata.zi), without that the tzdb is empty and
# will only provide UTC.  We don't want a Requires here though, instead
# the overall product needs to decide what to provide,

%description -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-32bit
The standard C++ library, needed for dynamically linked C++ programs.


%package -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-64bit
Summary:        The standard C++ shared library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Suggests:       libstdc++%{libstdcxx_sover}-locale
Provides:       libstdc++%{libstdcxx_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libstdc++%{libstdcxx_sover}-64bit
# The std::chrono timezone database is provided by timezone
# (/usr/share/zoneinfo/tzdata.zi), without that the tzdb is empty and
# will only provide UTC.  We don't want a Requires here though, instead
# the overall product needs to decide what to provide,

%description -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-64bit
The standard C++ library, needed for dynamically linked C++ programs.

%package -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-locale
Summary:        Standard C++ Library Locales
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libstdc++%{libstdcxx_sover}-locale = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libstdc++%{libstdcxx_sover}-locale

%description -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-locale
The standard C++ library locale data.

%package info
Summary:        Documentation for the GNU compiler collection
License:        GFDL-1.2-only
PreReq:         texinfo
BuildArch:      noarch

%description info
GNU info-pages for the GNU compiler collection covering both user-level
and internals documentation.

%package objc
Summary:        GNU Objective C Compiler
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}
Requires:       gcc15-objc = %{version}-%{release}
Requires:       libobjc%{libobjc_sover} >= %{version}-%{release}

%description objc
This package contains the GNU Objective C compiler. Objective C is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package objc-32bit
Summary:        GNU Objective C Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-32bit = %{version}-%{release}
Requires:       gcc15-objc = %{version}-%{release}
Requires:       libobjc%{libobjc_sover}-32bit >= %{version}-%{release}

%description objc-32bit
This package contains the GNU Objective C compiler. Objective C is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package objc-64bit
Summary:        GNU Objective C Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-64bit = %{version}-%{release}
Requires:       gcc15-objc = %{version}-%{release}
Requires:       libobjc%{libobjc_sover}-64bit >= %{version}-%{release}

%description objc-64bit
This package contains the GNU Objective C compiler. Objective C is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package -n libobjc%{libobjc_sover}%{libobjc_suffix}
Summary:        Library for the GNU Objective C Compiler
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libobjc%{libobjc_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libobjc%{libobjc_sover}

%description -n libobjc%{libobjc_sover}%{libobjc_suffix}
The library for the GNU Objective C compiler.

%package -n libobjc%{libobjc_sover}%{libobjc_suffix}-32bit
Summary:        Library for the GNU Objective C Compiler
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libobjc%{libobjc_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libobjc%{libobjc_sover}-32bit

%description -n libobjc%{libobjc_sover}%{libobjc_suffix}-32bit
The library for the GNU Objective C compiler.

%package -n libobjc%{libobjc_sover}%{libobjc_suffix}-64bit
Summary:        Library for the GNU Objective C Compiler
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libobjc%{libobjc_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libobjc%{libobjc_sover}-64bit

%description -n libobjc%{libobjc_sover}%{libobjc_suffix}-64bit
The library for the GNU Objective C compiler.

%package obj-c++
Summary:        GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-c++ = %{version}-%{release}
Requires:       gcc15-obj-c++ = %{version}-%{release}
Requires:       gcc15-objc = %{version}-%{release}

%description obj-c++
This package contains the GNU Objective C++ compiler. Objective C++ is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package obj-c++-32bit
Summary:        GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-c++-32bit = %{version}-%{release}
Requires:       gcc15-obj-c++ = %{version}-%{release}
Requires:       gcc15-objc-32bit = %{version}-%{release}

%description obj-c++-32bit
This package contains the GNU Objective C++ compiler. Objective C++ is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package obj-c++-64bit
Summary:        GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-c++-64bit = %{version}-%{release}
Requires:       gcc15-obj-c++ = %{version}-%{release}
Requires:       gcc15-objc-64bit = %{version}-%{release}

%description obj-c++-64bit
This package contains the GNU Objective C++ compiler. Objective C++ is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package -n cpp15
Summary:        The GCC Preprocessor
License:        GPL-3.0-or-later

%description -n cpp15
This Package contains just the preprocessor that is used by the X11
packages.

%package ada
Summary:        GNU Ada Compiler Based on GCC (GNAT)
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}
Requires:       gcc15-ada = %{version}-%{release}
Requires:       libada15 = %{version}-%{release}

%description ada
This package contains an Ada compiler and associated development
tools based on the GNU GCC technology.

%package ada-32bit
Summary:        GNU Ada Compiler Based on GCC (GNAT)
License:        GPL-3.0-or-later
Requires:       gcc15-32bit = %{version}-%{release}
Requires:       gcc15-ada = %{version}-%{release}
Requires:       libada15-32bit = %{version}-%{release}

%description ada-32bit
This package contains an Ada compiler and associated development
tools based on the GNU GCC technology.

%package ada-64bit
Summary:        GNU Ada Compiler Based on GCC (GNAT)
License:        GPL-3.0-or-later
Requires:       gcc15-64bit = %{version}-%{release}
Requires:       gcc15-ada = %{version}-%{release}
Requires:       libada15-64bit = %{version}-%{release}

%description ada-64bit
This package contains an Ada compiler and associated development
tools based on the GNU GCC technology.

%package -n libada15
Summary:        GNU Ada Runtime Libraries
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libgnarl-15 = %{version}-%{release}
Conflicts:      libgnarl-15
Provides:       libgnat-15 = %{version}-%{release}
Conflicts:      libgnat-15

%description -n libada15
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries. It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the Posix
1003.5 Binding (Florist).

%package -n libada15-32bit
Summary:        GNU Ada Runtime Libraries
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libgnarl-15-32bit = %{version}-%{release}
Conflicts:      libgnarl-15-32bit
Provides:       libgnat-15-32bit = %{version}-%{release}
Conflicts:      libgnat-15-32bit

%description -n libada15-32bit
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries. It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the Posix
1003.5 Binding (Florist).

%package -n libada15-64bit
Summary:        GNU Ada Runtime Libraries
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libgnarl-15-64bit = %{version}-%{release}
Conflicts:      libgnarl-15-64bit
Provides:       libgnat-15-64bit = %{version}-%{release}
Conflicts:      libgnat-15-64bit

%description -n libada15-64bit
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries. It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the Posix
1003.5 Binding (Florist).

%package fortran
Summary:        The GNU Fortran Compiler and Support Files
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}
Requires:       gcc15-fortran = %{version}-%{release}
Requires:       libgfortran%{libgfortran_sover} >= %{version}-%{release}
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover}-devel%{libdevel_suffix} = %{version}-%{release}
%endif

%description fortran
This is the Fortran compiler of the GNU Compiler Collection (GCC).

%package fortran-32bit
Summary:        The GNU Fortran Compiler and Support Files
License:        GPL-3.0-or-later
Requires:       gcc15-32bit = %{version}-%{release}
Requires:       gcc15-fortran = %{version}-%{release}
Requires:       libgfortran%{libgfortran_sover}-32bit >= %{version}-%{release}
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover}-devel%{libdevel_suffix}-32bit = %{version}-%{release}
%endif

%description fortran-32bit
This is the Fortran compiler of the GNU Compiler Collection (GCC).

%package fortran-64bit
Summary:        The GNU Fortran Compiler and Support Files
License:        GPL-3.0-or-later
Requires:       gcc15-64bit = %{version}-%{release}
Requires:       gcc15-fortran = %{version}-%{release}
Requires:       libgfortran%{libgfortran_sover}-64bit >= %{version}-%{release}
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover}-devel%{libdevel_suffix}-64bit = %{version}-%{release}
%endif

%description fortran-64bit
This is the Fortran compiler of the GNU Compiler Collection (GCC).

%package -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}
Summary:        The GNU Fortran Compiler Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover} >= %{version}-%{release}
%endif
Provides:       libgfortran%{libgfortran_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgfortran%{libgfortran_sover}

%description -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC).

%package -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-32bit
Summary:        The GNU Fortran Compiler Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover}-32bit >= %{version}-%{release}
%endif
Provides:       libgfortran%{libgfortran_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgfortran%{libgfortran_sover}-32bit

%description -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-32bit
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC).

%package -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-64bit
Summary:        The GNU Fortran Compiler Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover}-64bit >= %{version}-%{release}
%endif
Provides:       libgfortran%{libgfortran_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgfortran%{libgfortran_sover}-64bit

%description -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-64bit
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC).

%package -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}
Summary:        The GNU Fortran Compiler Quadmath Runtime Library
License:        LGPL-2.1-only
Provides:       libquadmath%{libquadmath_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libquadmath%{libquadmath_sover}

%description -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC) and quadruple precision floating point
operations.

%package -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-32bit
Summary:        The GNU Fortran Compiler Quadmath Runtime Library
License:        LGPL-2.1-only
Provides:       libquadmath%{libquadmath_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libquadmath%{libquadmath_sover}-32bit

%description -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-32bit
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC) and quadruple precision floating point
operations.

%package -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-64bit
Summary:        The GNU Fortran Compiler Quadmath Runtime Library
License:        LGPL-2.1-only
Provides:       libquadmath%{libquadmath_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libquadmath%{libquadmath_sover}-64bit

%description -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-64bit
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC) and quadruple precision floating point
operations.

%package -n libquadmath%{libquadmath_sover}-devel%{libdevel_suffix}
Summary:        The GNU Fortran Compiler Quadmath Runtime Library Development Files
License:        LGPL-2.1-only
Requires:       libquadmath%{libquadmath_sover} >= %{version}-%{release}

%description -n libquadmath%{libquadmath_sover}-devel%{libdevel_suffix}
The libquadmatah runtime library development files.

%package -n libquadmath%{libquadmath_sover}-devel%{libdevel_suffix}-32bit
Summary:        The GNU Fortran Compiler Quadmath Runtime Library Development Files
License:        LGPL-2.1-only
Requires:       libquadmath%{libquadmath_sover}-32bit >= %{version}-%{release}

%description -n libquadmath%{libquadmath_sover}-devel%{libdevel_suffix}-32bit
The libquadmatah runtime library development files.

%package -n libquadmath%{libquadmath_sover}-devel%{libdevel_suffix}-64bit
Summary:        The GNU Fortran Compiler Quadmath Runtime Library Development Files
License:        LGPL-2.1-only
Requires:       libquadmath%{libquadmath_sover}-64bit >= %{version}-%{release}

%description -n libquadmath%{libquadmath_sover}-devel%{libdevel_suffix}-64bit
The libquadmatah runtime library development files.

%package -n libitm%{libitm_sover}%{libitm_suffix}
Summary:        The GNU Compiler Transactional Memory Runtime Library
License:        MIT
Provides:       libitm%{libitm_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libitm%{libitm_sover}

%description -n libitm%{libitm_sover}%{libitm_suffix}
The runtime library needed to run programs compiled with the
-fgnu-tm option of the GNU Compiler Collection (GCC).

%package -n libitm%{libitm_sover}%{libitm_suffix}-32bit
Summary:        The GNU Compiler Transactional Memory Runtime Library
License:        MIT
Provides:       libitm%{libitm_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libitm%{libitm_sover}-32bit

%description -n libitm%{libitm_sover}%{libitm_suffix}-32bit
The runtime library needed to run programs compiled with the
-fgnu-tm option of the GNU Compiler Collection (GCC).

%package -n libitm%{libitm_sover}%{libitm_suffix}-64bit
Summary:        The GNU Compiler Transactional Memory Runtime Library
License:        MIT
Provides:       libitm%{libitm_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libitm%{libitm_sover}-64bit

%description -n libitm%{libitm_sover}%{libitm_suffix}-64bit
The runtime library needed to run programs compiled with the
-fgnu-tm option of the GNU Compiler Collection (GCC).

%package -n libasan%{libasan_sover}%{libasan_suffix}
Summary:        The GNU Compiler Address Sanitizer Runtime Library
License:        MIT
Provides:       libasan%{libasan_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libasan%{libasan_sover}

%description -n libasan%{libasan_sover}%{libasan_suffix}
The runtime library needed to run programs compiled with the
-fsanitize=address option of the GNU Compiler Collection (GCC).

%package -n libasan%{libasan_sover}%{libasan_suffix}-32bit
Summary:        The GNU Compiler Address Sanitizer Runtime Library
License:        MIT
Provides:       libasan%{libasan_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libasan%{libasan_sover}-32bit

%description -n libasan%{libasan_sover}%{libasan_suffix}-32bit
The runtime library needed to run programs compiled with the
-fsanitize=address option of the GNU Compiler Collection (GCC).

%package -n libasan%{libasan_sover}%{libasan_suffix}-64bit
Summary:        The GNU Compiler Address Sanitizer Runtime Library
License:        MIT
Provides:       libasan%{libasan_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libasan%{libasan_sover}-64bit

%description -n libasan%{libasan_sover}%{libasan_suffix}-64bit
The runtime library needed to run programs compiled with the
-fsanitize=address option of the GNU Compiler Collection (GCC).

%package -n libtsan%{libtsan_sover}%{libtsan_suffix}
Summary:        The GNU Compiler Thread Sanitizer Runtime Library
License:        MIT
Provides:       libtsan%{libtsan_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libtsan%{libtsan_sover}

%description -n libtsan%{libtsan_sover}%{libtsan_suffix}
The runtime library needed to run programs compiled with the
-fsanitize=thread option of the GNU Compiler Collection (GCC).

%package -n libtsan%{libtsan_sover}%{libtsan_suffix}-32bit
Summary:        The GNU Compiler Thread Sanitizer Runtime Library
License:        MIT
Provides:       libtsan%{libtsan_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libtsan%{libtsan_sover}-32bit

%description -n libtsan%{libtsan_sover}%{libtsan_suffix}-32bit
The runtime library needed to run programs compiled with the
-fsanitize=thread option of the GNU Compiler Collection (GCC).

%package -n libtsan%{libtsan_sover}%{libtsan_suffix}-64bit
Summary:        The GNU Compiler Thread Sanitizer Runtime Library
License:        MIT
Provides:       libtsan%{libtsan_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libtsan%{libtsan_sover}-64bit

%description -n libtsan%{libtsan_sover}%{libtsan_suffix}-64bit
The runtime library needed to run programs compiled with the
-fsanitize=thread option of the GNU Compiler Collection (GCC).

%package -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}
Summary:        The GNU Compiler Hardware-assisted Address Sanitizer Runtime Library
License:        MIT
Provides:       libhwasan%{libhwasan_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libhwasan%{libhwasan_sover}

%description -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}
The runtime library needed to run programs compiled with the
-fsanitize=hwaddress option of the GNU Compiler Collection (GCC).

%package -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-32bit
Summary:        The GNU Compiler Hardware-assisted Address Sanitizer Runtime Library
License:        MIT
Provides:       libhwasan%{libhwasan_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libhwasan%{libhwasan_sover}-32bit

%description -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-32bit
The runtime library needed to run programs compiled with the
-fsanitize=hwaddress option of the GNU Compiler Collection (GCC).

%package -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-64bit
Summary:        The GNU Compiler Hardware-assisted Address Sanitizer Runtime Library
License:        MIT
Provides:       libhwasan%{libhwasan_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libhwasan%{libhwasan_sover}-64bit

%description -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-64bit
The runtime library needed to run programs compiled with the
-fsanitize=hwaddress option of the GNU Compiler Collection (GCC).

%package -n libatomic%{libatomic_sover}%{libatomic_suffix}
Summary:        The GNU Compiler Atomic Operations Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libatomic%{libatomic_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libatomic%{libatomic_sover}

%description -n libatomic%{libatomic_sover}%{libatomic_suffix}
The runtime library for atomic operations of the GNU Compiler Collection (GCC).

%package -n libatomic%{libatomic_sover}%{libatomic_suffix}-32bit
Summary:        The GNU Compiler Atomic Operations Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libatomic%{libatomic_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libatomic%{libatomic_sover}-32bit

%description -n libatomic%{libatomic_sover}%{libatomic_suffix}-32bit
The runtime library for atomic operations of the GNU Compiler Collection (GCC).

%package -n libatomic%{libatomic_sover}%{libatomic_suffix}-64bit
Summary:        The GNU Compiler Atomic Operations Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       libatomic%{libatomic_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libatomic%{libatomic_sover}-64bit

%description -n libatomic%{libatomic_sover}%{libatomic_suffix}-64bit
The runtime library for atomic operations of the GNU Compiler Collection (GCC).

%package -n liblsan%{liblsan_sover}%{liblsan_suffix}
Summary:        The GNU Compiler Leak Sanitizer Runtime Library
License:        MIT
Provides:       liblsan%{liblsan_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      liblsan%{liblsan_sover}

%description -n liblsan%{liblsan_sover}%{liblsan_suffix}
The runtime library needed to run programs compiled with the
-fsanitize=leak option of the GNU Compiler Collection (GCC).

%package -n liblsan%{liblsan_sover}%{liblsan_suffix}-32bit
Summary:        The GNU Compiler Leak Sanitizer Runtime Library
License:        MIT
Provides:       liblsan%{liblsan_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      liblsan%{liblsan_sover}-32bit

%description -n liblsan%{liblsan_sover}%{liblsan_suffix}-32bit
The runtime library needed to run programs compiled with the
-fsanitize=leak option of the GNU Compiler Collection (GCC).

%package -n liblsan%{liblsan_sover}%{liblsan_suffix}-64bit
Summary:        The GNU Compiler Leak Sanitizer Runtime Library
License:        MIT
Provides:       liblsan%{liblsan_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      liblsan%{liblsan_sover}-64bit

%description -n liblsan%{liblsan_sover}%{liblsan_suffix}-64bit
The runtime library needed to run programs compiled with the
-fsanitize=leak option of the GNU Compiler Collection (GCC).

%package -n libubsan%{libubsan_sover}%{libubsan_suffix}
Summary:        The GNU Compiler Undefined Sanitizer Runtime Library
License:        MIT
Provides:       libubsan%{libubsan_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libubsan%{libubsan_sover}

%description -n libubsan%{libubsan_sover}%{libubsan_suffix}
The runtime library needed to run programs compiled with the
-fsanitize=undefined option of the GNU Compiler Collection (GCC).

%package -n libubsan%{libubsan_sover}%{libubsan_suffix}-32bit
Summary:        The GNU Compiler Undefined Sanitizer Runtime Library
License:        MIT
Provides:       libubsan%{libubsan_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libubsan%{libubsan_sover}-32bit

%description -n libubsan%{libubsan_sover}%{libubsan_suffix}-32bit
The runtime library needed to run programs compiled with the
-fsanitize=undefined option of the GNU Compiler Collection (GCC).

%package -n libubsan%{libubsan_sover}%{libubsan_suffix}-64bit
Summary:        The GNU Compiler Undefined Sanitizer Runtime Library
License:        MIT
Provides:       libubsan%{libubsan_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libubsan%{libubsan_sover}-64bit

%description -n libubsan%{libubsan_sover}%{libubsan_suffix}-64bit
The runtime library needed to run programs compiled with the
-fsanitize=undefined option of the GNU Compiler Collection (GCC).

%package -n libvtv%{libvtv_sover}%{libvtv_suffix}
Summary:        The GNU Compiler Vtable Verifier Runtime Library
License:        MIT
Provides:       libvtv%{libvtv_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libvtv%{libvtv_sover}

%description -n libvtv%{libvtv_sover}%{libvtv_suffix}
The runtime library needed to run programs compiled with the
-fvtable-verify option of the GNU Compiler Collection (GCC).

%package -n libvtv%{libvtv_sover}%{libvtv_suffix}-32bit
Summary:        The GNU Compiler Vtable Verifier Runtime Library
License:        MIT
Provides:       libvtv%{libvtv_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libvtv%{libvtv_sover}-32bit

%description -n libvtv%{libvtv_sover}%{libvtv_suffix}-32bit
The runtime library needed to run programs compiled with the
-fvtable-verify option of the GNU Compiler Collection (GCC).

%package -n libvtv%{libvtv_sover}%{libvtv_suffix}-64bit
Summary:        The GNU Compiler Vtable Verifier Runtime Library
License:        MIT
Provides:       libvtv%{libvtv_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libvtv%{libvtv_sover}-64bit

%description -n libvtv%{libvtv_sover}%{libvtv_suffix}-64bit
The runtime library needed to run programs compiled with the
-fvtable-verify option of the GNU Compiler Collection (GCC).

%package go
Summary:        GNU Go Compiler
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}
Requires:       gcc15-go = %{version}-%{release}
Requires:       libgo%{libgo_sover} >= %{version}-%{release}

%description go
This package contains a Go compiler and associated development
files based on the GNU GCC technology.

%package go-32bit
Summary:        GNU Go Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-32bit = %{version}-%{release}
Requires:       gcc15-go = %{version}-%{release}
Requires:       libgo%{libgo_sover}-32bit >= %{version}-%{release}

%description go-32bit
This package contains a Go compiler and associated development
files based on the GNU GCC technology.

%package go-64bit
Summary:        GNU Go Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-64bit = %{version}-%{release}
Requires:       gcc15-go = %{version}-%{release}
Requires:       libgo%{libgo_sover}-64bit >= %{version}-%{release}

%description go-64bit
This package contains a Go compiler and associated development
files based on the GNU GCC technology.

%package -n libgo%{libgo_sover}%{libgo_suffix}
Summary:        GNU Go compiler runtime library
License:        BSD-3-Clause
Provides:       libgo%{libgo_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgo%{libgo_sover}

%description -n libgo%{libgo_sover}%{libgo_suffix}
Runtime library for the GNU Go language.

%package -n libgo%{libgo_sover}%{libgo_suffix}-32bit
Summary:        GNU Go compiler runtime library
License:        BSD-3-Clause
Provides:       libgo%{libgo_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgo%{libgo_sover}-32bit

%description -n libgo%{libgo_sover}%{libgo_suffix}-32bit
Runtime library for the GNU Go language.

%package -n libgo%{libgo_sover}%{libgo_suffix}-64bit
Summary:        GNU Go compiler runtime library
License:        BSD-3-Clause
Provides:       libgo%{libgo_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgo%{libgo_sover}-64bit

%description -n libgo%{libgo_sover}%{libgo_suffix}-64bit
Runtime library for the GNU Go language.

%package d
Summary:        GNU D Compiler
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}
Requires:       gcc15-d = %{version}-%{release}
Requires:       libgdruntime%{libgdruntime_sover} >= %{version}-%{release}
Requires:       libgphobos%{libgphobos_sover} >= %{version}-%{release}

%description d
This package contains a D compiler and associated development
files based on the GNU GCC technology.

%package d-32bit
Summary:        GNU D Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-32bit = %{version}-%{release}
Requires:       gcc15-d = %{version}-%{release}
Requires:       libgdruntime%{libgdruntime_sover}-32bit >= %{version}-%{release}
Requires:       libgphobos%{libgphobos_sover}-32bit >= %{version}-%{release}

%description d-32bit
This package contains a D compiler and associated development
files based on the GNU GCC technology.

%package d-64bit
Summary:        GNU D Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-64bit = %{version}-%{release}
Requires:       gcc15-d = %{version}-%{release}
Requires:       libgdruntime%{libgdruntime_sover}-64bit >= %{version}-%{release}
Requires:       libgphobos%{libgphobos_sover}-64bit >= %{version}-%{release}

%description d-64bit
This package contains a D compiler and associated development
files based on the GNU GCC technology.

%package -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Provides:       libgphobos%{libgphobos_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgphobos%{libgphobos_sover}

%description -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}
Runtime library for the GNU D language.

%package -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-32bit
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Provides:       libgphobos%{libgphobos_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgphobos%{libgphobos_sover}-32bit

%description -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-32bit
Runtime library for the GNU D language.

%package -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-64bit
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Provides:       libgphobos%{libgphobos_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgphobos%{libgphobos_sover}-64bit

%description -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-64bit
Runtime library for the GNU D language.

%package -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Provides:       libgdruntime%{libgdruntime_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgdruntime%{libgdruntime_sover}

%description -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}
Runtime library for the GNU D language.

%package -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-32bit
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Provides:       libgdruntime%{libgdruntime_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgdruntime%{libgdruntime_sover}-32bit

%description -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-32bit
Runtime library for the GNU D language.

%package -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-64bit
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Provides:       libgdruntime%{libgdruntime_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgdruntime%{libgdruntime_sover}-64bit

%description -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-64bit
Runtime library for the GNU D language.

%package -n libgccjit%{libgccjit_sover}%{libgccjit_suffix}
Summary:        The GNU Compiler Collection JIT library
License:        GPL-3.0-or-later
Provides:       libgccjit%{libgccjit_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libgccjit%{libgccjit_sover}
# At runtime the JIT needs to be able to invoke the assembler and
# linker and find startfiles and libgcc.  The built-in driver knows
# the compilers version install directory only so we require the
# respective compiler libgccjit was built from.
Requires:       gcc15

%description -n libgccjit%{libgccjit_sover}%{libgccjit_suffix}
Support for embedding GCC inside programs and libraries

%package -n libgccjit%{libgccjit_sover}-devel%{libdevel_suffix}
Summary:        Support for embedding GCC inside programs and libraries
License:        GPL-3.0-or-later
Provides:       libgccjit%{libgccjit_sover}-devel = %{version}-%{release}
# Only one gccjit package can be installed at the same time since
# header files conflict
Conflicts:      libgccjit%{libgccjit_sover}-devel
Requires:       libgccjit%{libgccjit_sover} >= %{version}-%{release}

%description -n libgccjit%{libgccjit_sover}-devel%{libdevel_suffix}
Package contains header files and documentation for GCC JIT front-end.

%package rust
Summary:        GNU Rust Compiler
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}
Requires:       gcc15-rust = %{version}-%{release}

%description rust
This package contains a Rust compiler.

%package rust-32bit
Summary:        GNU Rust Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-32bit = %{version}-%{release}
Requires:       gcc15-rust = %{version}-%{release}

%description rust-32bit
This package contains a Rust compiler.

%package rust-64bit
Summary:        GNU Rust Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-64bit = %{version}-%{release}
Requires:       gcc15-rust = %{version}-%{release}

%description rust-64bit
This package contains a Rust compiler.

%package m2
Summary:        GNU Modula-2 Compiler
License:        GPL-3.0-or-later
Requires:       gcc15 = %{version}-%{release}
Requires:       gcc15-m2 = %{version}-%{release}
Requires:       libm2cor%{libm2_sover} >= %{version}-%{release}
Requires:       libm2iso%{libm2_sover} >= %{version}-%{release}
Requires:       libm2log%{libm2_sover} >= %{version}-%{release}
Requires:       libm2min%{libm2_sover} >= %{version}-%{release}
Requires:       libm2pim%{libm2_sover} >= %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix} = %{version}-%{release}

%description m2
This package contains a Modula-2 compiler.

%package m2-32bit
Summary:        GNU Modula-2 Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-32bit = %{version}-%{release}
Requires:       gcc15-m2 = %{version}-%{release}
Requires:       libm2cor%{libm2_sover}-32bit >= %{version}-%{release}
Requires:       libm2iso%{libm2_sover}-32bit >= %{version}-%{release}
Requires:       libm2log%{libm2_sover}-32bit >= %{version}-%{release}
Requires:       libm2min%{libm2_sover}-32bit >= %{version}-%{release}
Requires:       libm2pim%{libm2_sover}-32bit >= %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-32bit = %{version}-%{release}

%description m2-32bit
This package contains a Modula-2 compiler.

%package m2-64bit
Summary:        GNU Modula-2 Compiler
License:        GPL-3.0-or-later
Requires:       gcc15-64bit = %{version}-%{release}
Requires:       gcc15-m2 = %{version}-%{release}
Requires:       libm2cor%{libm2_sover}-64bit >= %{version}-%{release}
Requires:       libm2iso%{libm2_sover}-64bit >= %{version}-%{release}
Requires:       libm2log%{libm2_sover}-64bit >= %{version}-%{release}
Requires:       libm2min%{libm2_sover}-64bit >= %{version}-%{release}
Requires:       libm2pim%{libm2_sover}-64bit >= %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-64bit = %{version}-%{release}

%description m2-64bit
This package contains a Modula-2 compiler.

%package -n libm2log%{libm2_sover}%{libm2_suffix}
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2log%{libm2_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2log%{libm2_sover}

%description -n libm2log%{libm2_sover}%{libm2_suffix}
Runtime library for the GNU Modula-2 language.

%package -n libm2log%{libm2_sover}%{libm2_suffix}-32bit
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2log%{libm2_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2log%{libm2_sover}-32bit

%description -n libm2log%{libm2_sover}%{libm2_suffix}-32bit
Runtime library for the GNU Modula-2 language.

%package -n libm2log%{libm2_sover}%{libm2_suffix}-64bit
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2log%{libm2_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2log%{libm2_sover}-64bit

%description -n libm2log%{libm2_sover}%{libm2_suffix}-64bit
Runtime library for the GNU Modula-2 language.

%package -n libm2cor%{libm2_sover}%{libm2_suffix}
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2cor%{libm2_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2cor%{libm2_sover}

%description -n libm2cor%{libm2_sover}%{libm2_suffix}
Runtime library for the GNU Modula-2 language.

%package -n libm2cor%{libm2_sover}%{libm2_suffix}-32bit
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2cor%{libm2_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2cor%{libm2_sover}-32bit

%description -n libm2cor%{libm2_sover}%{libm2_suffix}-32bit
Runtime library for the GNU Modula-2 language.

%package -n libm2cor%{libm2_sover}%{libm2_suffix}-64bit
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2cor%{libm2_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2cor%{libm2_sover}-64bit

%description -n libm2cor%{libm2_sover}%{libm2_suffix}-64bit
Runtime library for the GNU Modula-2 language.

%package -n libm2iso%{libm2_sover}%{libm2_suffix}
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2iso%{libm2_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2iso%{libm2_sover}

%description -n libm2iso%{libm2_sover}%{libm2_suffix}
Runtime library for the GNU Modula-2 language.

%package -n libm2iso%{libm2_sover}%{libm2_suffix}-32bit
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2iso%{libm2_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2iso%{libm2_sover}-32bit

%description -n libm2iso%{libm2_sover}%{libm2_suffix}-32bit
Runtime library for the GNU Modula-2 language.

%package -n libm2iso%{libm2_sover}%{libm2_suffix}-64bit
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2iso%{libm2_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2iso%{libm2_sover}-64bit

%description -n libm2iso%{libm2_sover}%{libm2_suffix}-64bit
Runtime library for the GNU Modula-2 language.

%package -n libm2pim%{libm2_sover}%{libm2_suffix}
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2pim%{libm2_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2pim%{libm2_sover}

%description -n libm2pim%{libm2_sover}%{libm2_suffix}
Runtime library for the GNU Modula-2 language.

%package -n libm2pim%{libm2_sover}%{libm2_suffix}-32bit
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2pim%{libm2_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2pim%{libm2_sover}-32bit

%description -n libm2pim%{libm2_sover}%{libm2_suffix}-32bit
Runtime library for the GNU Modula-2 language.

%package -n libm2pim%{libm2_sover}%{libm2_suffix}-64bit
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2pim%{libm2_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2pim%{libm2_sover}-64bit

%description -n libm2pim%{libm2_sover}%{libm2_suffix}-64bit
Runtime library for the GNU Modula-2 language.

%package -n libm2min%{libm2_sover}%{libm2_suffix}
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2min%{libm2_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2min%{libm2_sover}

%description -n libm2min%{libm2_sover}%{libm2_suffix}
Runtime library for the GNU Modula-2 language.

%package -n libm2min%{libm2_sover}%{libm2_suffix}-32bit
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2min%{libm2_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2min%{libm2_sover}-32bit

%description -n libm2min%{libm2_sover}%{libm2_suffix}-32bit
Runtime library for the GNU Modula-2 language.

%package -n libm2min%{libm2_sover}%{libm2_suffix}-64bit
Summary:        GNU Modula-2 compiler runtime library
License:        BSL-1.0
Provides:       libm2min%{libm2_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      libm2min%{libm2_sover}-64bit

%description -n libm2min%{libm2_sover}%{libm2_suffix}-64bit
Runtime library for the GNU Modula-2 language.

%package -n gcc15-testresults
Summary:        Testsuite results
License:        Public-Domain

%description -n gcc15-testresults
Results from running the gcc and target library testsuites.




# Define the canonical target and host architecture
#   %%gcc_target_arch  is supposed to be the full target triple
#   %%cross_arch       is supposed to be the rpm target variant arch
#   %%TARGET_ARCH      will be the canonicalized target CPU part
#   %%HOST_ARCH        will be the canonicalized host CPU part
%if 0%{?gcc_target_arch:1}
%define TARGET_ARCH %(echo %{cross_arch})
%else
%define TARGET_ARCH %(echo %{_target_cpu})
%endif
%if 0%{?disable_32bit:1}
%define biarch 0
%else
%define biarch %(case " %{biarch_targets} " in (*" %{TARGET_ARCH} "*) echo 1;; (*) echo 0;; esac)
%endif

%define HOST_ARCH %(echo %{_target_cpu})
%define GCCDIST %{HOST_ARCH}-openruyi-linux

%define libsubdir %{_libdir}/gcc/%{GCCDIST}/%{gcc_dir_version}
%define gxxinclude %{_prefix}/include/c++/%{gcc_dir_version}

# Versionspecific directories
%define versmainlibdir %{libsubdir}
%define versmainlibdirbi32 %{libsubdir}/32
%define versmainlibdirbi64 %{libsubdir}/64
%if %{build_primary_64bit}
%define versmainlibdirbi %{versmainlibdirbi32}
%else
%define versmainlibdirbi %{versmainlibdirbi64}
%endif

%define mainlibdir %{_libdir}
%define mainlibdirbi32 %{_prefix}/lib
%define mainlibdirbi64 %{_prefix}/lib64
%if %{build_primary_64bit}
%define mainlibdirbi %{mainlibdirbi32}
%else
%define mainlibdirbi %{mainlibdirbi64}
%endif

# Now define a few macros that make it easy to package libs and
# related files just to the right package, without caring for the
# exact path the files are in.
#   %%mainlib  package X from all dirs that belong to the main package
#   %%biarchlib   package X from all dirs that belong to the -32/64bit package
%define mainlib() %{mainlibdir}/%1\
%{nil}
%define biarchlib() %{nil}
%if %{biarch}
%if !%{separate_biarch}
%define mainlib() %{mainlibdir}/%1\
%{mainlibdirbi}/%1\
%{nil}
%else
%define biarchlib() %{mainlibdirbi}/%1\
%{nil}
%endif
%endif

%define versmainlib() %{versmainlibdir}/%1\
%{nil}
%define versbiarchlib() %{nil}
%if %{biarch}
%if !%{separate_biarch}
%define versmainlib() %{versmainlibdir}/%1\
%{versmainlibdirbi}/%1\
%{nil}
%else
%define versbiarchlib() %{versmainlibdirbi}/%1\
%{nil}
%endif
%endif

# Synchronize output by lines, useful for configure output
%define make_output_sync -Oline

%prep
%setup -q -n gcc-%{version}

#test patching start

%patch -P 2
%patch -p1 -P 60 -P 61
%autopatch -p1 -m 1000

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
%if 0%{?gcc_target_arch:1}
    # Kill all -march/tune/cpu because that screws building the target libs
    -march=*|-mtune=*|-mcpu=*) ;;
%endif
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
#ENABLE_CHECKING="--enable-checking=yes"
ENABLE_CHECKING="--enable-checking=release"
#ENABLE_CHECKING=""

# Work around tail/head -1 changes
export _POSIX2_VERSION=199209

%if "%{hostsuffix}" != ""
mkdir -p host-tools/bin
# Using the host gnatmake like
#   CC="gcc%%{hostsuffix}" GNATBIND="gnatbind%%{hostsuffix}"
#   GNATMAKE="gnatmake%%{hostsuffix}"
# doesn't work due to PR33857, so an un-suffixed gnatmake has to be
# available
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

# libsanitizer needs <crypt.h> and since the glibc/libxcrypt split
# we don't have that yet in a pure cross environment
%if 0%{?gcc_target_arch:1}
  CONFARGS="$CONFARGS --disable-libsanitizer"
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
%if 0%{!?gcc_target_arch:1}
  --enable-linker-build-id \
%else
%if 0%{?gcc_target_glibc:1}
  --enable-linker-build-id \
%endif
%endif
  --enable-linux-futex \
%ifarch x86_64 aarch64
  --enable-gnu-indirect-function \
%endif
  --program-suffix=%{binsuffix} \
%ifarch %{disable_multilib_arch}
  --disable-multilib \
%endif
%if 0%{!?gcc_target_arch:1}
  --without-system-libunwind \
%endif
%if 0%{?gcc_target_arch:1}
  --program-prefix=%{gcc_target_arch}- \
  --target=%{gcc_target_arch} \
  --disable-nls \
%if 0%{?sysroot:1}
  --with-sysroot=%sysroot \
%endif
%if 0%{?build_sysroot:1}
  --with-build-sysroot=%{build_sysroot} \
%else
%if 0%{?sysroot:1}
  --with-build-sysroot=%{sysroot} \
%endif
%endif
%if 0%{?binutils_os:1}
  --with-build-time-tools=/usr/%{binutils_os}/bin \
%endif
%if 0%{?gcc_target_newlib}
  --with-newlib \
%if 0%{?gcc_libc_bootstrap:1}
  --disable-gcov \
%endif
%else
%if 0%{?gcc_libc_bootstrap:1}
  --disable-gcov --disable-threads --disable-shared \
  --disable-libmudflap --disable-libssp --disable-libgomp \
  --disable-libquadmath --disable-libatomic \
  --without-headers --with-newlib \
%endif
%endif
%endif
%if "%{TARGET_ARCH}" == "aarch64"
  --enable-fix-cortex-a53-835769 \
  --enable-fix-cortex-a53-843419 \
%endif
%if "%{TARGET_ARCH}" == "x86_64"
%ifnarch %{disable_multilib_arch}
  --enable-multilib \
  --with-arch-32=x86-64-v2 \
%endif
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
%if 0%{?do_profiling} && !0%{?building_testsuite:1}
%ifarch x86_64 aarch64
%if %{with bootstrap}
%define use_pgo_bootstrap 1
%endif
%endif
%endif
%{?use_pgo_bootstrap:setarch `arch` -R} make %{?make_output_sync} %{?use_pgo_bootstrap:profiledbootstrap} STAGE1_CFLAGS="$STAGE1_FLAGS" BOOT_CFLAGS="$optflags" %{?_smp_mflags}
make info
%if 0%{?run_tests:1}
echo "Run testsuite"
(make -C %{GCCDIST}/libstdc++-v3 check-abi || true)
mv %{GCCDIST}/libstdc++-v3/testsuite/libstdc++.log %{GCCDIST}/libstdc++-v3/testsuite/libstdc++-abi.log
mv %{GCCDIST}/libstdc++-v3/testsuite/libstdc++.sum %{GCCDIST}/libstdc++-v3/testsuite/libstdc++-abi.sum
# asan needs a whole shadow address space
ulimit -v unlimited || true
make -k check %{?_smp_mflags} || true
mkdir ../testresults
../contrib/test_summary | tee ../testresults/test_summary.txt
%endif

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
cd obj-%{GCCDIST}
# Work around tail/head -1 changes
export _POSIX2_VERSION=199209
export LIBRARY_PATH=%{buildroot}/%{libsubdir}:%{buildroot}/%{mainlibdirbi}

%make_install

# # verify libasan really ended up with libstdc++ as NEEDED.
# %ifarch %asan_arch
#   readelf -d %{buildroot}/%{versmainlibdir}/libasan.so.%{libasan_sover}* | grep 'NEEDED.*libstdc++' || exit 1
# %if %{biarch}
#   readelf -d %{buildroot}/%{versmainlibdirbi}/libasan.so.%{libasan_sover}* | grep 'NEEDED.*libstdc++' || exit 1
# %endif
# %endif

# Remove some useless .la files
for lib in libobjc libgfortran libquadmath libcaf_single \
    libgomp libgomp-plugin-hsa libstdc++ libsupc++ \
    libgo libasan libhwasan libatomic libitm libtsan liblsan libubsan libvtv \
    libstdc++fs libgdruntime libgphobos libstdc++exp \
    libm2cor libm2iso libm2log libm2min libm2pim; do
  rm -f %{buildroot}/%{versmainlibdir}/$lib.la
%if %{biarch}
  rm -f %{buildroot}/%{versmainlibdirbi}/$lib.la
%endif
done

mkdir -p %{buildroot}/%{_libdir}
%if %{biarch}
%if %{build_primary_64bit}
mkdir -p %{buildroot}/%{_prefix}/lib
%else
mkdir -p %{buildroot}/%{_prefix}/lib64
%endif
%endif

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
%ifarch %quadmath_arch
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
%ifarch %atomic_arch
  libatomic \
%endif
%ifarch %itm_arch
  libitm \
%endif
%ifarch %asan_arch
  libasan \
%endif
%ifarch %tsan_arch
  libtsan \
%endif
%ifarch %lsan_arch
  liblsan \
%endif
%ifarch %ubsan_arch
  libubsan \
%endif
%ifarch %hwasan_arch
  libhwasan \
%endif
%ifarch %vtv_arch
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
%if %{biarch}
  if test -d %{buildroot}/%{versmainlibdirbi}; then
    for lib in `find %{buildroot}/%{versmainlibdirbi} -maxdepth 1 -name "$libname.so.*"`; do
      mv $lib %{buildroot}/%{mainlibdirbi}/
    done
    if test -L %{buildroot}/%{versmainlibdirbi}/$libname.so; then
      ln -sf %{mainlibdirbi}/`readlink %{buildroot}/%{versmainlibdirbi}/$libname.so | sed -e 's/\(.*\.so\.[^\.]*\).*/\1/'`  \
         %{buildroot}/%{versmainlibdirbi}/$libname.so
    fi
  fi
%endif
done
%if %{build_cp}
# And we want to move the shlib gdb pretty printers to a more sane
# place so ldconfig does not complain
mkdir -p %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdir}
mv %{buildroot}/%{mainlibdir}/libstdc++.so.*-gdb.py %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdir}/
sed -i -e '/^libdir/s/\/gcc\/%{GCCDIST}\/%{gcc_dir_version}//g' %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdir}/libstdc++.so.*-gdb.py
%if %{biarch}
  if test -d %{buildroot}/%{versmainlibdirbi}; then
    mkdir -p %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdirbi}
    mv %{buildroot}/%{mainlibdirbi}/libstdc++.so.*-gdb.py %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdirbi}/
    sed -i -e '/^libdir/s/\/gcc\/%{GCCDIST}\/%{gcc_dir_version}//g' %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdirbi}/libstdc++.so.*-gdb.py
  fi
%endif
%endif

# Move libgcc_s around
if test -L %{buildroot}/%{_lib}/libgcc_s.so; then
  rm -f %{buildroot}/%{_lib}/libgcc_s.so
  ln -sf /%{_lib}/libgcc_s.so.%{libgcc_s} %{buildroot}/%{versmainlibdir}/libgcc_s.so
else
  mv %{buildroot}/%{_lib}/libgcc_s.so %{buildroot}/%{versmainlibdir}/
fi
chmod a+x %{buildroot}/%{_lib}/libgcc_s.so.%{libgcc_s}
%if 0%{?usrmerged}
mv %{buildroot}/%{_lib}/libgcc_s.so.%{libgcc_s} %{buildroot}/%{_slibdir}/libgcc_s.so.%{libgcc_s}
%endif
%if %{biarch}
%if %{build_primary_64bit}
if test -L %{buildroot}/lib/libgcc_s.so; then
  rm -f %{buildroot}/lib/libgcc_s.so
  ln -sf /lib/libgcc_s.so.%{libgcc_s} %{buildroot}/%{versmainlibdirbi32}/libgcc_s.so
else
  mv %{buildroot}/lib/libgcc_s.so %{buildroot}/%{versmainlibdirbi32}/
fi
ln -sf %{versmainlibdirbi32}/libgcc_s.so %{buildroot}/%{versmainlibdirbi32}/libgcc_s_32.so
chmod a+x %{buildroot}/lib/libgcc_s.so.%{libgcc_s}
%if 0%{?usrmerged}
mv %{buildroot}/lib/libgcc_s.so.%{libgcc_s} %{buildroot}/%{slibdir}/libgcc_s.so.%{libgcc_s}
%endif
%else
# 32-bit biarch systems
if test -L %{buildroot}/lib64/libgcc_s.so; then
  rm -f %{buildroot}/lib64/libgcc_s.so
  ln -sf /lib64/libgcc_s.so.%{libgcc_s} %{buildroot}/%{versmainlibdirbi64}/libgcc_s.so
else
  mv %{buildroot}/lib64/libgcc_s.so %{buildroot}/%{versmainlibdirbi64}/
fi
ln -sf %{versmainlibdirbi64}/libgcc_s.so %{buildroot}/%{versmainlibdirbi64}/libgcc_s_64.so
chmod a+x %{buildroot}/lib64/libgcc_s.so.%{libgcc_s}
%if 0%{?usrmerged}
mv %{buildroot}/lib64/libgcc_s.so.%{libgcc_s} %{buildroot}/%{slibdir64}/libgcc_s.so.%{libgcc_s}
%endif
%endif
%endif

%if %{build_ada}
mv %{buildroot}/%{libsubdir}/adalib/lib*-*.so %{buildroot}/%{_libdir}
ln -sf %{_libdir}/libgnarl%{binsuffix}.so %{buildroot}/%{libsubdir}/adalib/libgnarl.so
ln -sf %{_libdir}/libgnat%{binsuffix}.so %{buildroot}/%{libsubdir}/adalib/libgnat.so
chmod a+x %{buildroot}/%{_libdir}/libgna*-*.so
%if %{biarch}
mv %{buildroot}/%{versmainlibdirbi}/adalib/lib*-*.so %{buildroot}/%{mainlibdirbi}/
ln -sf %{mainlibdirbi}/libgnarl%{binsuffix}.so %{buildroot}/%{versmainlibdirbi}/adalib/libgnarl.so
ln -sf %{mainlibdirbi}/libgnat%{binsuffix}.so %{buildroot}/%{versmainlibdirbi}/adalib/libgnat.so
chmod a+x %{buildroot}/%{mainlibdirbi}/libgna*-*.so
%endif
%endif

rm -f %{buildroot}/%{_prefix}/bin/c++%{binsuffix}

# Remove some crap from the .la files:
for l in `find %{buildroot} -name '*.la'`; do
  echo "changing $l"
  sed -e '/^dependency_libs/s| -L%{_builddir}/[^ ]*||g' \
      -e '/^dependency_libs/s| -L/usr/%{GCCDIST}/bin||g' \
      -e '/^dependency_libs/s|-lm \(-lm \)*|-lm |' \
      -e '/^dependency_libs/s|-L[^ ]* ||g' \
%if %{biarch}
%if %{build_primary_64bit}
      -e '/^libdir/s|%{_libdir}/32|%{_prefix}/lib|' \
      -e '/^libdir/s|lib64/\.\./||' \
%else
      -e '/^libdir/s|%{_libdir}/64|%{_prefix}/lib64|' \
%endif
%endif
      < $l  > $l.new
  mv $l.new $l
done

# The spec for the PIE subpackage
cat > %{buildroot}/%{libsubdir}/defaults.spec <<EOF
*default_spec:
%%{pie|fpic|fPIC|fpie|fPIE|no-pie|fno-pic|fno-PIC|fno-pie|fno-PIE|shared|static|static-pie|nostdlib|nodefaultlibs|nostartfiles:;:-fPIE}%%{fno-pic|fno-PIC|fno-pie|fno-PIE|pie|no-pie|shared|static|static-pie|nostdlib|nodefaultlibs|nostartfiles:;: -pie}
EOF

%if 0%{?run_tests:1}
cp `find . -name "*.sum"` ../testresults/
cp `find . -name "*.log"  \! -name "config.log" | grep -v 'acats.\?/tests' | grep -v libbacktrace` ../testresults/
chmod 644 ../testresults/*
%endif
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
%if %{biarch}
%if %{build_primary_64bit}
rm -f %{buildroot}/%{_prefix}/lib/libiberty.a
%else
rm -f %{buildroot}/%{_prefix}/lib64/libiberty.a
%endif
%endif
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
%find_lang cpplib%{binsuffix}
%find_lang gcc%{binsuffix}
%find_lang libstdc++
cat cpplib%{binsuffix}.lang gcc%{binsuffix}.lang > gcc15-locale.lang

%files -f floatn-fixes.list
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%dir %{libsubdir}/include
%dir %{libsubdir}/include-fixed
%if %{biarch}
%if %{build_primary_64bit}
%dir %{libsubdir}/32
%else
%dir %{libsubdir}/64
%endif
%endif
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
%{libsubdir}/include/amxtransposeintrin.h
%{libsubdir}/include/avx10_2-512bf16intrin.h
%{libsubdir}/include/avx10_2-512convertintrin.h
%{libsubdir}/include/avx10_2-512mediaintrin.h
%{libsubdir}/include/avx10_2-512minmaxintrin.h
%{libsubdir}/include/avx10_2-512satcvtintrin.h
%{libsubdir}/include/avx10_2bf16intrin.h
%{libsubdir}/include/avx10_2convertintrin.h
%{libsubdir}/include/avx10_2copyintrin.h
%{libsubdir}/include/avx10_2mediaintrin.h
%{libsubdir}/include/avx10_2minmaxintrin.h
%{libsubdir}/include/avx10_2satcvtintrin.h
%{libsubdir}/include/movrsintrin.h
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
%ifarch %asan_arch
%{libsubdir}/include/sanitizer
%endif
%if %{build_fortran}
%{libsubdir}/include/ISO_Fortran_binding.h
%endif
%versmainlib *crt*.o
%versmainlib libgcc*.a
%versmainlib libgcov.a
%versmainlib libgcc_s*.so
%versmainlib libgomp.so
%versmainlib libgomp.a
%versmainlib libgomp.spec
%ifarch %itm_arch
%versmainlib libitm.so
%versmainlib libitm.a
%versmainlib libitm.spec
%endif
%ifarch %atomic_arch
%versmainlib libatomic.so
%versmainlib libatomic.a
%endif
%ifarch %asan_arch
%versmainlib libasan.so
%versmainlib libasan.a
%versmainlib libasan_preinit.o
%endif
%ifarch %tsan_arch
%if %build_primary_64bit
%versmainlib libtsan.so
%versmainlib libtsan.a
%versmainlib libtsan_preinit.o
%endif
%endif
%ifarch %lsan_arch
%if %build_primary_64bit
%versmainlib liblsan.so
%versmainlib liblsan.a
%versmainlib liblsan_preinit.o
%endif
%endif
%ifarch %ubsan_arch
%versmainlib libubsan.so
%versmainlib libubsan.a
%endif
%ifarch %hwasan_arch
%versmainlib libhwasan.so
%versmainlib libhwasan.a
%versmainlib libhwasan_preinit.o
%endif
%ifarch %asan_arch %ubsan_arch %tsan_arch %lsan_arch %hwasan_arch
%versmainlib libsanitizer.spec
%endif
%ifarch %vtv_arch
%versmainlib libvtv.so
%versmainlib libvtv.a
%endif
%doc %{_mandir}/man1/gcc%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov-dump%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov-tool%{binsuffix}.1.gz
%doc %{_mandir}/man1/lto-dump%{binsuffix}.1.gz

%if %{separate_biarch}
%files -n gcc15%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib *crt*.o
%versbiarchlib libgcc*.a
%versbiarchlib libgcov.a
%versbiarchlib libgcc_s*.so
%versbiarchlib libgomp.so
%versbiarchlib libgomp.a
%versbiarchlib libgomp.spec
%ifarch %itm_arch
%versbiarchlib libitm.so
%versbiarchlib libitm.a
%versbiarchlib libitm.spec
%endif
%ifarch %atomic_arch
%versbiarchlib libatomic.a
%versbiarchlib libatomic.so
%endif
%ifarch %asan_arch
%versbiarchlib libasan.a
%versbiarchlib libasan.so
%versbiarchlib libasan_preinit.o
%endif
%ifarch %ubsan_arch
%versbiarchlib libubsan.a
%versbiarchlib libubsan.so
%endif
%ifarch %tsan_arch
%if %separate_bi64
%versbiarchlib libtsan.a
%versbiarchlib libtsan.so
%versbiarchlib libtsan_preinit.o
%endif
%endif
%ifarch %lsan_arch
%if %separate_bi64
%versbiarchlib liblsan.a
%versbiarchlib liblsan.so
%versbiarchlib liblsan_preinit.o
%endif
%endif
# libhwasan.{a,so} is not built in 32-bit mode
%ifarch %asan_arch %ubsan_arch %tsan_arch %lsan_arch %hwasan_arch
%versbiarchlib libsanitizer.spec
%endif
%ifarch %vtv_arch
%versbiarchlib libvtv.a
%versbiarchlib libvtv.so
%endif
%endif

%if %{enable_plugins}
%files devel
%defattr(-,root,root)
%dir %{libsubdir}/plugin
%{libsubdir}/plugin
%if %{build_m2}
%exclude %{libsubdir}/plugin/m2rte.so
%endif
%endif

%files locale -f gcc15-locale.lang

%files -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-locale -f libstdc++.lang

%files PIE
%defattr(-,root,root)
%dir %{libsubdir}
%{libsubdir}/defaults.spec

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

%if %{separate_biarch}
%files c++%{separate_biarch_suffix}
%defattr(-,root,root)
# empty - only for the dependency
%endif

%files -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}
%defattr(-,root,root)
%mainlib libstdc++.so.%{libstdcxx_sover}*

%if %{separate_biarch}
%files -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libstdc++.so.%{libstdcxx_sover}*
%endif

%files -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%versmainlib libstdc++.a
%versmainlib libstdc++fs.a
%versmainlib libstdc++exp.a
%versmainlib libstdc++.so
%versmainlib libsupc++.a
%versmainlib libstdc++.modules.json
%{_prefix}/include/c++

%files -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}
%defattr(-,root,root)
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load%{_prefix}
%dir %{_datadir}/gdb/auto-load/%{mainlibdir}
%{_datadir}/gdb/auto-load/%{mainlibdir}/libstdc++.so.*-gdb.py
%{_datadir}/gcc%{binsuffix}

%if %{separate_biarch}
%files -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%versbiarchlib libstdc++.a
%versbiarchlib libstdc++fs.a
%versbiarchlib libstdc++exp.a
%versbiarchlib libstdc++.so
%versbiarchlib libsupc++.a
%versbiarchlib libstdc++.modules.json

%files -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%dir %{_datadir}/gdb/auto-load/%{mainlibdirbi}
%{_datadir}/gdb/auto-load/%{mainlibdirbi}/libstdc++.so.*-gdb.py
%endif
%endif

%files -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}
%defattr(-,root,root)
%{_slibdir}/libgcc_s.so.%{libgcc_s}
%if %{biarch}
%if %{build_primary_64bit}
%if !%{separate_bi32}
%{slibdir}/libgcc_s.so.%{libgcc_s}
%endif
%else
%if !%{separate_bi64}
%{slibdir64}/libgcc_s.so.%{libgcc_s}
%endif
%endif
%endif

%if %{separate_bi64}
%files -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-64bit
%defattr(-,root,root)
%{slibdir64}/libgcc_s.so.%{libgcc_s}
%endif

%if %{separate_bi32}
%files -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-32bit
%defattr(-,root,root)
%{slibdir}/libgcc_s.so.%{libgcc_s}
%endif

%files -n libgomp%{libgomp_sover}%{libgomp_suffix}
%defattr(-,root,root)
%mainlib libgomp.so.%{libgomp_sover}*

%if %{separate_biarch}
%files -n libgomp%{libgomp_sover}%{libgomp_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgomp.so.%{libgomp_sover}*
%endif

%ifarch %asan_arch
%files -n libasan%{libasan_sover}%{libasan_suffix}
%defattr(-,root,root)
%mainlib libasan.so.%{libasan_sover}*

%if %{separate_biarch}
%files -n libasan%{libasan_sover}%{libasan_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libasan.so.%{libasan_sover}*
%endif
%endif

%ifarch %lsan_arch
%if %build_primary_64bit
%files -n liblsan%{liblsan_sover}%{liblsan_suffix}
%defattr(-,root,root)
%mainlib liblsan.so.%{liblsan_sover}*
%endif

%if %{separate_biarch} && %{separate_bi64}
%files -n liblsan%{liblsan_sover}%{liblsan_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib liblsan.so.%{liblsan_sover}*
%endif
%endif

%ifarch %tsan_arch
%if %build_primary_64bit
%files -n libtsan%{libtsan_sover}%{libtsan_suffix}
%defattr(-,root,root)
%mainlib libtsan.so.%{libtsan_sover}*
%endif

%if %{separate_biarch} && %{separate_bi64}
%files -n libtsan%{libtsan_sover}%{libtsan_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libtsan.so.%{libtsan_sover}*
%endif
%endif

%ifarch %hwasan_arch
%files -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}
%defattr(-,root,root)
%mainlib libhwasan.so.%{libhwasan_sover}*
%endif

%ifarch %atomic_arch
%files -n libatomic%{libatomic_sover}%{libatomic_suffix}
%defattr(-,root,root)
%mainlib libatomic.so.%{libatomic_sover}*

%if %{separate_biarch}
%files -n libatomic%{libatomic_sover}%{libatomic_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libatomic.so.%{libatomic_sover}*
%endif
%endif

%ifarch %itm_arch
%files -n libitm%{libitm_sover}%{libitm_suffix}
%defattr(-,root,root)
%mainlib libitm.so.%{libitm_sover}*

%if %{separate_biarch}
%files -n libitm%{libitm_sover}%{libitm_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libitm.so.%{libitm_sover}*
%endif
%endif

%ifarch %ubsan_arch
%files -n libubsan%{libubsan_sover}%{libubsan_suffix}
%defattr(-,root,root)
%mainlib libubsan.so.%{libubsan_sover}*

%if %{separate_biarch}
%files -n libubsan%{libubsan_sover}%{libubsan_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libubsan.so.%{libubsan_sover}*
%endif
%endif

%ifarch %vtv_arch
%files -n libvtv%{libvtv_sover}%{libvtv_suffix}
%defattr(-,root,root)
%mainlib libvtv.so.%{libvtv_sover}*

%if %{separate_biarch}
%files -n libvtv%{libvtv_sover}%{libvtv_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libvtv.so.%{libvtv_sover}*
%endif

%endif

%if %{build_fortran}
%files fortran
%defattr(-,root,root)
%dir %{libsubdir}/finclude
%{_prefix}/bin/gfortran%{binsuffix}
%{libsubdir}/f951
%{libsubdir}/finclude/*
%versmainlib libgfortran.a
%versmainlib libgfortran.so
%versmainlib libgfortran.spec
%versmainlib libcaf_single.a
%doc %{_mandir}/man1/gfortran%{binsuffix}.1.gz

%if %{separate_biarch}
%files fortran%{separate_biarch_suffix}
%defattr(-,root,root)
%dir %{versmainlibdirbi}/finclude
%{versmainlibdirbi}/finclude/*
%versbiarchlib libgfortran.a
%versbiarchlib libgfortran.so
%versbiarchlib libgfortran.spec
%versbiarchlib libcaf_single.a
%endif

%files -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}
%defattr(-,root,root)
%mainlib libgfortran.so.%{libgfortran_sover}*

%if %{separate_biarch}
%files -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgfortran.so.%{libgfortran_sover}*
%endif

%ifarch %quadmath_arch
%files -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}
%defattr(-,root,root)
%mainlib libquadmath.so.%{libquadmath_sover}*

%if %{separate_biarch}
%files -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libquadmath.so.%{libquadmath_sover}*
%endif

%files -n libquadmath%{libquadmath_sover}-devel%{libdevel_suffix}
%defattr(-,root,root)
%{libsubdir}/include/quadmath.h
%{libsubdir}/include/quadmath_weak.h
%versmainlib libquadmath.a
%versmainlib libquadmath.so

%if %{separate_biarch}
%files -n libquadmath%{libquadmath_sover}-devel%{libdevel_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib libquadmath.a
%versbiarchlib libquadmath.so
%endif
%endif
%endif

%files info
%defattr(-,root,root)
%doc %{_infodir}/cpp%{binsuffix}.info*.gz
%doc %{_infodir}/cppinternals%{binsuffix}.info*.gz
%doc %{_infodir}/gcc%{binsuffix}.info*.gz
%doc %{_infodir}/gccint%{binsuffix}.info*.gz
%doc %{_infodir}/gccinstall%{binsuffix}.info*.gz
%doc %{_infodir}/libgomp%{binsuffix}.info*.gz
%ifarch %itm_arch
%doc %{_infodir}/libitm%{binsuffix}.info*.gz
%endif
%if %{build_fortran}
%doc %{_infodir}/gfortran%{binsuffix}.info*.gz
%ifarch %quadmath_arch
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

%files -n cpp15
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
%versmainlib libobjc.a
%versmainlib libobjc.so

%if %{separate_biarch}
%files objc%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib libobjc.a
%versbiarchlib libobjc.so
%endif

%files -n libobjc%{libobjc_sover}%{libobjc_suffix}
%defattr(-,root,root)
%mainlib libobjc.so.%{libobjc_sover}*

%if %{separate_biarch}
%files -n libobjc%{libobjc_sover}%{libobjc_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libobjc.so.%{libobjc_sover}*
%endif
%endif

%if %{build_objcp}
%files obj-c++
%defattr(-,root,root)
%{libsubdir}/cc1objplus

%if %{separate_biarch}
%files obj-c++%{separate_biarch_suffix}
%defattr(-,root,root)
# empty - only for the dependency
%endif
%endif

%if %{build_ada}
%files ada
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%{_prefix}/bin/gnat*
%dir %{versmainlibdir}/adalib
%{versmainlibdir}/adainclude
%{versmainlibdir}/adalib/*.ali
%{versmainlibdir}/adalib/*.a
%{versmainlibdir}/adalib/libgnarl.so
%{versmainlibdir}/adalib/libgnat.so
%{versmainlibdir}/gnat1
%{versmainlibdir}/ada_target_properties

%if %{separate_biarch}
%files ada%{separate_biarch_suffix}
%defattr(-,root,root)
%dir %{versmainlibdirbi}/adalib
%{versmainlibdirbi}/adainclude
%{versmainlibdirbi}/adalib/*.ali
%{versmainlibdirbi}/adalib/*.a
%{versmainlibdirbi}/adalib/libgnarl.so
%{versmainlibdirbi}/adalib/libgnat.so
%{versmainlibdirbi}/ada_target_properties
%endif

%files -n libada15
%defattr(-,root,root)
%mainlib libgnarl%{binsuffix}.so
%mainlib libgnat%{binsuffix}.so

%if %{separate_biarch}
%files -n libada15%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgnarl%{binsuffix}.so
%biarchlib libgnat%{binsuffix}.so
%endif
%endif

%if %{build_go}
%files go
%defattr(-,root,root)
%{_prefix}/bin/gccgo%{binsuffix}
%{_prefix}/bin/go%{binsuffix}
%{_prefix}/bin/gofmt%{binsuffix}
%{libsubdir}/go1
%versmainlib libgo.a
%versmainlib libgo.so
%versmainlib libgobegin.a
%versmainlib libgolibbegin.a
%versmainlibdir/buildid
%versmainlibdir/cgo
%dir %mainlibdir/go
%dir %mainlibdir/go/%{gcc_dir_version}
%mainlibdir/go/%{gcc_dir_version}/%{GCCDIST}
%doc %{_mandir}/man1/gccgo%{binsuffix}.1.gz
%doc %{_mandir}/man1/go%{binsuffix}.1.gz
%doc %{_mandir}/man1/gofmt%{binsuffix}.1.gz

%if %{separate_biarch}
%files go%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib libgo.a
%versbiarchlib libgo.so
%versbiarchlib libgobegin.a
%versbiarchlib libgolibbegin.a
%dir %mainlibdirbi/go
%dir %mainlibdirbi/go/%{gcc_dir_version}
%mainlibdirbi/go/%{gcc_dir_version}/%{GCCDIST}
%endif

%files -n libgo%{libgo_sover}%{libgo_suffix}
%defattr(-,root,root)
%mainlib libgo.so.%{libgo_sover}*

%if %{separate_biarch}
%files -n libgo%{libgo_sover}%{libgo_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgo.so.%{libgo_sover}*
%endif
%endif

%if %{build_d}
%files d
%defattr(-,root,root)
%{_prefix}/bin/gdc%{binsuffix}
%{libsubdir}/d21
%versmainlib libgphobos.a
%versmainlib libgphobos.so
%versmainlib libgdruntime.a
%versmainlib libgdruntime.so
%versmainlib libgphobos.spec
%{versmainlibdir}/include/d
%doc %{_mandir}/man1/gdc%{binsuffix}.1.gz

%if %{separate_biarch}
%files d%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib libgphobos.a
%versbiarchlib libgphobos.so
%versbiarchlib libgdruntime.a
%versbiarchlib libgdruntime.so
%versbiarchlib libgphobos.spec
%endif

%files -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}
%defattr(-,root,root)
%mainlib libgphobos.so.%{libgphobos_sover}*

%if %{separate_biarch}
%files -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgphobos.so.%{libgphobos_sover}*
%endif

%files -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}
%defattr(-,root,root)
%mainlib libgdruntime.so.%{libgdruntime_sover}*

%if %{separate_biarch}
%files -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgdruntime.so.%{libgdruntime_sover}*
%endif
%endif

%if %{build_jit}
%files -n libgccjit%{libgccjit_sover}%{libgccjit_suffix}
%defattr(-,root,root)
%{_prefix}/%{_lib}/libgccjit.so.%{libgccjit_sover}*

%files -n libgccjit%{libgccjit_sover}-devel%{libdevel_suffix}
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
%versmainlib libm2log.a
%versmainlib libm2log.so
%versmainlib libm2cor.a
%versmainlib libm2cor.so
%versmainlib libm2iso.a
%versmainlib libm2iso.so
%versmainlib libm2pim.a
%versmainlib libm2pim.so
%versmainlib libm2min.a
%versmainlib libm2min.so
%doc %{_mandir}/man1/gm2%{binsuffix}.1.gz

%if %{separate_biarch}
%files m2%{separate_biarch_suffix}
%defattr(-,root,root)
%{versmainlibdirbi}/m2
%versbiarchlib libm2log.a
%versbiarchlib libm2log.so
%versbiarchlib libm2cor.a
%versbiarchlib libm2cor.so
%versbiarchlib libm2iso.a
%versbiarchlib libm2iso.so
%versbiarchlib libm2pim.a
%versbiarchlib libm2pim.so
%versbiarchlib libm2min.a
%versbiarchlib libm2min.so
%endif

%files -n libm2log%{libm2_sover}%{libm2_suffix}
%defattr(-,root,root)
%mainlib libm2log.so.%{libm2_sover}*

%if %{separate_biarch}
%files -n libm2log%{libm2_sover}%{libm2_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libm2log.so.%{libm2_sover}*
%endif

%files -n libm2cor%{libm2_sover}%{libm2_suffix}
%defattr(-,root,root)
%mainlib libm2cor.so.%{libm2_sover}*

%if %{separate_biarch}
%files -n libm2cor%{libm2_sover}%{libm2_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libm2cor.so.%{libm2_sover}*
%endif

%files -n libm2iso%{libm2_sover}%{libm2_suffix}
%defattr(-,root,root)
%mainlib libm2iso.so.%{libm2_sover}*

%if %{separate_biarch}
%files -n libm2iso%{libm2_sover}%{libm2_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libm2iso.so.%{libm2_sover}*
%endif

%files -n libm2pim%{libm2_sover}%{libm2_suffix}
%defattr(-,root,root)
%mainlib libm2pim.so.%{libm2_sover}*

%if %{separate_biarch}
%files -n libm2pim%{libm2_sover}%{libm2_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libm2pim.so.%{libm2_sover}*
%endif

%files -n libm2min%{libm2_sover}%{libm2_suffix}
%defattr(-,root,root)
%mainlib libm2min.so.%{libm2_sover}*

%if %{separate_biarch}
%files -n libm2min%{libm2_sover}%{libm2_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libm2min.so.%{libm2_sover}*
%endif
%endif

%if 0%{?run_tests:1}
%files -n gcc15-testresults
%defattr(-,root,root)
%doc testresults/test_summary.txt
%doc testresults/*.sum
%doc testresults/*.log
%endif

%changelog
%{?autochangelog}
