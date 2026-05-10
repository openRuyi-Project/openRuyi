# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname beniget

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        Scientific Tools for Python
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/beniget/
#!RemoteAsset:  sha256:e7af11fa8ec7de3d3eb3d98b1e722d15d44017d8b35d8aa11d54f6719b312f22
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(gast)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Beniget provides a static over-approximation of the global and local definitions inside Python Module/Class/Function. It can also compute def-use chains from each definition.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
