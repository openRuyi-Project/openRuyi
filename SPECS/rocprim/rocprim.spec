# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global rocm_version 7.1.1

Name:           rocprim
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm parallel primatives
License:        MIT AND BSD-3-Clause
URL:            https://github.com/ROCm/rocPRIM
#!RemoteAsset
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF
BuildOption(conf):  -DBUILD_TEST=OFF
BuildOption(conf):  -DCMAKE_AR=%{rocmllvm_bindir}/llvm-ar
BuildOption(conf):  -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang
BuildOption(conf):  -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++
BuildOption(conf):  -DCMAKE_LINKER=%{rocmllvm_bindir}/ld.lld
BuildOption(conf):  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/..
BuildOption(conf):  -DCMAKE_RANLIB=%{rocmllvm_bindir}/llvm-ranlib
BuildOption(conf):  -DGPU_TARGETS=%{rocm_gpu_list_default}
BuildOption(conf):  -DROCM_SYMLINK_LIBS=OFF

BuildRequires:  clang-tools-extra-devel
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(Clang)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(LLD)
BuildRequires:  cmake(LLVM)
BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  rocm-cmake
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-llvm-macros
BuildRequires:  rocminfo

%description
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%package        devel
Summary:        ROCm parallel primatives
BuildArch:      noarch

%description    devel
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%install -a
rm -f %{buildroot}%{_prefix}/share/doc/rocprim/LICENSE.md

%files devel
%doc README.md
%license LICENSE.md
%license NOTICES.txt
%{_includedir}/%{name}
%{_libdir}/cmake/rocprim

%changelog
%autochangelog
