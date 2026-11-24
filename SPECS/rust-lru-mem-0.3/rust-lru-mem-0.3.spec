# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lru-mem
%global full_version 0.3.0
%global pkgname lru-mem-0.3

Name:           rust-lru-mem-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "lru-mem"
License:        MIT OR Apache-2.0
URL:            https://github.com/florian1345/lru-mem
#!RemoteAsset:  sha256:cf5c8c26d903a41c80d4cc171940a57a4d1bc51139ebd6aad87e2f9ae3774780
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.14/default) >= 0.14.0
Requires:       crate(hashbrown-0.14/raw) >= 0.14.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lru-mem"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
