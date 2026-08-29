# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xml5ever
%global full_version 0.35.0
%global pkgname xml5ever-0.35

Name:           rust-xml5ever-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "xml5ever"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/html5ever/blob/main/xml5ever/README.md
#!RemoteAsset:  sha256:ee3f1e41afb31a75aef076563b0ad3ecc24f5bd9d12a72b132222664eb76b494
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(markup5ever-0.35/default) >= 0.35.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/trace-tokenizer) = %{version}

%description
Source code for takopackized Rust crate "xml5ever"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
