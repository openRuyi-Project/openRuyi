# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pypi_name python-slugify
%global srcname slugify

Name:           python-%{pypi_name}
Version:        8.0.4
Release:        %autorelease
Summary:        Python module to deal with unicode slugs
License:        BSD-3-Clause
URL:            https://github.com/un33k/python-slugify
#!RemoteAsset:  sha256:59202371d1d05b54a9e7720c5e038f928f45daaffe41dd10822f3907b937c856
Source:         https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(text-unidecode)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A Python slugify application that handles Unicode.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{srcname}

%changelog
%autochangelog
