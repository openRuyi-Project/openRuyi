# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname boolean.py
%global pypi_name boolean_py

Name:           python-boolean-py
Version:        5.0
Release:        %autorelease
Summary:        Boolean algebra in one Python module
License:        BSD-2-clause
URL:            https://github.com/bastikr/boolean.py
#!RemoteAsset:  sha256:60cbc4bad079753721d32649545505362c754e121570ada4658b852a3a318d95
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l boolean +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-boolean-py = %{version}-%{release}
%python_provide python3-boolean-py

%description
This is a small Python library that implements boolean algebra.
It defines two base elements, TRUE and FALSE, and a Symbol class
that can take on one of these two values.  Calculations are done
only in terms of AND, OR, and NOT---other compositions like XOR
and NAND are emulated on top of them. Expressions are constructed
from parsed strings or directly in Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
