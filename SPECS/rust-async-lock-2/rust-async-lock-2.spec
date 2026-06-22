# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-lock
%global full_version 2.8.0
%global pkgname async-lock-2

Name:           rust-async-lock-2
Version:        2.8.0
Release:        %autorelease
Summary:        Rust crate "async-lock"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-lock
#!RemoteAsset:  sha256:287272293e9d8c41773cec55e365490fe034813a2f172f502d6ddcf75b2f582b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(event-listener-2/default) >= 2.5.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-lock"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
