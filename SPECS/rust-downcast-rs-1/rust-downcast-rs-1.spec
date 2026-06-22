# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name downcast-rs
%global full_version 1.2.1
%global pkgname downcast-rs-1

Name:           rust-downcast-rs-1
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "downcast-rs"
License:        MIT OR Apache-2.0
URL:            https://github.com/marcianx/downcast-rs
#!RemoteAsset:  sha256:75b325c5dbd37f80359721ad39aca5a29fb04c89279657cffdda8736d0c0b9d2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
It supports type parameters, associated types, and type constraints.
Source code for takopackized Rust crate "downcast-rs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
