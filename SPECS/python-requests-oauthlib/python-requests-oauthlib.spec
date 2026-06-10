# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname requests-oauthlib

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        OAuthlib authentication support for Requests
License:        ISC
URL:            https://github.com/requests/requests-oauthlib
VCS:            git:https://github.com/requests/requests-oauthlib.git
#!RemoteAsset:  sha256:b3dffaebd884d8cd778494369603a9e7b58d29111bf6b41bdc2dcd87203af4e9
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l requests_oauthlib

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This project provides first-class OAuth library support for Requests,
making it easy to authenticate against OAuth 1.0/a and OAuth 2.0
protected resources.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
