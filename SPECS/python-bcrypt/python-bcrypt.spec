# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname bcrypt

Name:           python-%{srcname}
Version:        5.0.0
Release:        %autorelease
Summary:        Modern password hashing library
License:        Apache-2.0
URL:            https://github.com/pyca/bcrypt
#!RemoteAsset:  sha256:f748f7c2d6fd375cc93d3fba7ef4a9e3a092421b8dbf34d8d4dc06be9492dfdd
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  cargo
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(wheel)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(base64-0.22/default) >= 0.22.1
BuildRequires:  crate(bcrypt-0.17/default) >= 0.17.0
BuildRequires:  crate(bcrypt-pbkdf-0.10/default) >= 0.10.0
BuildRequires:  crate(getrandom-0.3/default) >= 0.3.0
BuildRequires:  crate(pyo3-0.26/abi3) >= 0.26.0
BuildRequires:  crate(pyo3-0.26/default) >= 0.26.0
BuildRequires:  crate(pyo3-0.26/extension-module) >= 0.26.0
BuildRequires:  crate(subtle-2/default) >= 2.6.0

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Bcrypt is a Python module which provides a password hashing method based
on the Blowfish password hashing algorithm, as described in
http://static.usenix.org/events/usenix99/provos.html ("A Future-Adaptable
Password Scheme") by Niels Provos and David Mazieres.

%prep -a
%rust_setup_registry
rm -f src/_bcrypt/Cargo.lock

%generate_buildrequires
%pyproject_buildrequires -x tests

%check -a
%pytest

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
