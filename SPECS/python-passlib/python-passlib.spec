# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname passlib

Name:           python-%{srcname}
Version:        1.7.4
Release:        %autorelease
Summary:        Comprehensive password hashing framework supporting over 20 schemes
License:        BSD-3-Clause AND Beerware AND UnixCrypt AND ISC
URL:            https://foss.heptapod.net/python-libs/passlib
#!RemoteAsset:  sha256:defd50f72b65c5402ab2c573830a6978e5f202ad0d984793c8dde2c4152ebe04
Source:         https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L
BuildOption(check):  -e passlib.ext.django.models

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README
%license LICENSE

%changelog
%autochangelog
