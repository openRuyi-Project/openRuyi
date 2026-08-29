# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cbor2

Name:           python-%{srcname}
Version:        6.1.2
Release:        %autorelease
Summary:        CBOR encoder and decoder for Python
License:        MIT
URL:            https://github.com/agronholm/cbor2
#!RemoteAsset:  sha256:6b43037a66947dee5af0abb1a4c3a13b3abac5a4a3f32f9771efbbcd030fd909
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Pin wildcard Rust dependency to the lock-selected 0.4 provider for RPM
# capability consistency.
Patch2000:      2000-pin-num-bigint-rust-dependency.patch

BuildOption(install):  -l %{srcname} -L

BuildRequires:  cargo
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(bigdecimal-0.4/default) >= 0.4.10
BuildRequires:  crate(half-2/default) >= 2.7.1
BuildRequires:  crate(num-bigint-0.4/default) >= 0.4.6
BuildRequires:  crate(pyo3-0.28/default) >= 0.28.0
BuildRequires:  crate(pyo3-0.28/bigdecimal) >= 0.28.0
BuildRequires:  crate(pyo3-0.28/extension-module) >= 0.28.0
BuildRequires:  crate(pyo3-0.28/num-bigint) >= 0.28.0
BuildRequires:  crate(pyo3-build-config-0.28/resolve-config) >= 0.28.2

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
cbor2 provides a CBOR encoder and decoder for Python, including a Rust-backed
extension module for performance.

%prep -a
%rust_setup_registry
rm -f rust/Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/cbor2

%changelog
%autochangelog
