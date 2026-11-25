# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name logos-codegen
%global full_version 0.15.1
%global pkgname logos-codegen-0.15

Name:           rust-logos-codegen-0.15
Version:        0.15.1
Release:        %autorelease
Summary:        Rust crate "logos-codegen"
License:        MIT OR Apache-2.0
URL:            https://logos.maciej.codes/
#!RemoteAsset:  sha256:192a3a2b90b0c05b27a0b2c43eecdb7c415e29243acc3f89cc8247a5b693045c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(beef-0.5/default) >= 0.5.0
Requires:       crate(fnv-1/default) >= 1.0.6
Requires:       crate(lazy-static-1/default) >= 1.4.0
Requires:       crate(proc-macro2-1/default) >= 1.0.9
Requires:       crate(quote-1/default) >= 1.0.3
Requires:       crate(regex-syntax-0.8/default) >= 0.8.2
Requires:       crate(rustc-version-0.4) >= 0.4.1
Requires:       crate(syn-2/default) >= 2.0.13
Requires:       crate(syn-2/full) >= 2.0.13

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/forbid-unsafe) = %{version}
Provides:       crate(%{pkgname}/fuzzing) = %{version}

%description
Source code for takopackized Rust crate "logos-codegen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
