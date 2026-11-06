# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname httpx2

Name:           python-%{srcname}
Version:        2.13.0
Release:        %autorelease
Summary:        HTTP client for Python
License:        BSD-3-Clause
URL:            https://github.com/pydantic/httpx2
#!RemoteAsset:  sha256:81bd07dc67a3701729ef1f777a3c00c915d4539604fdb5afd327f8682f6b7b44
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# The WebSocket adapter imports wsproto, which is provided by the optional WebSocket extra.
BuildOption(check):  -e %{srcname}.websockets

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(anyio)
BuildRequires:  python3dist(httpcore2)
BuildRequires:  python3dist(idna)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
HTTPX 2 provides a next generation HTTP client for Python.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_bindir}/httpx2

%changelog
%autochangelog
