# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name filesize
%global full_version 0.2.0
%global pkgname filesize-0.2

Name:           rust-filesize-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "filesize"
License:        MIT
URL:            https://github.com/Freaky/rust-filesize
#!RemoteAsset:  sha256:12d741e2415d4e2e5bd1c1d00409d1a8865a57892c2d689b504365655d237d43
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winapi-0.3/default) >= 0.3.8
Requires:       crate(winapi-0.3/fileapi) >= 0.3.8
Requires:       crate(winapi-0.3/winerror) >= 0.3.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "filesize"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
