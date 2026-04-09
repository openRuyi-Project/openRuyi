# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond tests 0

%global srcname parameterized

Name:           python-%{srcname}
Version:        0.9.0
Release:        %autorelease
Summary:        Parameterized testing with any Python test framework
License:        BSD-2-Clause
URL:            https://github.com/wolever/parameterized
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l parameterized

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-nose2
%endif

Provides:       python3-parameterized = %{version}-%{release}
%python_provide python3-parameterized

%description
Parameterized testing with any Python test framework.

%generate_buildrequires
%pyproject_buildrequires

%check
%if %{with tests}
%{python3} -m nose2 -v
%pytest parameterized/test.py
%{python3} -m unittest -v parameterized.test
%endif

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
