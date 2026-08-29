# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname compreffor

Name:           python-%{srcname}
Version:        0.6.0
Release:        %autorelease
Summary:        CFF subroutinizer for fontTools
License:        Apache-2.0
URL:            https://github.com/googlefonts/compreffor
VCS:            git:https://github.com/googlefonts/compreffor
#!RemoteAsset:  sha256:7ea034a50c59cc78732f1480040eac2bb36f826ce2eb607c3029b5d38ab11ba8
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(fonttools) >= 4
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-git-ls-files)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
compreffor is a CFF subroutinizer library and CLI for fontTools.

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
