# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname html5lib
# skip tests as we don't have pytest-expect yet.
%bcond tests 0

Name:           python-%{srcname}
Version:        1.1
Release:        %autorelease
Summary:        A python based HTML parser/tokenizer
License:        MIT
URL:            https://github.com/html5lib/html5lib-python
#!RemoteAsset
Source:         https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(six) >= 1.9
BuildRequires:  python3dist(webencodings)
%if %{with tests}
# for tests
BuildRequires:  python3(pytest)
BuildRequires:  python3(pytest-expect)
%endif

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A python based HTML parser/tokenizer based on the WHATWG HTML5
specification for maximum compatibility with major desktop web browsers.

%generate_buildrequires
%pyproject_buildrequires

%check
%if %{with tests}
%pytest
%endif

%files -f %{pyproject_files}
%doc CHANGES.rst README.rst
%license LICENSE

%changelog
%{?autochangelog}
