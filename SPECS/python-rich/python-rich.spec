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
#!RemoteAsset:  sha256:73ff50c7c0c1c77c8243079283f4edb376f0f6442433aecb8ce7e6d0b92d1fe4
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

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output.

%generate_buildrequires
%pyproject_buildrequires

%if %{with tests}
%check -a
%pytest -vv
%endif

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
