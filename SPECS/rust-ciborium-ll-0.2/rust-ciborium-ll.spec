# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ciborium-ll
%global full_version 0.2.2
%global pkgname ciborium-ll-0.2

Name:           rust-ciborium-ll-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "ciborium-ll"
License:        Apache-2.0
URL:            https://github.com/enarx/ciborium
#!RemoteAsset:  sha256:57663b653d948a338bfb3eeba9bb2fd5fcfaecb9e199e87e1eda4d9e8b240fd9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ciborium-io-0.2/default) >= 0.2.2
Requires:       crate(half-2.0) >= 2.7.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "ciborium-ll"

%package     -n %{name}+std
Summary:        Low-level CBOR codec primitives - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(half-2.0/std) >= 2.7.1
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ciborium-ll crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
