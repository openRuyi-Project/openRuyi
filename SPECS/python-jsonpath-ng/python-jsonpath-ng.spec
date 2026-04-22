# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jsonpath-ng

Name:           python-%{srcname}
Version:        1.7.0
Release:        %autorelease
Summary:        Implementation of JSONPath for Python
License:        Apache-2.0 AND WTFPL
URL:            https://github.com/h2non/jsonpath-ng
#!RemoteAsset:  sha256:f6f5f7fd4e5ff79c785f1573b394043b39849fb2bb47bcead935d12b00beab3c
Source:         https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l jsonpath_ng

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(ply)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Implementation of JSONPath for Python that aims to be standard compliant,
including arithmetic and binary comparison operators, as defined in the
original JSONPath proposal.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/jsonpath_ng

%changelog
%autochangelog
