# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yaml-rust
%global full_version 0.4.5
%global pkgname yaml-rust-0.4

Name:           rust-yaml-rust-0.4
Version:        0.4.5
Release:        %autorelease
Summary:        Rust crate "yaml-rust"
License:        MIT OR Apache-2.0
URL:            http://chyh1990.github.io/yaml-rust/
#!RemoteAsset:  sha256:56c1936c4cc7a1c9ab21a1ebb602eb942ba868cbd44a99cb7cdc5892335e1c85
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(linked-hash-map-0.5/default) >= 0.5.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "yaml-rust"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
