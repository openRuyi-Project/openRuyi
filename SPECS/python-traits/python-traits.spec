# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname traits

Name:           python-%{srcname}
Version:        7.1.0
Release:        %autorelease
Summary:        Explicitly typed attributes for Python
License:        BSD-3-Clause AND CC-BY-3.0
URL:            http://docs.enthought.com/traits/
VCS:            git:https://github.com/enthought/traits
#!RemoteAsset:  sha256:af4775747e11e05ffe13d3ba463d92f67f1f3d1a9e4f46ba33a44ea22b0c9644
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Maybe upstream should update these tests
BuildOption(check):  -e traits.stubs_tests.examples
BuildOption(check):  -e 'traits.stubs_tests.examples.*'
BuildOption(check):  -e traits.stubs_tests.numpy_examples.Array
# No module named 'sphinx'
BuildOption(check):  -e traits.util.trait_documenter

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(numpy)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The traits package developed by Enthought provides a special type
definition called a trait. Although they can be used as normal Python object
attributes, traits also have several additional characteristics: initialization,
validation, delegation, notification, and visualization.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES.rst README.rst examples/tutorials/
%license LICENSE.txt

%changelog
%autochangelog
