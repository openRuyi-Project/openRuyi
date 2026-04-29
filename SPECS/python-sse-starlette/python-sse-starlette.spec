# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sse-starlette
%global pypi_name sse_starlette

Name:           python-%{srcname}
Version:        3.3.4
Release:        %autorelease
Summary:        Server-Sent Events for Starlette and FastAPI
License:        BSD-3-Clause
URL:            https://github.com/sysid/sse-starlette
#!RemoteAsset:  sha256:aaf92fc067af8a5427192895ac028e947b484ac01edbc3caf00e7e7137c7bef1
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(anyio)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Production ready Server-Sent Events implementation for Starlette and FastAPI
following the W3C SSE specification.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc AUTHORS README.md
%license LICENSE

%changelog
%autochangelog
