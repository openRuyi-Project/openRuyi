# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname redis

Name:           python-%{srcname}
Version:        7.4.0
Release:        %autorelease
Summary:        Redis Python client
License:        MIT
URL:            https://github.com/redis/redis-py
#!RemoteAsset:  sha256:64a6ea7bf567ad43c964d2c30d82853f8df927c5c9017766c55a1d1ed95d18ad
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e redis.asyncio.multidb.*
BuildOption(check):  -e redis.multidb.*

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(requests)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The Python interface to the Redis key-value store.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
