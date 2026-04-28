# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname soxr

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        High quality, one-dimensional sample-rate conversion library for Python.
License:        LGPL-2.1
URL:            https://github.com/dofuuz/python-soxr
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python-SoXR is a Python wrapper of libsoxr.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
