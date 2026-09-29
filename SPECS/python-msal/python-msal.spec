# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname msal

Name:           python-%{srcname}
Version:        1.39.0
Release:        %autorelease
Summary:        Microsoft Authentication Library for Python
License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-python
#!RemoteAsset:  sha256:6ab7de335e6d7f5717e2c7e1dbf86e4dda2f6acf3c56773b78dc53ebc6395b5f
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
# msal.broker requires pymsalruntime from upstream's optional platform broker extra.
BuildOption(check):    -e msal.broker

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cryptography) < 51
BuildRequires:  python3dist(pyjwt[crypto]) >= 1
BuildRequires:  python3dist(pyjwt[crypto]) < 3
BuildRequires:  python3dist(requests) < 3
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
MSAL for Python enables applications to authenticate users and access the
Microsoft identity platform using OAuth 2.0 and OpenID Connect.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
