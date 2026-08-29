# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-stream
%global full_version 0.3.6
%global pkgname async-stream-0.3

Name:           rust-async-stream-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "async-stream"
License:        MIT
URL:            https://github.com/tokio-rs/async-stream
#!RemoteAsset:  sha256:0b5a71a6f37880a80d1d7f19efd781e4b5de42c88f0722cc13bcb6cc2cfe8476
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-stream-impl-0.3/default) >= 0.3.6
Requires:       crate(futures-core-0.3/default) >= 0.3.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-stream"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
