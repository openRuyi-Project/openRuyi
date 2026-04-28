# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname yarl

Name:           python-%{srcname}
Version:        1.22.0
Release:        %autorelease
Summary:        Python module to handle URLs
License:        Apache-2.0
URL:            https://github.com/aio-libs/yarl
#!RemoteAsset:  sha256:bebf8557577d4401ba8bd9ff33906f1376c877aa78d1fe216ad01b4d6745af71
Source0:        https://files.pythonhosted.org/packages/source/y/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(expandvars)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(idna)
BuildRequires:  python3dist(multidict)
BuildRequires:  python3dist(propcache)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The module provides handy URL class for URL parsing and changing.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
%autochangelog
