# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name leb128
%global full_version 0.2.7
%global pkgname leb128-0.2

Name:           rust-leb128-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "leb128"
License:        MIT OR Apache-2.0
URL:            https://github.com/gimli-rs/leb128
#!RemoteAsset:  sha256:c83bff1d572d6b9aeef67ddfc8448e4a3737909cb28e81f97c791b9018703e52
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "leb128"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
