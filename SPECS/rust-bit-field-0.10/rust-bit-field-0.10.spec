# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bit_field
%global full_version 0.10.3
%global pkgname bit-field-0.10

Name:           rust-bit-field-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "bit_field"
License:        Apache-2.0 OR MIT
URL:            https://github.com/phil-opp/rust-bit-field
#!RemoteAsset:  sha256:1e4b40c7323adcfc0a41c4b88143ed58346ff65a288fc144329c5c45e05d70c6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bit_field"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
