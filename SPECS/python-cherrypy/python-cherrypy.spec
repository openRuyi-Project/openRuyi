# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname CherryPy
%global pypi_name cherrypy

Name:           python-%{pypi_name}
Version:        18.10.0
Release:        %autorelease
Summary:        Pythonic, object-oriented web development framework
License:        BSD-3-Clause
URL:            https://cherrypy.dev/
#!RemoteAsset:  sha256:6c70e78ee11300e8b21c0767c542ae6b102a49cac5cfd4e3e313d7bb907c5891
Source0:        https://files.pythonhosted.org/packages/source/C/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pip)

Provides:       python3-%{pypi_name} = %{version}-%{release}
%python_provide python3-%{pypi_name}

%description
CherryPy allows developers to build web applications in much the same way
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
