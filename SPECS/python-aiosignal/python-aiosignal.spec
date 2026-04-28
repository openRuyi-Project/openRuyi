# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aiosignal

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        List of registered asynchronous callbacks
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiosignal
#!RemoteAsset:  sha256:f47eecd9468083c2029cc99945502cb7708b082c232f9aca65da147157b251c7
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(frozenlist)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
FrozenList is a list-like structure which implements
collections.abc.MutableSequence, and which can be made immutable.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
%autochangelog
