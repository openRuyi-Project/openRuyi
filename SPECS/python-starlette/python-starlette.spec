# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname starlette

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        The little ASGI library that shines
License:        BSD-3-Clause
URL:            https://github.com/Kludex/starlette
VCS:            git:https://github.com/Kludex/starlette.git
#!RemoteAsset:  sha256:6a4beaf1f81bb472fd19ea9b918b50dc3a77a6f2e190a12954b25e6ed5eea149
Source:         https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(itsdangerous)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(httpx)

Requires:       python3dist(anyio)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Starlette is a lightweight ASGI framework for building async web services in
Python. It provides routing, middleware, WebSocket support, and other tools for
high-performance web applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
