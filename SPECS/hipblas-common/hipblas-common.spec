# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global rocm_version 7.1.1

Name:           hipblas-common
Version:        %{rocm_version}
Release:        %autorelease
Summary:        Common files shared by hipBLAS and hipBLASLt
License:        MIT
Url:            https://github.com/ROCm/hipBLAS-common
#!RemoteAsset
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz
BuildArch:      noarch
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake

%description
%summary

%package        devel
Summary:        Libraries and headers for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%{summary}

%install -a
rm -f %{buildroot}%{_prefix}/share/doc/hipblas-common/LICENSE.md

%files devel
%license LICENSE.md
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}

%changelog
%autochangelog
