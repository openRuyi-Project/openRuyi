# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jupyter-server
%global pypi_name jupyter_server

Name:           python-%{srcname}
Version:        2.20.0
Release:        %autorelease
Summary:        Backend services and REST APIs for Jupyter applications
License:        BSD-3-Clause
URL:            https://github.com/jupyter-server/jupyter_server
#!RemoteAsset:  sha256:b5778ba337d8015a3dc2b80803ecdd5ac18d3797fddf61a50ea5fb472b4ebe14
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l jupyter_server

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(anyio)
BuildRequires:  python3dist(argon2-cffi)
BuildRequires:  python3dist(hatch-jupyter-builder)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(jupyter-core)
BuildRequires:  python3dist(jupyter-events)
BuildRequires:  python3dist(jupyter-server-terminals)
BuildRequires:  python3dist(nbconvert)
BuildRequires:  python3dist(nbformat)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(prometheus-client)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyzmq)
BuildRequires:  python3dist(send2trash)
BuildRequires:  python3dist(terminado)
BuildRequires:  python3dist(tornado)
BuildRequires:  python3dist(traitlets)
BuildRequires:  python3dist(websocket-client)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Jupyter Server provides the core services, APIs, and REST endpoints used by
Jupyter web applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/jupyter-server

%changelog
%autochangelog
