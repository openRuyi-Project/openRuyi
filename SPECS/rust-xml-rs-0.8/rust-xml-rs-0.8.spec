# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xml-rs
%global full_version 0.8.28
%global pkgname xml-rs-0.8

Name:           rust-xml-rs-0.8
Version:        0.8.28
Release:        %autorelease
Summary:        Rust crate "xml-rs"
License:        MIT
URL:            https://lib.rs/crates/xml
#!RemoteAsset:  sha256:3ae8337f8a065cfc972643663ea4279e04e7256de865aa66fe25cec5fb912d3f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "xml-rs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
