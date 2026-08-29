# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname unicodedata2

Name:           python-%{srcname}
Version:        17.0.1
Release:        %autorelease
Summary:        Unicodedata backport updated to the latest Unicode version
License:        Apache-2.0
URL:            https://github.com/fonttools/unicodedata2
VCS:            git:https://github.com/fonttools/unicodedata2
#!RemoteAsset:  sha256:d79943d153f5f6bfbe3f55a5ec611985184bda37fcedb3ecc75322d82ae6ad3b
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
unicodedata2 is a unicodedata backport updated to the latest Unicode version.

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE

%changelog
%autochangelog
