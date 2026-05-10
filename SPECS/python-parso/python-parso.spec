# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname parso

Name:           python-%{srcname}
Version:        0.8.7
Release:        %autorelease
Summary:        Python Parser
License:        MIT
URL:            https://github.com/davidhalter/parso
#!RemoteAsset:  sha256:eaaac4c9fdd5e9e8852dc778d2d7405897ec510f2a298071453e5e3a07914bb1
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Parso is a Python parser that supports error recovery and round-trip
parsing for different Python versions (in multiple Python versions). Parso
is also able to list multiple syntax errors in your python file.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
