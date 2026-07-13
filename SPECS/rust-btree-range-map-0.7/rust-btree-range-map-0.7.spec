# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name btree-range-map
%global full_version 0.7.2
%global pkgname btree-range-map-0.7

Name:           rust-btree-range-map-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "btree-range-map"
License:        MIT OR Apache-2.0
URL:            https://github.com/timothee-haudebourg/btree-range-map
#!RemoteAsset:  sha256:1be5c9672446d3800bcbcaabaeba121fe22f1fb25700c4562b22faf76d377c33
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(btree-slab-0.6/default) >= 0.6.0
Requires:       crate(cc-traits-2/default) >= 2.0.0
Requires:       crate(range-traits-0.3/default) >= 0.3.0
Requires:       crate(slab-0.4/default) >= 0.4.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "btree-range-map"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
