# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clippy
%global full_version 0.0.166
%global pkgname clippy-0.0.166

Name:           rust-clippy-0.0.166
Version:        0.0.166
Release:        %autorelease
Summary:        Rust crate "clippy"
License:        MPL-2.0
URL:            https://github.com/rust-lang-nursery/rust-clippy
#!RemoteAsset:  sha256:86c1e9a7fd08987104fcca0ce1ab0a627006ed955ce14a87ffa32754c947fccb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cargo-metadata-0.2/default) >= 0.2.0
Requires:       crate(clippy-lints-0.0.166/default) >= 0.0.166

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debugging) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clippy"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
