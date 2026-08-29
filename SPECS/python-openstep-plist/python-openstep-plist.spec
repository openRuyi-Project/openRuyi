# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname openstep-plist

Name:           python-%{srcname}
Version:        0.5.2
Release:        %autorelease
Summary:        ASCII plist parser written in Cython
License:        MIT
URL:            https://github.com/fonttools/openstep-plist
VCS:            git:https://github.com/fonttools/openstep-plist
#!RemoteAsset:  sha256:2a0d70ff7a03cce64a727062b64bb2f5c9af9fd4a636aaa4339b6aaa2cf65195
Source0:        https://files.pythonhosted.org/packages/source/o/openstep_plist/openstep_plist-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l openstep_plist +auto

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython) >= 0.28.5
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
openstep-plist is an ASCII plist parser written in Cython.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
