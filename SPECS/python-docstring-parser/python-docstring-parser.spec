# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname docstring-parser
%global pypi_name docstring_parser

Name:           python-%{srcname}
Version:        0.18.0
Release:        %autorelease
Summary:        Parse Python docstrings in reST, Google and Numpydoc format
License:        MIT
URL:            https://github.com/rr-/docstring_parser
#!RemoteAsset:  sha256:292510982205c12b1248696f44959db3cdd1740237a968ea1e2e7a900eeb2015
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
BuildOption(check):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
docstring-parser parses Python docstrings written in reStructuredText, Google
or Numpydoc style into a structured representation.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE.md

%changelog
%autochangelog
