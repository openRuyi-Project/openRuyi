# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linked-hash-map
%global full_version 0.5.6
%global pkgname linked-hash-map-0.5

Name:           rust-linked-hash-map-0.5
Version:        0.5.6
Release:        %autorelease
Summary:        Rust crate "linked-hash-map"
License:        MIT OR Apache-2.0
URL:            https://github.com/contain-rs/linked-hash-map
#!RemoteAsset:  sha256:0717cef1bc8b636c6e1c1bbdefc09e6322da8a9321966e8928ef80d20f7f770f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

# Drop features that depend on unpackaged crates.
Patch2000:      2000-drop-unpackaged-features.patch

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "linked-hash-map"

%package     -n %{name}+serde
Summary:        HashMap wrapper that holds key-value pairs in insertion order - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-impl) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust linked-hash-map crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde_impl" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
