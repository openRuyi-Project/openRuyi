# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyroaring

Name:           python-%{srcname}
Version:        1.0.4
Release:        %autorelease
Summary:        Python library for handling efficiently sorted integer sets
License:        MIT
URL:            https://github.com/Ezibenroc/PyRoaringBitMap
#!RemoteAsset:  sha256:99d4217bdfeedc91b82efcec940175a9f9a9137c6476faf7ce5d9c9dd889c8e6
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An efficient and light-weight ordered set of integers.
This is a Python wrapper for the C library CRoaring.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
