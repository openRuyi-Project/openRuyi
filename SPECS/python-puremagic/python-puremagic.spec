# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname puremagic

Name:           python-%{srcname}
Version:        1.30
Release:        %autorelease
Summary:        Pure python implementation of magic file detection
License:        MIT
URL:            https://github.com/cdgriffith/puremagic
#!RemoteAsset:  sha256:f9ff7ac157d54e9cf3bff1addfd97233548e75e685282d84ae11e7ffee1614c9
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Pure Python module that will identify a file based on its magic numbers.
It does NOT try to match files on non-magic string.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.md README.rst
%license LICENSE

%changelog
%autochangelog
