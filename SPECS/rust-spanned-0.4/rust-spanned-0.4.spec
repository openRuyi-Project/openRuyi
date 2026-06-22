# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name spanned
%global full_version 0.4.1
%global pkgname spanned-0.4

Name:           rust-spanned-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "spanned"
License:        MIT OR Apache-2.0
URL:            FIXME
#!RemoteAsset:  sha256:c92d4b0c055fde758f086eb4a6e73410247df8a3837fd606d2caeeaf72aa566d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.98
Requires:       crate(bstr-1/default) >= 1.6.0
Requires:       crate(color-eyre-0.6/default) >= 0.6.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "spanned"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
