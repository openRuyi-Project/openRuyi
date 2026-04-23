# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zope-interface
%global pypi_name zope_interface

Name:           python-%{srcname}
Version:        8.3
Release:        %autorelease
Summary:        Interfaces for Python
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.interface
VCS:            git:https://github.com/zopefoundation/zope.interface.git
#!RemoteAsset:  sha256:e1a9de7d0b5b5c249a73b91aebf4598ce05e334303af6aa94865893283e9ff10
Source:         https://files.pythonhosted.org/packages/source/z/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l zope
BuildOption(check):  -e "zope.interface.tests*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
zope.interface provides an implementation of "object interfaces" for Python.
Interfaces are a mechanism for labeling objects as conforming to a given API or
contract. Several APIs are provided to query for interfaces and test whether
objects provide or implement them.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGES.rst
%license LICENSE.txt COPYRIGHT.txt

%changelog
%autochangelog
