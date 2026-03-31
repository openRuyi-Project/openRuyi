# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gitdb

Name:           python-%{srcname}
Version:        4.0.11
Release:        %autorelease
Summary:        Git Object Database
License:        BSD-3-Clause
URL:            https://github.com/gitpython-developers/gitdb
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(smmap)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
GitDB allows you to access bare git repositories for reading and writing.
It aims at allowing full access to loose objects as well as packs with
performance and scalability in mind. It operates exclusively on streams,
allowing to handle large objects with a small memory footprint.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%{?autochangelog}
