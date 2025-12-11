# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jsonschema

Name:           python-%{srcname}
Version:        4.17.3
Release:        %autorelease
Summary:        Implementation of JSON Schema validation for Python
License:        MIT
URL:            https://github.com/Julian/jsonschema
#!RemoteAsset
Source:         https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# skip some benchmarks and test_jsonschema_test_suite which requires external test suite
BuildOption(check):  -e 'jsonschema.benchmarks*' -e 'jsonschema.tests.test_jsonschema_test_suite'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-hatchling
BuildRequires:  python3-hatch-vcs
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python-hatch_fancy_pypi_readme
# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-attrs
BuildRequires:  python3-pyrsistent

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
jsonschema is an implementation of JSON Schema for Python (supporting
2.7+, including Python 3).

 - Full support for Draft 7, Draft 6, Draft 4 and Draft 3
 - Lazy validation that can iteratively report all validation errors.
 - Small and extensible
 - Programmatic querying of which properties or items failed validation.

%generate_buildrequires
%pyproject_buildrequires

%check
%pytest

%files -f %{pyproject_files}
%license COPYING json/LICENSE
%doc README.rst
%{_bindir}/jsonschema

%changelog
%{?autochangelog}
