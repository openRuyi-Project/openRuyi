# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ijson

Name:           python-%{srcname}
Version:        3.5.0
Release:        %autorelease
Summary:        Iterative JSON parser with standard Python iterator interfaces
License:        BSD-3-Clause
URL:            https://github.com/ICRAR/ijson
#!RemoteAsset:  sha256:94688760720e3f5212731b3cb8d30267f9a045fb38fb3870254e7b9504246f31
Source:         https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# skip some import check.
BuildOption(check):  -e ijson.backends.yajl
BuildOption(check):  -e ijson.backends.yajl2
BuildOption(check):  -e ijson.backends.yajl2_c
BuildOption(check):  -e ijson.backends.yajl2_cffi

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Iterative JSON parser with standard Python iterator interfaces.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
