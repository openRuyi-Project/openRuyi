# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname lmdb

Name:           python-%{srcname}
Version:        2.2.0
Release:        %autorelease
Summary:        Universal Python binding for the LMDB Lightning Database
License:        OLDAP-2.8
URL:            https://github.com/jnwatson/py-lmdb
#!RemoteAsset:  sha256:53020e20305c043ea6e68089bc242d744fba6073cdb268332299ba6dda2886d4
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(patch-ng)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
python-lmdb is a universal Python binding for the LMDB 'Lightning' Database.
LMDB is a tiny, lightning-fast embedded key-value store.

%generate_buildrequires
%pyproject_buildrequires

%files
%doc README.md
%license LICENSE
%{python3_sitearch}/lmdb/
%{python3_sitearch}/lmdb-*.dist-info/

%changelog
%autochangelog
