# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zstandard

Name:           python-%{srcname}
Version:        0.25.0
Release:        %autorelease
Summary:        Zstandard bindings for Python
License:        BSD-3-Clause
URL:            https://github.com/indygreg/python-zstandard
#!RemoteAsset:  sha256:7713e1179d162cf5c7906da876ec2ccb9c3a9dcbdffef0cc7f70c3667a205f0b
Source0:        https://files.pythonhosted.org/packages/source/z/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname} +auto
# No module named 'zstandard._cffi'
BuildOption(check):  -e zstandard.backend_cffi

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(libzstd)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This project provides Python bindings for interfacing with
the Zstandard compression library.  A C extension and CFFI
interface are provided.

%generate_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE zstd/COPYING

%changelog
%autochangelog
