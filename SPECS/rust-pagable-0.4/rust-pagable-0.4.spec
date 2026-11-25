# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pagable
%global full_version 0.4.2
%global pkgname pagable-0.4

Name:           rust-pagable-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "pagable"
License:        Apache-2.0
URL:            https://github.com/facebook/starlark-rust
#!RemoteAsset:  sha256:f2b6c3024f51bd32fc2fbadedb27783151515348f24cdf2e0ad83270b844f449
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(allocative-0.3/default) >= 0.3.6
Requires:       crate(anyhow-1/default) >= 1.0.102
Requires:       crate(async-trait-0.1/default) >= 0.1.86
Requires:       crate(blake3-1/default) >= 1.8.0
Requires:       crate(blake3-1/rayon) >= 1.8.0
Requires:       crate(blake3-1/std) >= 1.8.0
Requires:       crate(blake3-1/traits-preview) >= 1.8.0
Requires:       crate(bytemuck-1/const-zeroed) >= 1.25.0
Requires:       crate(bytemuck-1/default) >= 1.25.0
Requires:       crate(bytemuck-1/derive) >= 1.25.0
Requires:       crate(bytemuck-1/min-const-generics) >= 1.25.0
Requires:       crate(bytemuck-1/must-cast) >= 1.25.0
Requires:       crate(bytemuck-1/nightly-stdsimd) >= 1.25.0
Requires:       crate(dashmap-6/default) >= 6.1.0
Requires:       crate(dupe-0.9/default) >= 0.9.1
Requires:       crate(either-1/default) >= 1.8.0
Requires:       crate(erased-serde-0.4/default) >= 0.4.10
Requires:       crate(fancy-regex-0.16/default) >= 0.16.2
Requires:       crate(indexmap-2/default) >= 2.14.0
Requires:       crate(indexmap-2/serde) >= 2.14.0
Requires:       crate(inventory-0.3/default) >= 0.3.24
Requires:       crate(num-bigint-0.4/default) >= 0.4.6
Requires:       crate(num-bigint-0.4/serde) >= 0.4.6
Requires:       crate(once-cell-1/default) >= 1.21.4
Requires:       crate(pagable-derive-0.4/default) >= 0.4.2
Requires:       crate(parking-lot-0.12/default) >= 0.12.1
Requires:       crate(parking-lot-0.12/send-guard) >= 0.12.1
Requires:       crate(postcard-1/default) >= 1.0.8
Requires:       crate(postcard-1/use-crc) >= 1.0.8
Requires:       crate(postcard-1/use-std) >= 1.0.8
Requires:       crate(regex-1/default) >= 1.12.3
Requires:       crate(sequence-trie-0.3/default) >= 0.3.6
Requires:       crate(serde-1/default) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(serde-1/rc) >= 1.0.219
Requires:       crate(serde-json-1/default) >= 1.0.140
Requires:       crate(serde-json-1/raw-value) >= 1.0.140
Requires:       crate(smallvec-1/const-generics) >= 1.15.0
Requires:       crate(smallvec-1/default) >= 1.15.0
Requires:       crate(sorted-vector-map-0.2/default) >= 0.2.0
Requires:       crate(static-assertions-1/default) >= 1.1.0
Requires:       crate(static-interner-0.1/default) >= 0.1.2
Requires:       crate(strong-hash-0.1/default) >= 0.1.0
Requires:       crate(take-mut-0.2/default) >= 0.2.0
Requires:       crate(triomphe-0.1/default) >= 0.1.11

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pagable"

%package     -n %{name}+tokio
Summary:        Serialization framework with content-addressed `Arc` deduplication and runtime polymorphism via typetag - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.52.1
Requires:       crate(tokio-1/full) >= 1.52.1
Requires:       crate(tokio-1/test-util) >= 1.52.1
Requires:       crate(tokio-1/tracing) >= 1.52.1
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust pagable crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
