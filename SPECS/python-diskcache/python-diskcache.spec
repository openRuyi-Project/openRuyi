# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname diskcache

Name:           python-%{srcname}
Version:        5.6.3
Release:        %autorelease
Summary:        Python disk-backed cache
License:        Apache-2.0
URL:            https://grantjenks.com/docs/diskcache/
#!RemoteAsset:  sha256:2c3a3fa2743d8535d832ec61c2054a1641f41775aa7c556758a109941e33e4fc
Source:         https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
# Tests
BuildRequires:  python3dist(django)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
DiskCache is an Apache2 licensed disk and file backed cache library,
written in pure-Python, and compatible with Django.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
