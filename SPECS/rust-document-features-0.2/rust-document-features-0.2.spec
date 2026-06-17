# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name document-features
%global full_version 0.2.12
%global pkgname document-features-0.2

Name:           rust-document-features-0.2
Version:        0.2.12
Release:        %autorelease
Summary:        Rust crate "document-features"
License:        MIT OR Apache-2.0
URL:            https://slint.rs
#!RemoteAsset:  sha256:d4b8a88685455ed29a21542a33abd9cb6510b6b129abadabdcef0f4c55bc8f61
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(litrs-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/self-test) = %{version}

%description
Source code for takopackized Rust crate "document-features"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
