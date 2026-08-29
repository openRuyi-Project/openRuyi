# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cookiecutter

Name:           python-%{srcname}
Version:        2.7.1
Release:        %autorelease
Summary:        CLI utility to create projects from templates
License:        BSD-3-Clause
URL:            https://github.com/cookiecutter/cookiecutter
#!RemoteAsset:  sha256:ca7bb7bc8c6ff441fbf53921b5537668000e38d56e28d763a1b73975c66c6138
Source:         https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(arrow)
BuildRequires:  python3dist(binaryornot)
BuildRequires:  python3dist(python-slugify)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(rich)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       pythondist(binaryornot)
Requires:       python3dist(click)
Requires:       python3dist(jinja2)
Requires:       python3dist(pyyaml)
Requires:       python3dist(requests)
Requires:       python3dist(slugify)
Requires:       python3dist(arrow)

%description
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

%prep -a
# no setup.py
cat <<EOF >> pyproject.toml

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
EOF

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/%{srcname}

%changelog
%autochangelog
