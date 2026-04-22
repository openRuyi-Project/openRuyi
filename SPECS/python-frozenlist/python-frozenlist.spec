# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname frozenlist

Name:           python-%{srcname}
Version:        1.8.0
Release:        %autorelease
Summary:        List-like structure which can be made immutable
License:        Apache-2.0
URL:            https://github.com/aio-libs/frozenlist
#!RemoteAsset:  sha256:3ede829ed8d842f6cd48fc7081d7a41001a56f1f38603f9d49bf3020d59a31ad
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(expandvars)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
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
