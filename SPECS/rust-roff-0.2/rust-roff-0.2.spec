# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name roff
%global full_version 0.2.2
%global pkgname roff-0.2

Name:           rust-roff-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "roff"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/roff-rs
#!RemoteAsset:  sha256:88f8660c1ff60292143c98d08fc6e2f654d722db50410e3f3797d40baaf9d8f3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "roff"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
