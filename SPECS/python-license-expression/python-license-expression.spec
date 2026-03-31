# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

%global pypi_name license_expression
%global srcname license-expression

Name:           python-%{srcname}
Version:        30.4.4
Release:        %autorelease
Summary:        Library to parse, compare, simplify and normalize license expressions
License:        Apache-2.0
URL:            https://github.com/nexB/license-expression
#!RemoteAsset
Source:         https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
# for tests.
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(boolean-py)
%if %{with doc}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinxcontrib-apidoc)
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This module defines a mini language to parse, validate, simplify, normalize and
compare license expressions using a boolean logic engine.

It supports SPDX license expressions and also accepts other license naming
conventions and license identifiers aliases to resolve and normalize licenses.

%if %{with doc}
%package        doc
Summary:        Documentation for python-license-expression
License:        Apache-2.0 AND BSD-2-Clause AND MIT
BuildArch:      noarch
Requires:       python3-license-expression = %{version}-%{release}

%description    doc
Documentation for license-expression.
%endif

%prep -a
%if %{with doc}
sed -i '/sphinx_reredirects/d' setup.cfg
sed -i '/sphinx_reredirects/d' docs/source/conf.py
sed -i '/sphinx_rtd_dark_mode/d' docs/source/conf.py
sed -i '/sphinx_copybutton/d' docs/source/conf.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%if %{with doc}
%install -a
sphinx-build-3 -b html docs/source html
rm -rf html/.{doctrees,buildinfo}
%endif

%files -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CODE_OF_CONDUCT.rst README.rst
%license apache-2.0.LICENSE

%if %{with doc}
%files doc
%doc html
%endif

%changelog
%{?autochangelog}
