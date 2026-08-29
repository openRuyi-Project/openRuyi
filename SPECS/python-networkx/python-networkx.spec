# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname networkx

Name:           python-%{srcname}
Version:        3.6.1
Release:        %autorelease
Summary:        Network Analysis in Python
License:        BSD-3-Clause
URL:            https://github.com/networkx/networkx
#!RemoteAsset:  sha256:26b7c357accc0c8cde558ad486283728b65b6a95d85ee1cd66bafab4c8168509
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# We don't have python-pygraphviz, python3dist(pytest_mpl), python-matplotlib, etc...
BuildOption(check):  -e 'networkx.drawing.tests.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
# For tests
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(sympy)
BuildRequires:  python3dist(pydot)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog
