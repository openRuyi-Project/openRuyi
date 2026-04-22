# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname dill

Name:           python-%{srcname}
Version:        0.4.1
Release:        %autorelease
Summary:        serialize all of Python
License:        BSD-3-Clause
URL:            https://github.com/uqfoundation/dill
#!RemoteAsset:  sha256:423092df4182177d4d8ba8290c8a5b640c66ab35ec7da59ccfa00f6fa3eea5fa
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Skip import tests
BuildOption(check):  -e "dill.tests.*"
BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
dill extends Python’s pickle module for serializing and de-serializing
Python objects to the majority of the built-in Python types.
Serialization is the process of converting an object to a byte stream,
and the inverse of which is converting a byte stream back to a Python object hierarchy.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/get_gprof
%{_bindir}/get_objgraph
%{_bindir}/undill

%changelog
%autochangelog
