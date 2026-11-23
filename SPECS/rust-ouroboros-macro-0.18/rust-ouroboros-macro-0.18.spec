# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ouroboros_macro
%global full_version 0.18.5
%global pkgname ouroboros-macro-0.18

Name:           rust-ouroboros-macro-0.18
Version:        0.18.5
Release:        %autorelease
Summary:        Rust crate "ouroboros_macro"
License:        MIT OR Apache-2.0
URL:            https://github.com/someguynamedjosh/ouroboros
#!RemoteAsset:  sha256:3c7028bdd3d43083f6d8d4d5187680d0d3560d54df4cc9d752005268b41e64d0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.4/default) >= 0.4.1
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(proc-macro2-diagnostics-0.10/default) >= 0.10.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ouroboros_macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
