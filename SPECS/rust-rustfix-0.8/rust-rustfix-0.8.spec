# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustfix
%global full_version 0.8.7
%global pkgname rustfix-0.8

Name:           rust-rustfix-0.8
Version:        0.8.7
Release:        %autorelease
Summary:        Rust crate "rustfix"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:82fa69b198d894d84e23afde8e9ab2af4400b2cba20d6bf2b428a8b01c222c5a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.204
Requires:       crate(serde-1/derive) >= 1.0.204
Requires:       crate(serde-json-1/default) >= 1.0.120
Requires:       crate(thiserror-1/default) >= 1.0.63
Requires:       crate(tracing-0.1/std) >= 0.1.40
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rustfix"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
