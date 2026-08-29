# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pygtrie

Name:           python-%{srcname}
Version:        2.5.0
Release:        %autorelease
Summary:        Trie data structure implementation for Python
License:        Apache-2.0
URL:            https://github.com/mina86/pygtrie
VCS:            git:https://github.com/mina86/pygtrie.git
#!RemoteAsset:  sha256:203514ad826eb403dab1d2e2ddd034e0d1534bbe4dbe0213bb0593f66beba4e2
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pygtrie provides a trie data structure implementation for Python. It includes
mutable mappings optimized for prefix lookup operations.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
