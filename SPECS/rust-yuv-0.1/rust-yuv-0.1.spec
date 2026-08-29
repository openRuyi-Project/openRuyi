# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yuv
%global full_version 0.1.10
%global pkgname yuv-0.1

Name:           rust-yuv-0.1
Version:        0.1.10
Release:        %autorelease
Summary:        Rust crate "yuv"
License:        BSD-2-Clause
URL:            https://lib.rs/crates/yuv
#!RemoteAsset:  sha256:adb00ec278d3f05b635a766c22205efb5825592d93c955c8021e1dfe21de5a6d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(rgb-0.8) >= 0.8.52

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "yuv"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
