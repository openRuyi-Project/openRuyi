# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond tests 0

Name:           ruyi
Version:        0.43.0
Release:        %autorelease
Summary:        RuyiSDK Package Manager
License:        Apache-2.0
URL:            https://github.com/ruyisdk/ruyi
#!RemoteAsset
Source:         https://github.com/ruyisdk/ruyi/archive/refs/tags/%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l ruyi -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-pip
BuildRequires:  python3-poetry_core
%if %{with tests}
BuildRequires:  python3-pytest
%endif

Requires:       python3-requests
Requires:       python3-rich

%description
RuyiSDK Package Manager, the official package manager for RuyiSDK.

%generate_buildrequires
%pyproject_buildrequires

%check
%if %{with tests}
%pytest
%endif

%files -f %{pyproject_files}
%license LICENSE-Apache.txt
%doc README.md README.zh.md
%{_bindir}/ruyi

%changelog
%autochangelog
