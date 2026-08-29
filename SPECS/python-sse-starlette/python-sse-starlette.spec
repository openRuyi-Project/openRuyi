# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sse-starlette
%global pypi_name sse_starlette

Name:           python-%{srcname}
Version:        3.4.2
Release:        %autorelease
Summary:        Server-Sent Events plugin for Starlette
License:        BSD-3-Clause
URL:            https://github.com/sysid/sse-starlette
#!RemoteAsset:  sha256:2f9a7f51ed84395a0427fb9f66cb1ec11f7899d977a72cbc9070b962a2e14489
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
BuildOption(check):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(anyio)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(starlette)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
sse-starlette provides asynchronous Server-Sent Events support for Starlette
applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
