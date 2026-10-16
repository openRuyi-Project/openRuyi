# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-xid
%global full_version 0.1.0
%global pkgname unicode-xid-0.1

Name:           rust-unicode-xid-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "unicode-xid"
License:        MIT OR Apache-2.0
URL:            https://github.com/unicode-rs/unicode-xid
#!RemoteAsset:  sha256:fc72304796d0818e357ead4e000d19c9c174ab23dc11093ac919054d20a6a7fc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bench) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}

%description
Source code for takopackized Rust crate "unicode-xid"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
