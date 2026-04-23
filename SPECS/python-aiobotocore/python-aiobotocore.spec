# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aiobotocore

Name:           python-%{srcname}
Version:        3.7.0
Release:        %autorelease
Summary:        asyncio support for botocore library using aiohttp
License:        Apache-2.0
URL:            https://aiobotocore.aio-libs.org/en/latest/
VCS:            git:https://github.com/aio-libs/aiobotocore.git
#!RemoteAsset:  sha256:c64d871ed5491a6571948dd48eabd185b46c6c23b64e3afd0c059fc7593ada30
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
