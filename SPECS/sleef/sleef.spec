# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: Current ld error on riscv64. Reenable it later
# But Debian disables this option for all arch
%bcond dft 0
%bcond quad 1

# Adds a BuildRequires on tlfloat and enables more tests
# TODO: no tlfloat on openRuyi
%bcond tlfloat 0

%global so_version 3

%ifarch x86_64 riscv64
%global gnuabi_arches 1
%endif

# TODO: riscv64 test-build failed on on openRuyi
%global enable_test OFF

Name:           sleef
Version:        3.9.0
Release:        %autorelease
Summary:        Vectorized math library
License:        BSL-1.0
URL:            https://sleef.org
VCS:            git:https://github.com/shibatch/sleef.git
#!RemoteAsset
Source0:        https://github.com/shibatch/sleef/archive/%{version}/sleef-%{version}.tar.gz
BuildSystem:    cmake

# -DENFORCE_TESTER3: The build should fail if we cannot build all tests.
# -DENFORCE_TESTER4: Likewise, except that tester4 requires tlfloat.
#
# -DSLEEFDFT_ENABLE_STREAM: The author writes, “The recommended value for
#   SLEEFDFT_ENABLE_STREAM depends on the architecture, and it is only
#   recommended to be turned on on x86_64.”
#   https://github.com/shibatch/sleef/discussions/654#discussioncomment-12860550
BuildOption(conf):  -GNinja
BuildOption(conf):  -DSLEEF_BUILD_DFT:BOOL=%{?with_dft:TRUE}%{?!with_dft:FALSE}
BuildOption(conf):  -DSLEEF_ENFORCE_DFT:BOOL=%{?with_dft:TRUE}%{?!with_dft:FALSE}
BuildOption(conf):  -DSLEEFDFT_ENABLE_STREAM:BOOL=FALSE
BuildOption(conf):  -DSLEEF_BUILD_QUAD:BOOL=%{?with_quad:TRUE}%{?!with_quad:FALSE}
BuildOption(conf):  -DSLEEF_BUILD_SHARED_LIBS:BOOL=TRUE
BuildOption(conf):  -DSLEEF_BUILD_TESTS=%{enable_test}
BuildOption(conf):  -DSLEEF_ENABLE_TESTER4=%{enable_test}
BuildOption(conf):  -DSLEEF_TEST_ALL_IUT==%{enable_test}
BuildOption(conf):  -DSLEEF_ENABLE_TLFLOAT:BOOL=%{?with_tlfloat:TRUE}%{?!with_tlfloat:FALSE}

BuildRequires:  cmake >= 3.4.3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja
# For tests only:
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libcrypto)
%if %{with dft}
BuildRequires:  pkgconfig(fftw3)
%endif
%if %{with tlfloat}
BuildRequires:  pkgconfig(tlfloat)
%endif

%description
SLEEF stands for SIMD Library for Evaluating Elementary Functions. It
implements vectorized versions of all C99 real floating point math functions.
It can utilize SIMD instructions that are available on modern processors. SLEEF
is designed to efficiently perform computation with SIMD instructions by
reducing the use of conditional branches and scatter/gather memory access.

The library contains implementations of all C99 real FP math functions in
double precision and single precision. Different accuracy of the results can be
chosen for a subset of the elementary functions; for this subset there are
versions with up to 1 ULP error (which is the maximum error, not the average)
and even faster versions with a few ULPs of error. For non-finite inputs and
outputs, the functions return correct results as specified in the C99 standard.

%package        devel
Summary:        Development files for sleef
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The sleef-devel package contains libraries and header files for
developing applications that use sleef.

%package        doc
Summary:        Documentation for sleef
BuildArch:      noarch

%description    doc
The sleef-doc package contains detailed API documentation for developing
applications that use sleef.

%if %{?gnuabi_arches}
%package        gnuabi
Summary:        GNUABI version of sleef

%description gnuabi
The GNUABI version of the library (libsleefgnuabi.so) is built for x86 and
aarch64 architectures. This library provides an API compatible with libmvec in
glibc, and the API conforms to the x86 vector ABI, AArch64 vector ABI and Power
Vector ABI.

%package        gnuabi-devel
Summary:        Development files for GNUABI version of sleef
Requires:       %{name}-gnuabi%{?_isa} = %{version}-%{release}

%description    gnuabi-devel
The sleef-gnuabi-devel package contains libraries for developing applications
that use the GNUABI version of sleef. Note that this package does not contain
any header files.
%endif

%if %{with dft}
%package        dft
Summary:        Discrete Fourier Transform (DFT) library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    dft
SLEEF includes subroutines for discrete Fourier transform(DFT). These
subroutines are fully vectorized, heavily unrolled, and parallelized in such a
way that modern SIMD instructions and multiple cores can be utilized for
efficient computation. It has an API similar to that of FFTW for easy
migration. The subroutines can utilize long vectors up to 2048 bits.

%package        dft-devel
Summary:        Development files for sleef-dft
Requires:       %{name}-dft%{?_isa} = %{version}-%{release}

%description    dft-devel
The sleef-dft-devel package contains libraries and header files for
developing applications that use sleef-dft.
%endif

%if %{with quad}
%package quad
Summary:        Vectorized quad-precision math library

%description    quad
An experimental quad-precision library

%package        quad-devel
Summary:        Development files for sleef-quad
Requires:       %{name}-quad%{?_isa} = %{version}-%{release}

%description    quad-devel
The sleef-quad-devel package contains libraries and header files for
developing applications that use sleef-quad.
%endif

%prep -a
rm -rf src/gencoef
# Remove an unwanted hidden file from the docs
find docs/ -type f -name .nojekyll -print -delete

%files
%license LICENSE.txt
%{_libdir}/libsleef.so.%{so_version}{,.*}

%files devel
%{_includedir}/sleef.h
%{_libdir}/libsleef.so
%{_libdir}/pkgconfig/sleef.pc
%{_libdir}/cmake/sleef/

%files doc
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.adoc
%doc docs/

%if %{?gnuabi_arches}
%files gnuabi
%license LICENSE.txt
%{_libdir}/libsleefgnuabi.so.%{so_version}{,.*}

%files gnuabi-devel
%{_libdir}/libsleefgnuabi.so
%endif

%if %{with dft}
%files dft
%{_libdir}/libsleefdft.so.%{so_version}{,.*}

%files dft-devel
%{_includedir}/sleefdft.h
%{_libdir}/libsleefdft.so
%endif

%if %{with quad}
%files quad
%license LICENSE.txt
%{_libdir}/libsleefquad.so.%{so_version}{,.*}

%files quad-devel
%{_includedir}/sleefquad.h
%{_libdir}/libsleefquad.so
%endif

%changelog
%autochangelog
