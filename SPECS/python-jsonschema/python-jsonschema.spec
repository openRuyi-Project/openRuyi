# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jsonschema

Name:           python-%{srcname}
Version:        4.26.0
Release:        %autorelease
Summary:        Implementation of JSON Schema validation for Python
License:        MIT
URL:            https://github.com/python-jsonschema/jsonschema
#!RemoteAsset
Source:         https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatch-fancy-pypi-readme)
# runtime dependencies
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(jsonschema-specifications)
BuildRequires:  python3dist(referencing)
BuildRequires:  python3dist(rpds-py)
# for tests
BuildRequires:  python3dist(pytest)

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
%pytest --ignore=jsonschema/tests/test_exceptions.py

%files -f %{pyproject_files}
%license COPYING json/LICENSE
%doc README.rst
%{_bindir}/jsonschema

%changelog
%{?autochangelog}
