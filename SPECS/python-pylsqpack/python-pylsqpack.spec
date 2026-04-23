# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pylsqpack

Name:           python-%{srcname}
Version:        0.3.23
Release:        %autorelease
Summary:        pylsqpack is a wrapper around the ls-qpack library
License:        BSD-3-Clause
URL:            https://github.com/aiortc/pylsqpack
#!RemoteAsset:  sha256:f55b126940d8b3157331f123d4428d703a698a6db65a6a7891f7ec1b90c86c56
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python wrapper for the ls-qpack QPACK library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
