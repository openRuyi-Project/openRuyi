# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname linkify-it-py

Name:           python-%{srcname}
Version:        2.0.3
Release:        %autorelease
Summary:        Link recognition library with full Unicode support
License:        MIT
URL:            https://github.com/tsutsu3/linkify-it-py
#!RemoteAsset:  sha256:68cda27e162e9215c17d786649d1da0021a451bdc436ef9e0fa0ba5234b9b048
Source:         https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l linkify_it

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(uc-micro-py)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is a Python port of linkify-it, a link recognition library with FULL
unicode support. It is focused on high quality link pattern detection in
plain text.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -v

%files -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md README.md

%changelog
%autochangelog
