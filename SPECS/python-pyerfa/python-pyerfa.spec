# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyerfa

Name:           python-%{srcname}
Version:        2.0.1.5
Release:        %autorelease
Summary:        Python bindings for ERFA
License:        BSD-3-Clause
URL:            https://github.com/liberfa/pyerfa
#!RemoteAsset:  sha256:17d6b24fe4846c65d5e7d8c362dcb08199dc63b30a236aedd73875cc83e1f6c0
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l erfa

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyERFA provides Python bindings for the ERFA astronomy library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE.rst licenses/

%changelog
%autochangelog
