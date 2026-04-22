# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aiohttp-socks
%global pypi_name aiohttp_socks

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        SOCKS proxy connector for aiohttp
License:        Apache-2.0
URL:            https://pypi.org/project/aiohttp-socks/
#!RemoteAsset:  sha256:0afe51638527c79077e4bd6e57052c87c4824233d6e20bb061c53766421b10f0
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(python-socks[asyncio])
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(python-socks)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SOCKS proxy connector for aiohttp. SOCKS4(a) and SOCKS5 are supported.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
