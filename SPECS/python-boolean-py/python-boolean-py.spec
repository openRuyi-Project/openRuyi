# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname boolean_py

Name:           python-boolean-py
Version:        5.0
Release:        %autorelease
Summary:        Boolean algebra in one Python module
License:        BSD-2-clause
URL:            https://github.com/bastikr/boolean.py
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l boolean +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-boolean-py
%python_provide python3-boolean-py

%description
This is a small Python library that implements boolean algebra.
It defines two base elements, @code{TRUE} and @code{FALSE}, and a
@code{Symbol} class that can take on one of these two values.  Calculations
are done only in terms of @code{AND}, @code{OR}, and @code{NOT}---other
compositions like @code{XOR} and @code{NAND} are emulated on top of them.
Expressions are constructed from parsed strings or directly in Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%{?autochangelog}
