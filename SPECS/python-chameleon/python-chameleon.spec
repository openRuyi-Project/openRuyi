# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname chameleon
%global pypi_name Chameleon

Name:           python-%{srcname}
Version:        4.6.0
Release:        %autorelease
Summary:        Fast HTML/XML template compiler
License:        BSD-3-Clause AND BSD-4-Clause AND Python-2.0 AND ZPL-2.1
URL:            https://chameleon.readthedocs.io
VCS:            git:https://github.com/malthe/chameleon.git
#!RemoteAsset:  sha256:910cd729f6f7f38adad132ee51faa4f3ccc8344a6721aac31aa51a31f5781c1b
Source0:        https://files.pythonhosted.org/packages/source/C/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Chameleon is an HTML/XML template engine for Python. It uses the page templates
language.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES.rst COPYRIGHT.txt README.rst
%license LICENSE.txt

%changelog
%autochangelog
