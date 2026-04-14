# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname starlette

Name:           python-%{srcname}
Version:        0.52.1
Release:        %autorelease
Summary:        Lightweight ASGI framework/toolkit
License:        BSD-3-Clause
URL:            https://www.starlette.io/
VCS:            git:https://github.com/encode/starlette.git
#!RemoteAsset:  sha256:834edd1b0a23167694292e94f597773bc3f89f362be6effee198165a35d62933
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):    starlette

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(itsdangerous)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Starlette is a lightweight ASGI framework/toolkit, ideal for building async
web services in Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
