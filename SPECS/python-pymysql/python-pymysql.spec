# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define srcname pymysql

Name:           python-pymysql
Version:        1.1.3
Release:        %autorelease
Summary:        Pure-Python MySQL client library
License:        MIT
URL:            https://github.com/PyMySQL/PyMySQL
#!RemoteAsset:  sha256:e70ebf2047a4edf6138cf79c68ad418ef620af65900aa585c5e8bfc95044d43a
Source:         https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-1.1.3.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-pymysql = %{version}-%{release}
%python_provide python3-pymysql

%description
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
