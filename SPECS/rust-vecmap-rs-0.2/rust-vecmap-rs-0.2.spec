# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vecmap-rs
%global full_version 0.2.4
%global pkgname vecmap-rs-0.2

Name:           rust-vecmap-rs-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "vecmap-rs"
License:        MIT OR Apache-2.0
URL:            https://github.com/martinohmann/vecmap-rs
#!RemoteAsset:  sha256:f9758649b51083aa8008666f41c23f05abca1766aad4cc447b195dd83ef1297b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vecmap-rs"

%package     -n %{name}+serde
Summary:        Vector-based map and set implementation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust vecmap-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
