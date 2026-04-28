# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname semantic_version

Name:           python-semantic-version
Version:        2.10.0
Release:        %autorelease
Summary:        Library implementing the 'SemVer' scheme
License:        BSD-2-Clause
URL:            https://github.com/rbarrois/python-semanticversion
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# skip the tests as we have no django yet.
BuildOption(check):  -e semantic_version.django_fields

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

# We provide these for compatibility
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
Provides:       python3-semantic-version
%python_provide python3-semantic-version

%description
This small python library provides a few tools to handle semantic versioning in
Python.

%files -f %{pyproject_files}
%doc README.rst ChangeLog CREDITS

%changelog
%{?autochangelog}
