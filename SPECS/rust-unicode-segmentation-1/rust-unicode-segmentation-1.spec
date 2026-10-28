# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-segmentation
%global full_version 1.13.3
%global pkgname unicode-segmentation-1

Name:           rust-unicode-segmentation-1
Version:        1.13.3
Release:        %autorelease
Summary:        Rust crate "unicode-segmentation"
License:        MIT OR Apache-2.0
URL:            https://github.com/unicode-rs/unicode-segmentation
#!RemoteAsset:  sha256:c6f5d3c3b1bf09027a88a6bc961fc00497d651009560b5463668dc81b0fa87a8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}

%description
Source code for takopackized Rust crate "unicode-segmentation"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
