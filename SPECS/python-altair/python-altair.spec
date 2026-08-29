# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname altair

Name:           python-%{srcname}
Version:        6.1.0
Release:        %autorelease
Summary:        Declarative statistical visualization library for Python
License:        BSD-3-Clause
URL:            https://github.com/vega/altair
#!RemoteAsset:  sha256:dda699216cf85b040d968ae5a569ad45957616811e38760a85e5118269daca67
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(narwhals)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Altair is a declarative statistical visualization library for Python, based on
Vega and Vega-Lite.

%generate_buildrequires
%pyproject_buildrequires

%check
# skip tests as some deps we don't have yet.

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
