# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-segmentation
%global full_version 1.13.2
%global pkgname unicode-segmentation-1

Name:           rust-unicode-segmentation-1
Version:        1.13.2
Release:        %autorelease
Summary:        Rust crate "unicode-segmentation"
License:        MIT OR Apache-2.0
URL:            https://github.com/unicode-rs/unicode-segmentation
#!RemoteAsset:  sha256:9629274872b2bfaf8d66f5f15725007f635594914870f65218920345aa11aa8c
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
