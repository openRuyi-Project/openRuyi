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
#!RemoteAsset:  sha256:0f864437ab8b6076ba6707453ef8f98a6a0d512a80e93f8abdb676f737ecb60d
Source:         https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# skip some benchmarks and test_jsonschema_test_suite which requires external test suite
BuildOption(check):  -e 'jsonschema.benchmarks*' -e 'jsonschema.tests.test_jsonschema_test_suite'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(hatch-fancy-pypi-readme)
# for tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(pyrsistent)
BuildRequires:  python3dist(hypothesis)

Provides:       python3-%{srcname} = %{version}-%{release}
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

%check -a
%pytest

%files -f %{pyproject_files}
%license COPYING json/LICENSE
%doc README.rst
%{_bindir}/jsonschema

%changelog
%autochangelog
