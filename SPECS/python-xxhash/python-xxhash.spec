# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname xxhash

Name:           python-%{srcname}
Version:        3.6.0
Release:        %autorelease
Summary:        Python binding for xxHash
License:        BSD-3-Clause
URL:            https://github.com/ifduyue/python-xxhash
VCS:            git:https://github.com/ifduyue/python-xxhash
#!RemoteAsset:  sha256:f0162a78b13a0d7617b2845b90c763339d1f1d82bb04a4b07f4ab535cc5e05d6
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(libxxhash)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
xxhash provides Python bindings for the xxHash family of extremely fast
non-cryptographic hash algorithms.

%generate_buildrequires
%pyproject_buildrequires

%build -p
export XXHASH_LINK_SO=1

%files -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license LICENSE

%changelog
%autochangelog
