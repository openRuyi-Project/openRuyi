# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global rocm_version 7.2.4

Name:           hipblas-common
Version:        %{rocm_version}
Release:        %autorelease
Summary:        Common files shared by hipBLAS and hipBLASLt
License:        MIT
URL:            https://github.com/ROCm/hipBLAS-common
#!RemoteAsset:  sha256:4d02427f8c9074bd55d397e9e144aaaeb392f6a9b5503e30d5ecca057ac61dc8
Source0:        %{url}/archive/rocm-%{version}.tar.gz
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
