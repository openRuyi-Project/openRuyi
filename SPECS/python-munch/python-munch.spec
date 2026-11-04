# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname munch

Name:           python-%{srcname}
Version:        4.0.0
Release:        %autorelease
Summary:        Python dictionaries with attribute access
License:        MIT
URL:            https://github.com/Infinidat/munch
#!RemoteAsset:  sha256:542cb151461263216a4e37c3fd9afc425feeaf38aaa3025cd2a981fadb422235
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Adapt the reserved-attribute assertions to Python 3.13 class metadata.
Patch2000:      2000-tests-accept-python-class-metadata.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Munch provides dictionaries whose keys can also be accessed as attributes.
It can convert nested dictionaries to and from this representation.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Exercise dictionary access and nested conversion using upstream's core tests.
%pytest tests/test_munch.py

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
