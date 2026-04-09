# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cherrypy
%global camelname CherryPy

Name:           python-%{srcname}
Version:        18.10.0
Release:        %autorelease
Summary:        Pythonic, object-oriented web development framework
License:        BSD-3-Clause
URL:            https://cherrypy.dev/
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/C/%{camelname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
%{camelname} allows developers to build web applications in much the same way
they would build any other object-oriented Python program. This usually
results in smaller source code developed in less time.

%generate_buildrequires
# Nothing to do

%check
# skip tests as some deps we don't have yet.

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.md
%{_bindir}/cherryd

%changelog
%autochangelog
