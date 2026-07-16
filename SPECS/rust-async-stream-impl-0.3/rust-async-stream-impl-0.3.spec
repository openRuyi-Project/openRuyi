# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-stream-impl
%global full_version 0.3.6
%global pkgname async-stream-impl-0.3

Name:           rust-async-stream-impl-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "async-stream-impl"
License:        MIT
URL:            https://github.com/tokio-rs/async-stream
#!RemoteAsset:  sha256:c7c24de15d275a1ecfd47a380fb4d5ec9bfe0933f309ed5e705b775596a3574d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.60
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.2
Requires:       crate(syn-2/full) >= 2.0.2
Requires:       crate(syn-2/visit-mut) >= 2.0.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-stream-impl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
