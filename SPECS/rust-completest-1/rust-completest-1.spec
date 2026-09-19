# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name completest
%global full_version 1.1.0
%global pkgname completest-1

Name:           rust-completest-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "completest"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/completest
#!RemoteAsset:  sha256:dea8f71e372b5a4f9a52c6365e0731b1ff34c3e6068ae64422412a8f45ab898e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "completest"

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
