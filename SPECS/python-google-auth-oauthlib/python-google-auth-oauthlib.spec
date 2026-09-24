# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname google-auth-oauthlib
%global pypi_name google_auth_oauthlib

Name:           python-%{srcname}
Version:        1.4.1
Release:        %autorelease
Summary:        OAuthlib integration for Google Auth
License:        Apache-2.0
URL:            https://github.com/googleapis/google-auth-library-python-oauthlib
#!RemoteAsset:  sha256:1a83f5f2a8421dedadaa3caf25b3a710dddf85a33a63144be41c2fc79174b106
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(google-auth) >= 2.15
BuildRequires:  python3dist(requests-oauthlib) >= 0.7
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Google Auth OAuthlib integrates google-auth with the requests-oauthlib OAuth
client library.

%pyproject_extras_subpkg -n python-%{srcname} tool

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/google-oauthlib-tool

%changelog
%autochangelog
