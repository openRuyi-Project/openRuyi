# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-broadcast
%global full_version 0.7.2
%global pkgname async-broadcast-0.7

Name:           rust-async-broadcast-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "async-broadcast"
License:        MIT OR Apache-2.0
URL:            https://github.com/smol-rs/async-broadcast
#!RemoteAsset:  sha256:435a87a52755b8f27fcf321ac4f04b2802e337c8c4872923137471ec39c37532
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(event-listener-5/default) >= 5.0.0
Requires:       crate(event-listener-strategy-0.5/default) >= 0.5.0
Requires:       crate(futures-core-0.3/default) >= 0.3.21
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.13
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-broadcast"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
