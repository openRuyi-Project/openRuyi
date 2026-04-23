# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pycparser

Name:           python-%{srcname}
Version:        2.21
Release:        %autorelease
Summary:        C parser in Python
License:        BSD-3-Clause
URL:            https://github.com/eliben/pycparser
#!RemoteAsset:  sha256:e644fdec12f7872f86c58ff790da456218b10f863970249516d60a5eaca77206
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Pycparser is a complete parser of the C language, written in pure Python
using the PLY parsing library.  It parses C code into an AST and can serve as
a front-end for C compilers or analysis tools.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE

%changelog
%autochangelog
