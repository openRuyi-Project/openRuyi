# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# hipCUB need GPU to run test
%bcond test 0

%global rocm_release 7.2
%global rocm_patch   4
%global rocm_version %{rocm_release}.%{rocm_patch}

%global llvm_maj_ver 22

Name:           hipcub
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm port of CUDA CUB (header-only)
License:        BSD-3-Clause AND MIT
URL:            https://github.com/ROCm/rocm-libraries
#!RemoteAsset:  sha256:2b08b0e7fc8d97717bc9656a0cc0e502dd221770f34deb8721ced2239939d779
Source:         %{url}/releases/download/rocm-%{version}/hipcub.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DGPU_TARGETS=%{rocm_gpu_list_default}
BuildOption(conf):  -DBUILD_TEST=ON
BuildOption(conf):  -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang
BuildOption(conf):  -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++

BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  clang%{llvm_maj_ver}-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(rocprim)
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
BuildRequires:  ninja
BuildRequires:  rocm-cmake
BuildRequires:  rocm-llvm-macros

%global _description %{expand:
hipCUB is a thin header-only wrapper library on top of rocPRIM which enables
developers to render portable HIP code. Existing CUDA CUB source code can
be recompiled in HIP using hipCUB.
}

%description
%{_description}

%package        test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    test
%{_description}

%prep -a
# Fix cmake install lib directory
sed -i -e 's/ROCM_INSTALL_LIBDIR lib/ROCM_INSTALL_LIBDIR %{_lib}/' \
    cmake/ROCMExportTargetsHeaderOnly.cmake

%conf -p
export PATH=%{rocmllvm_bindir}:$PATH

%install -a
rm -f %{buildroot}/%{_datadir}/doc/hipcub/LICENSE.txt

%if %{without test}
%check
%endif

%files
%doc README.md
%license LICENSE.txt
%{_includedir}/hipcub/
%{_libdir}/cmake/hipcub/

%files test
%{_bindir}/test_*
%{_bindir}/hipcub/

%changelog
%autochangelog
