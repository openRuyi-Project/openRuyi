# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aiohttp

Name:           python-%{srcname}
Version:        3.13.3
Release:        %autorelease
Summary:        Python HTTP client/server for asyncio
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiohttp
#!RemoteAsset:  sha256:a949eee43d3782f2daae4f4a2819b2cb9b0c5d3b7f7a927067cc84dafdbb9f88
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pkgconfig)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(multidict)
BuildRequires:  python3dist(yarl)
BuildRequires:  python3dist(aiohappyeyeballs)
BuildRequires:  python3dist(aiosignal)
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(frozenlist)
BuildRequires:  python3dist(propcache)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python HTTP client/server for asyncio which supports both the client and the
server side of the HTTP protocol, client and server websocket, and webservers
with middlewares and pluggable routing.

%generate_buildrequires
%pyproject_buildrequires

%check
# skip tests as some deps we don't have yet.

%files -f %{pyproject_files}
%doc CHANGES.rst
%doc README.rst

%changelog
%autochangelog
