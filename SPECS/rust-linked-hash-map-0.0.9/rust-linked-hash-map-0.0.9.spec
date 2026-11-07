# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linked-hash-map
%global full_version 0.0.9
%global pkgname linked-hash-map-0.0.9

Name:           rust-linked-hash-map-0.0.9
Version:        0.0.9
Release:        %autorelease
Summary:        Rust crate "linked-hash-map"
License:        MIT OR Apache-2.0
URL:            https://github.com/contain-rs/linked-hash-map
#!RemoteAsset:  sha256:83f7ff3baae999fdf921cccf54b61842bb3b26868d50d02dff48052ebec8dd79
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "linked-hash-map"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
