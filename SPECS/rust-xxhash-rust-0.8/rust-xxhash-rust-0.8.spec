# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xxhash-rust
%global full_version 0.8.15
%global pkgname xxhash-rust-0.8

Name:           rust-xxhash-rust-0.8
Version:        0.8.15
Release:        %autorelease
Summary:        Rust crate "xxhash-rust"
License:        BSL-1.0
URL:            https://github.com/DoumanAsh/xxhash-rust
#!RemoteAsset:  sha256:fdd20c5420375476fbd4394763288da7eb0cc0b8c11deed431a91562af7335d3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/const-xxh3) = %{version}
Provides:       crate(%{pkgname}/const-xxh32) = %{version}
Provides:       crate(%{pkgname}/const-xxh64) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/xxh3) = %{version}
Provides:       crate(%{pkgname}/xxh32) = %{version}
Provides:       crate(%{pkgname}/xxh64) = %{version}

%description
Source code for takopackized Rust crate "xxhash-rust"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
