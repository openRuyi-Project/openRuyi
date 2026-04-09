# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond test 0

%global rocm_version 7.1.1

Name:           rocsparse
Version:        %{rocm_version}
Release:        %autorelease
Summary:        SPARSE implementation for ROCm
License:        MIT
Url:            https://github.com/ROCm/rocSPARSE
#!RemoteAsset
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF
BuildOption(conf):  -DBUILD_WITH_OFFLOAD_COMPRESS=ON
BuildOption(conf):  -DCMAKE_CXX_COMPILER=hipcc
BuildOption(conf):  -DCMAKE_C_COMPILER=clang
BuildOption(conf):  -DCMAKE_LINKER=%{rocmllvm_bindir}/ld.lld
BuildOption(conf):  -DCMAKE_AR=%{rocmllvm_bindir}/llvm-ar
BuildOption(conf):  -DCMAKE_RANLIB=%{rocmllvm_bindir}/llvm-ranlib
BuildOption(conf):  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/..
BuildOption(conf):  -DHIP_PLATFORM=amd
BuildOption(conf):  -DROCM_SYMLINK_LIBS=OFF
BuildOption(conf):  -DBUILD_CLIENTS_BENCHMARKS=%{?with_test:ON}%{!?with_test:OFF}
BuildOption(conf):  -DBUILD_CLIENTS_TESTS=%{?with_test:ON}%{!?with_test:OFF}
BuildOption(conf):  -DBUILD_CLIENTS_TESTS_OPENMP=OFF
BuildOption(conf):  -DBUILD_FORTRAN_CLIENTS=OFF
BuildOption(conf):  -DGPU_TARGETS=%{rocm_gpu_list_default}
BuildOption(conf):  -G Ninja
%if %{with test}
BuildOption(conf):  -DCMAKE_MATRICES_DIR=%{_builddir}/rocsparse-test-matrices/
%endif

BuildRequires:  clang
BuildRequires:  clang-tools-extra
BuildRequires:  compiler-rt
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(rocprim)
BuildRequires:  hipcc
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python3
BuildRequires:  rocm-cmake
BuildRequires:  rocm-llvm-macros
BuildRequires:  rocminfo
%if %{with test}
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(rocblas)
BuildRequires:  cmake(openmp)
BuildRequires:  gcc-gfortran
BuildRequires:  python3dist(pyyaml)
%endif

Provides:       %{name} = %{version}-%{release}

%description
rocSPARSE exposes a common interface that provides Basic
Linear Algebra Subroutines for sparse computation
implemented on top of AMD's Radeon Open eCosystem Platform
ROCm runtime and toolchains. rocSPARSE is created using
the HIP programming language and optimized for AMD's
latest discrete GPUs.

%package        devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}

%if %{with test}
%package        test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    test
%{summary}
%endif

%prep -a
# /usr/include/gtest/internal/gtest-port.h:273:2: error: C++ versions less than C++17 are not supported.
# Convert the c++14 to c++17
sed -i -e 's@set(CMAKE_CXX_STANDARD 14)@set(CMAKE_CXX_STANDARD 17)@' {,clients/}CMakeLists.txt


%install -a
rm -f %{buildroot}%{_prefix}/share/doc/rocsparse/LICENSE.md

%if %{with test}
mkdir -p %{buildroot}/%{_datadir}/rocsparse/matrices
install -pm 644 %{_builddir}/rocsparse-test-matrices/* %{buildroot}/%{_datadir}/rocsparse/matrices
%endif

%check
%if %{with test}
export LD_LIBRARY_PATH=%{_vpath_builddir}/library:$LD_LIBRARY_PATH
%{_vpath_builddir}/clients/staging/rocsparse-test
%endif

%files
%doc README.md
%license LICENSE.md
%{_libdir}/librocsparse.so.1{,.*}

%files devel
%{_includedir}/rocsparse/
%{_libdir}/librocsparse.so
%{_libdir}/cmake/rocsparse/

%if %{with test}
%files test
%{_bindir}/rocsparse*
%{_datadir}/rocsparse/test/rocsparse_*
%{_datadir}/rocsparse/
%{_libdir}/rocsparse/
%{_libexecdir}/rocsparse/
%endif

%changelog
%autochangelog
