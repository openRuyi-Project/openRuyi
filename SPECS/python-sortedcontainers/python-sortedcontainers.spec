# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sortedcontainers

Name:           python-%{srcname}
Version:        2.4.0
Release:        %autorelease
Summary:        Pure Python sorted container types
License:        Apache-2.0
URL:            https://github.com/grantjenks/python-sortedcontainers
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
SortedContainers is an Apache2 licensed sorted collections library, written in
pure-Python, and fast as C-extensions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
