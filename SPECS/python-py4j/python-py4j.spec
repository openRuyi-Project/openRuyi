# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname py4j

Name:           python-%{srcname}
Version:        0.10.9.9
Release:        %autorelease
Summary:        Dynamic access to Java objects from Python
License:        BSD-3-Clause
URL:            https://www.py4j.org/
VCS:            git:https://github.com/bartdag/py4j.git
#!RemoteAsset:  sha256:f694cad19efa5bd1dee4f3e5270eb406613c974394035e5bfc4ec1aba870b879
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l py4j

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Py4J enables Python programs to dynamically access Java objects in a Java
virtual machine.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{_datadir}/py4j/

%changelog
%autochangelog
