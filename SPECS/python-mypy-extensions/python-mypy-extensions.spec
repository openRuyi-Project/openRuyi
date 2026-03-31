# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mypy_extensions
%global pypi_name mypy-extensions

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        %autorelease
Summary:        Type system extensions for programs checked with the mypy type checker
License:        MIT
URL:            https://github.com/python/mypy_extensions
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The `mypy_extensions` module defines extensions to the Python standard library `typing` module that are supported by the mypy type checker and the mypyc compiler.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%{?autochangelog}
