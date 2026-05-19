# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vt100
%global full_version 0.16.2
%global pkgname vt100-0.16

Name:           rust-vt100-0.16
Version:        0.16.2
Release:        %autorelease
Summary:        Rust crate "vt100"
License:        MIT
URL:            https://github.com/doy/vt100-rust
#!RemoteAsset:  sha256:054ff75fb8fa83e609e685106df4faeffdf3a735d3c74ebce97ec557d5d36fd9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itoa-1.0/default) >= 1.0.15
Requires:       crate(unicode-width-0.2/default) >= 0.2.1
Requires:       crate(vte-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "vt100"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
