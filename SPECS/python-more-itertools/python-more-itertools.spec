# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname more-itertools
%global pypi_name more_itertools

Name:           python-%{srcname}
Version:        11.0.2
Release:        %autorelease
Summary:        More routines for operating on iterables, beyond itertools
License:        MIT
URL:            https://github.com/more-itertools/more-itertools
VCS:            git:https://github.com/more-itertools/more-itertools.git
#!RemoteAsset:  sha256:392a9e1e362cbc106a2457d37cabf9b36e5e12efd4ebff1654630e76597df804
Source:         https://files.pythonhosted.org/packages/source/m/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(flit-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
more-itertools provides additional building blocks, recipes, and routines for
working with Python iterables beyond what the standard itertools module offers.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
