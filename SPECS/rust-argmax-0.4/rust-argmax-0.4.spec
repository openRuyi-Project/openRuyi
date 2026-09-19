# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name argmax
%global full_version 0.4.0
%global pkgname argmax-0.4

Name:           rust-argmax-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "argmax"
License:        MIT OR Apache-2.0
URL:            https://github.com/sharkdp/argmax
#!RemoteAsset:  sha256:0144c58b55af0133ec3963ce5e4d07aad866e3bbcfdcddbf4590dbd7ad6ff557
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.127
Requires:       crate(nix-0.30/feature) >= 0.30.1
Requires:       crate(once-cell-1/default) >= 1.17.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "argmax"

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
