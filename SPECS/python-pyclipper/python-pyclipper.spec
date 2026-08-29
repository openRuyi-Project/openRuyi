# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyclipper

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        Cython wrapper for the Clipper library
License:        MIT
URL:            https://github.com/fonttools/pyclipper
VCS:            git:https://github.com/fonttools/pyclipper
#!RemoteAsset:  sha256:9882bd889f27da78add4dd6f881d25697efc740bf840274e749988d25496c8e1
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pyclipper is a Cython wrapper for the Clipper polygon clipping library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE*

%changelog
%autochangelog
