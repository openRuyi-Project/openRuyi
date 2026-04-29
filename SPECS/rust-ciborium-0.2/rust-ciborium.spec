# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ciborium
%global full_version 0.2.2
%global pkgname ciborium-0.2

Name:           rust-ciborium-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "ciborium"
License:        Apache-2.0
URL:            https://github.com/enarx/ciborium
#!RemoteAsset:  sha256:42e69ffd6f0917f5c029256a24d0161db17cea3997d185db0d35926308770f0e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ciborium-io-0.2/alloc) >= 0.2.2
Requires:       crate(ciborium-io-0.2/default) >= 0.2.2
Requires:       crate(ciborium-ll-0.2/default) >= 0.2.2
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "ciborium"

%package     -n %{name}+std
Summary:        Serde implementation of CBOR using ciborium-basic - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(ciborium-io-0.2/alloc) >= 0.2.2
Requires:       crate(ciborium-io-0.2/std) >= 0.2.2
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-1.0/std) >= 1.0.228
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ciborium crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
