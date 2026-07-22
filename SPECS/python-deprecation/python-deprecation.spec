# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname deprecation

Name:           python-%{srcname}
Version:        2.1.0
Release:        %autorelease
Summary:        Library to handle automated deprecations
License:        Apache-2.0
URL:            https://github.com/briancurtin/deprecation
#!RemoteAsset:  sha256:72b3bde64e5d778694b0cf68178aed03d15e15477116add3fb773e581f9518ff
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l deprecation

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Deprecation is a library that enables automated deprecation messages.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
