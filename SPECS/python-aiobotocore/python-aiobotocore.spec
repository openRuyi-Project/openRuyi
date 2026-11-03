# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aiobotocore

Name:           python-%{srcname}
Version:        3.10.0
Release:        %autorelease
Summary:        asyncio support for botocore library using aiohttp
License:        Apache-2.0
URL:            https://aiobotocore.aio-libs.org/en/latest/
VCS:            git:https://github.com/aio-libs/aiobotocore.git
#!RemoteAsset:  sha256:35480ef11c51e23087273b85d97f80da2f356a46ce5f3fb88e24483cd343ffdb
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Async client for amazon services using botocore and aiohttp/asyncio.
This library is a mostly full featured asynchronous version of botocore.

%prep -a
sed -i -E 's/"botocore[^"]*"/"botocore"/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
