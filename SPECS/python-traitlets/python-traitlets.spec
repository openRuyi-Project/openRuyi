# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname traitlets

Name:           python-%{srcname}
Version:        5.15.0
Release:        %autorelease
Summary:        A lightweight derivative of Enthought Traits for configuring Python objects
License:        BSD-3-Clause
URL:            https://github.com/ipython/traitlets
#!RemoteAsset:  sha256:4fead733f81cf1c4c938e06f8ca4633896833c9d89eff878159457f4d4392971
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A lightweight pure-Python derivative of Enthought Traits, used for
configuring Python objects.

This package powers the config system of IPython and Jupyter.

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
