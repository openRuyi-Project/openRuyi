# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio_with_wasm_proc
%global full_version 0.8.8
%global pkgname tokio-with-wasm-proc-0.8

Name:           rust-tokio-with-wasm-proc-0.8
Version:        0.8.8
Release:        %autorelease
Summary:        Rust crate "tokio_with_wasm_proc"
License:        MIT
URL:            https://github.com/cunarist/tokio-with-wasm
#!RemoteAsset:  sha256:d01145a2c788d6aae4cd653afec1e8332534d7d783d01897cefcafe4428de992
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1/default) >= 1.0.37
Requires:       crate(syn-2/default) >= 2.0.77
Requires:       crate(syn-2/full) >= 2.0.77

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio_with_wasm_proc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
