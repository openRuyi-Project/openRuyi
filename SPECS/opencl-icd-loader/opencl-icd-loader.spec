# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstream_version 2026.05.29

Name:           opencl-icd-loader
Version:        3.1
Release:        %autorelease
Summary:        Khronos official OpenCL ICD Loader
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/OpenCL-ICD-Loader
VCS:            git:https://github.com/KhronosGroup/OpenCL-ICD-Loader.git
#!RemoteAsset:  sha256:48fd0c5181db7cd046f4f731d5955694892e10998d49d09ee0d997e7e04fd939
Source0:        https://github.com/KhronosGroup/OpenCL-ICD-Loader/archive/refs/tags/v%{upstream_version}/%{name}-%{upstream_version}.tar.gz
BuildSystem:    cmake

BuildOption(prep):  -n %{name}-%{upstream_version}
BuildOption(conf):  -DOPENCL_ICD_LOADER_HEADERS_DIR=%{_includedir}
BuildOption(conf):  -DBUILD_TESTING=ON

BuildRequires:  cmake
BuildRequires:  pkgconfig(OpenCL-Headers)

%description
Khronos official OpenCL ICD Loader.

%package        devel
Summary:        Development files for the Khronos OpenCL ICD loader
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opencl-headers

%description    devel
This package contains the shared library symlink, pkg-config file and CMake
configuration needed to link applications against the Khronos OpenCL ICD loader.

%files
%doc README.md
%license LICENSE
%{_libdir}/libOpenCL.so.1
%{_libdir}/libOpenCL.so.1.0.0

%files devel
%{_bindir}/cllayerinfo
%{_libdir}/libOpenCL.so
%{_libdir}/pkgconfig/OpenCL.pc
%{_datadir}/cmake/OpenCLICDLoader/

%changelog
%autochangelog
