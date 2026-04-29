# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sip

Name:           python-%{srcname}
Version:        6.15.1
Release:        %autorelease
Summary:        A Python bindings generator for C/C++ libraries
License:        BSD-2-Clause
URL:            https://www.riverbankcomputing.com/software/sip/
VCS:            git:https://github.com/Python-SIP/sip
#!RemoteAsset:  sha256:dc2e58c1798a74e1b31c28e837339822fe8fa55288ae30e8986eb28100ebca5a
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# not support dynamic version.
Patch0:         0001-fix-version.patch

BuildOption(install):  -l sipbuild

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(ply)
BuildRequires:  python3dist(setuptools-scm) >= 8

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SIP is a collection of tools that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt, the Python
bindings for the Qt toolkit, but can be used to create bindings for any C or
C++ library.

SIP v6 comprises a build system (implemented as a PEP 517 backend), a set of
tools, and a runtime module.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/sip-build
%{_bindir}/sip-distinfo
%{_bindir}/sip-install
%{_bindir}/sip-module
%{_bindir}/sip-sdist
%{_bindir}/sip-wheel

%changelog
%autochangelog
