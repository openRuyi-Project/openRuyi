# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-implement
%global full_version 0.60.0
%global pkgname windows-implement-0.60

Name:           rust-windows-implement-0.60
Version:        0.60.0
Release:        %autorelease
Summary:        Rust crate "windows-implement"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:a47fddd13af08290e67f4acabf4b459f647552718f683a7b415d290ac744a836
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0) >= 1.0.0
Requires:       crate(quote-1.0) >= 1.0.0
Requires:       crate(syn-2.0/clone-impls) >= 2.0.0
Requires:       crate(syn-2.0/full) >= 2.0.0
Requires:       crate(syn-2.0/parsing) >= 2.0.0
Requires:       crate(syn-2.0/printing) >= 2.0.0
Requires:       crate(syn-2.0/proc-macro) >= 2.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "windows-implement"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
