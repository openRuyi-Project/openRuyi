# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name miette-derive
%global full_version 5.10.0
%global pkgname miette-derive-5

Name:           rust-miette-derive-5
Version:        5.10.0
Release:        %autorelease
Summary:        Rust crate "miette-derive"
License:        Apache-2.0
URL:            https://github.com/zkat/miette
#!RemoteAsset:  sha256:49e7bc1560b95a3c4a25d03de42fe76ca718ab92d1a22a55b9b4cf67b3ae635c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.11
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Like `thiserror` for Diagnostics.
Source code for takopackized Rust crate "miette-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
