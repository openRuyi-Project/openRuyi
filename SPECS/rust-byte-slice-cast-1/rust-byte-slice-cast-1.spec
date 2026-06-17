# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name byte-slice-cast
%global full_version 1.2.3
%global pkgname byte-slice-cast-1

Name:           rust-byte-slice-cast-1
Version:        1.2.3
Release:        %autorelease
Summary:        Rust crate "byte-slice-cast"
License:        MIT
URL:            https://github.com/sdroege/bytes-num-slice-cast
#!RemoteAsset:  sha256:7575182f7272186991736b70173b0ea045398f984bf5ebbb3804736ce1330c9d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "byte-slice-cast"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
