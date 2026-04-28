# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname emoji

Name:           python-%{srcname}
Version:        2.15.0
Release:        %autorelease
Summary:        Emoji library for Python
License:        BSD-3-Clause
URL:            https://github.com/carpedm20/emoji
#!RemoteAsset:  sha256:eae4ab7d86456a70a00a985125a03263a5eac54cd55e51d7e184b1ed3b6757e4
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Full featured simple emoji library for Python. This project was
inspired by kyokomi. The entire set of Emoji codes as defined by the unicode
consortium is supported in addition to a bunch of aliases.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGES.md
%license LICENSE.txt

%changelog
%{?autochangelog}
