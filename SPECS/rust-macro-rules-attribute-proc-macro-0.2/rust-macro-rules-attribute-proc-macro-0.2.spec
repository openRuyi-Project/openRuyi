# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name macro_rules_attribute-proc_macro
%global full_version 0.2.2
%global pkgname macro-rules-attribute-proc-macro-0.2

Name:           rust-macro-rules-attribute-proc-macro-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "macro_rules_attribute-proc_macro"
License:        Apache-2.0 OR MIT OR Zlib
URL:            https://github.com/danielhenrymantilla/macro_rules_attribute-rs
#!RemoteAsset:  sha256:670fdfda89751bc4a84ac13eaa63e205cf0fd22b4c9a5fbfa085b63c1f1d3a30
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/verbose-expansions) = %{version}

%description
Source code for takopackized Rust crate "macro_rules_attribute-proc_macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
