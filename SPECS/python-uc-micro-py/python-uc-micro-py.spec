# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pypi_name uc_micro

%global srcname uc-micro-py

Name:           python-%{srcname}
Version:        1.0.3
Release:        %autorelease
Summary:        Micro subset of Unicode data files for linkify-it.py
License:        MIT
URL:            https://github.com/tsutsu3/uc.micro-py
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Micro subset of Unicode data files for linkify-it.py projects. This is a
Python port of uc.micro (JavaScript).

%generate_buildrequires
%pyproject_buildrequires

%check
%pytest -v

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
