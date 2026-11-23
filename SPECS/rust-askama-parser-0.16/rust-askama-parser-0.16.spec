# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name askama_parser
%global full_version 0.16.1
%global pkgname askama-parser-0.16

Name:           rust-askama-parser-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "askama_parser"
License:        MIT OR Apache-2.0
URL:            https://askama.rs/
#!RemoteAsset:  sha256:2c5ae75772275d268b03ab8bdccdd12117b6169ee23256942b34e46c9f476583
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustc-hash-2/default) >= 2.0.0
Requires:       crate(unicode-ident-1/default) >= 1.0.12
Requires:       crate(winnow-1/default) >= 1.0.0
Requires:       crate(winnow-1/simd) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "askama_parser"

%package     -n %{name}+config
Summary:        Parser for Askama templates - feature "config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/config) = %{version}

%description -n %{name}+config
This metapackage enables feature "config" for the Rust askama_parser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
