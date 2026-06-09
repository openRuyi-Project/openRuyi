# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jsonschema

Name:           python-%{srcname}
Version:        4.26.0
Release:        %autorelease
Summary:        Implementation of JSON Schema validation for Python
License:        MIT
URL:            https://github.com/Julian/jsonschema
#!RemoteAsset:  sha256:0c26707e2efad8aa1bfc5b7ce170f3fccc2e4918ff85989ba9ffa9facb2be326
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
BuildRequires:  python3dist(jsonpath-ng)

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
%doc README.rst
%license COPYING json/LICENSE
%{_bindir}/jsonschema

%changelog
%autochangelog
