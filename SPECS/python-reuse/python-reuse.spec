# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname reuse

Name:           python-%{srcname}
Version:        6.2.0
Release:        %autorelease
Summary:        A tool for compliance with the REUSE recommendations
License:        Apache-2.0 AND CC0-1.0 AND CC-BY-SA-4.0 AND GPL-3.0-or-later
URL:            https://github.com/fsfe/reuse-tool
#!RemoteAsset:  sha256:4feae057a2334c9a513e6933cdb9be819d8b822f3b5b435a36138bd218897d23
Source:         https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l reuse -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(license-expression)
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(tomlkit)
BuildRequires:  python3dist(python-debian)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A tool for compliance with the REUSE recommendations. Essentially,
it is a linter that checks for a project's compliance, and a compiler that
generates a project's bill of materials.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSES/*.txt
%{_bindir}/reuse

%changelog
%autochangelog
