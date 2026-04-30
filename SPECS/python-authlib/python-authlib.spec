# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname authlib

Name:           python-%{srcname}
Version:        1.6.10
Release:        %autorelease
Summary:        Python library for OAuth and OpenID Connect
License:        BSD-3-Clause
URL:            https://github.com/authlib/authlib
#!RemoteAsset:  sha256:856a4f54d6ef3361ca6bb6d14a27e8b88f8097cca795fb428ffe13720e2ecde6
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
# No modules named django,flask,https_client,sqla_oauth2,starlette_client
BuildOption(check):  -e 'authlib.integrations.django_*'
BuildOption(check):  -e 'authlib.integrations.flask_*'
BuildOption(check):  -e 'authlib.integrations.httpx_client*'
BuildOption(check):  -e 'authlib.integrations.requests_client*'
BuildOption(check):  -e 'authlib.integrations.sqla_oauth2*'
BuildOption(check):  -e 'authlib.integrations.starlette_client*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Authlib is a Python library for building OAuth and OpenID Connect servers and
clients.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
