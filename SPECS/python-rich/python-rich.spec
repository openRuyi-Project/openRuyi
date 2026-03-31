# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rich

%bcond tests 0

Name:           python-%{srcname}
Version:        14.2.0
Release:        %autorelease
Summary:        Render rich text and beautiful formatting in the terminal
License:        MIT
URL:            https://github.com/Textualize/rich
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry-core)
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(attrs)
%endif

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output.

%generate_buildrequires
%pyproject_buildrequires

%check
%if %{with tests}
%pytest -vv
%endif

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%{?autochangelog}
