# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytzdata

Name:           python-%{srcname}
Version:        2020.1
Release:        %autorelease
Summary:        Better dates and times for Python
License:        Apache-2.0
URL:            https://github.com/sdispater/pytzdata
#!RemoteAsset:  sha256:3efa13b335a00a8de1d345ae41ec78dd11c9f8807f522d39850f2dd828681540
Source:         https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# just remove the deps.
Patch0:         0001-remove-poetry-dep.patch

BuildOption(install):  -l %{srcname} -L
# skip the import check
BuildOption(check):  -e pytzdata.commands.app
BuildOption(check):  -e pytzdata.commands.make
BuildOption(check):  -e pytzdata.commands.zones

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(setuptools)
BuildRequires:  tzdata

Requires:       tzdata

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The Olson timezone database for Python. This package contains the python
bindings to the database provided by the system tzdata package.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
