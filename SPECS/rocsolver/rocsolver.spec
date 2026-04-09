# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global rocm_version 7.1.1

# consume too much time
%bcond test 0
%bcond sample 0
%bcond benchmark 0

Name:           rocsolver
Version:        %{rocm_version}
Release:        %autorelease
Summary:        Next generation LAPACK implementation for ROCm platform
License:        BSD-3-Clause AND BSD-2-Clause
Url:            https://github.com/ROCm/rocSOLVER
#!RemoteAsset
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DCMAKE_CXX_COMPILER=hipcc
BuildOption(conf):  -DCMAKE_C_COMPILER=clang
BuildOption(conf):  -DCMAKE_AR=%{rocmllvm_bindir}/llvm-ar
BuildOption(conf):  -DCMAKE_RANLIB=%{rocmllvm_bindir}/llvm-ranlib
BuildOption(conf):  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/..
BuildOption(conf):  -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF
BuildOption(conf):  -DROCM_SYMLINK_LIBS=OFF
BuildOption(conf):  -DHIP_PLATFORM=amd
BuildOption(conf):  -DAMDGPU_TARGETS=%{rocm_gpu_list_default}
BuildOption(conf):  -DBUILD_OFFLOAD_COMPRESS=ON
BuildOption(conf):  -DBUILD_PARALLEL_HIP_JOBS=ON
BuildOption(conf):  -DBUILD_CLIENTS_TESTS=%{?with_test:ON}%{!?with_test:OFF}
BuildOption(conf):  -DBUILD_CLIENTS_BENCHMARKS=%{?with_benchmark:ON}%{!?with_benchmark:OFF}
BuildOption(conf):  -DBUILD_CLIENTS_SAMPLES=%{?with_sample:ON}%{!?with_sample:OFF}

# https://github.com/ROCm/rocSOLVER/pull/652
Patch0:         0001-rocsolver-ninja-job-pools.patch
# https://github.com/ROCm/rocSOLVER/pull/962
Patch1:         0001-rocsolver-parallel-jobs.patch

BuildRequires:  clang
BuildRequires:  clang-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(rocblas)
BuildRequires:  cmake(rocprim)
BuildRequires:  compiler-rt
BuildRequires:  gcc-c++
BuildRequires:  hipcc
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  ninja
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-llvm-macros
BuildRequires:  rocsparse-devel
BuildRequires:  rocminfo

Provides:       rocsolver = %{version}-%{release}

%description
rocSOLVER is a work-in-progress implementation of a subset
of LAPACK functionality on the ROCm platform.

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

%install -a
rm -f %{buildroot}%{_prefix}/share/doc/rocsolver/LICENSE.md

%files
%license LICENSE.md
%doc README.md
%{_libdir}/librocsolver.so.0{,.*}

%files devel
%{_includedir}/rocsolver/
%{_libdir}/librocsolver.so
%{_libdir}/cmake/rocsolver/

%if %{with test}
%files test
%{_datadir}/rocsolver/
%{_bindir}/rocsolver*
%endif

%changelog
%autochangelog
