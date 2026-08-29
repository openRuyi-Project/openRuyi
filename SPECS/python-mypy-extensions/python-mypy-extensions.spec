# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mypy-extensions
%global pypi_name mypy_extensions

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        Type system extensions for programs checked with the mypy type checker
License:        MIT
URL:            https://github.com/python/mypy_extensions
#!RemoteAsset:  sha256:52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The `mypy_extensions` module defines extensions to the Python standard
library `typing` module that are supported by the mypy type checker and
the mypyc compiler.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
