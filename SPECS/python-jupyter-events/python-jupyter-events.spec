# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jupyter-events
%global pypi_name jupyter_events

Name:           python-%{srcname}
Version:        0.12.1
Release:        %autorelease
Summary:        Jupyter Event System library
License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter_events
#!RemoteAsset:  sha256:faff25f77218335752f35f23c5fe6e4a392a7bd99a5939ccb9b8fbf594636cf3
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l jupyter_events

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(jsonschema[format-nongpl])
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-json-logger)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(referencing)
BuildRequires:  python3dist(rfc3339-validator)
BuildRequires:  python3dist(rfc3986-validator)
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(traitlets)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
jupyter-events provides event schema validation, logging, and registration for
Jupyter applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/jupyter-events

%changelog
%autochangelog
