# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cysqlite

Name:           python-%{srcname}
Version:        0.3.0
Release:        %autorelease
Summary:        SQLite3 binding for Python
License:        MIT
URL:            https://github.com/coleifer/cysqlite
#!RemoteAsset:  sha256:aaac2707c2ec96e75af7b48cc72914f0db235ed2793155b5339aaab7ec5b9320
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
cysqlite is a SQLite3 binding for Python using Cython for performance.

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
