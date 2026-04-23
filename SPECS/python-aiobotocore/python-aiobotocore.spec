# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aiobotocore

Name:           python-%{srcname}
Version:        3.5.0
Release:        %autorelease
Summary:        asyncio support for botocore library using aiohttp
License:        Apache-2.0
URL:            https://aiobotocore.aio-libs.org/en/latest/
VCS:            git:https://github.com/aio-libs/aiobotocore.git
#!RemoteAsset:  sha256:d45d1c4659ad0e48b694a5aa4ff18829100386f7de96c8d146ec7757a6f12918
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

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
