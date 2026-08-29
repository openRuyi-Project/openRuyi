# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname blake3

Name:           python-%{srcname}
Version:        1.0.8
Release:        %autorelease
Summary:        Python bindings for the Rust blake3 crate
License:        CC0-1.0 OR Apache-2.0
URL:            https://github.com/oconnor663/blake3-py
#!RemoteAsset:  sha256:513cc7f0f5a7c035812604c2c852a0c1468311345573de647e310aca4ab165ba
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  cargo
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(maturin)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros

BuildRequires:  crate(blake3-1/default) >= 1.5.5
BuildRequires:  crate(blake3-1/mmap) >= 1.5.5
BuildRequires:  crate(blake3-1/rayon) >= 1.5.5
BuildRequires:  crate(hex-0.4/default) >= 0.4.3
BuildRequires:  crate(pyo3-0.26/default) >= 0.26.0
BuildRequires:  crate(pyo3-0.26/extension-module) >= 0.26.0
BuildRequires:  crate(rayon-1/default) >= 1.11.0

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
blake3 provides Python bindings for the BLAKE3 cryptographic hash function,
backed by the official Rust implementation.

%prep -a
%rust_setup_registry
rm -f Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
