# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname Authlib
%global pypi_name authlib

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        %autorelease
Summary:        The ultimate Python library for OAuth and OpenID Connect
License:        BSD-3-Clause
URL:            https://github.com/authlib/authlib
#!RemoteAsset:  sha256:b3e326c9aa9cc3ea95fe7d89fd880722d3608da4d00e8a27e061e64b48d801d5
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(joserfc)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(werkzeug)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{pypi_name} = %{version}-%{release}
%python_provide python3-%{pypi_name}

%description
The ultimate Python library in building OAuth and OpenID Connect servers
and clients. Supports OAuth 1.0, OAuth 2.0, OpenID Connect, and JOSE (JWS,
JWE, JWK, JWT).

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
