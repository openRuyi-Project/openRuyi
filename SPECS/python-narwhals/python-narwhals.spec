# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname narwhals

Name:           python-%{srcname}
Version:        2.15.0
Release:        %autorelease
Summary:        Extremely lightweight compatibility layer between dataframe libraries
License:        MIT
URL:            https://github.com/narwhals-dev/narwhals
#!RemoteAsset:  sha256:a9585975b99d95084268445a1fdd881311fa26ef1caa18020d959d5b2ff9a965
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Extremely lightweight and extensible compatibility layer between
dataframe libraries!

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
%autochangelog
