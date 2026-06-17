# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name image-webp
%global full_version 0.2.4
%global pkgname image-webp-0.2

Name:           rust-image-webp-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "image-webp"
License:        MIT OR Apache-2.0
URL:            https://github.com/image-rs/image-webp
#!RemoteAsset:  sha256:525e9ff3e1a4be2fbea1fdf0e98686a6d98b4d8f937e1bf7402245af1909e8c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-lite-0.1/default) >= 0.1.0
Requires:       crate(quick-error-2/default) >= 2.0.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/benchmarks) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "image-webp"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
