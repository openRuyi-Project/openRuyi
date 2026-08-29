# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pandas

Name:           python-%{srcname}
Version:        3.0.1
Release:        %autorelease
Summary:        Python data structures for data analysis, time series, and statistics
License:        BSD-3-Clause
URL:            https://pandas.pydata.org/
#!RemoteAsset:  sha256:4186a699674af418f655dbd420ed87f50d56b4cd6603784279d9eef6627823c8
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# PyArrow is optional.
# TODO: Add python-pyarrow.
BuildOption(check):  -e pandas.core.arrays.arrow.extension_types
# Numba is optional.
# TODO: Add python-numba.
# Skip import checks for all tests
BuildOption(check):  -e 'pandas.tests.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(jinja2)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Pandas is a Python package providing data structures designed for
working with structured (tabular, multidimensional, potentially
heterogeneous) and time series data. It is a high-level building
block for doing data analysis in Python.

%generate_buildrequires
%pyproject_buildrequires -p

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
