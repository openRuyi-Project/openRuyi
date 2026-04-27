# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond tests 0

Name:           ruyi
Version:        0.46.0
Release:        %autorelease
Summary:        RuyiSDK Package Manager
License:        Apache-2.0
URL:            https://github.com/ruyisdk/ruyi
#!RemoteAsset:  sha256:1652cb296fedcec5775149fc5592811414fbc84a9ffef33bc427855cb39c1c0b
Source:         https://github.com/ruyisdk/ruyi/archive/refs/tags/%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l ruyi -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry-core)
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

Requires:       python3dist(requests)
Requires:       python3dist(rich)

%description
RuyiSDK Package Manager, the official package manager for RuyiSDK.

%generate_buildrequires
%pyproject_buildrequires

%if %{with tests}
%check -a
%pytest
%endif

%files -f %{pyproject_files}
%doc README.md README.zh.md
%license LICENSE-Apache.txt
%{_bindir}/ruyi

%changelog
%autochangelog
