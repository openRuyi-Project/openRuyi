# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-process
%global full_version 1.8.1
%global pkgname async-process-1

Name:           rust-async-process-1
Version:        1.8.1
Release:        %autorelease
Summary:        Rust crate "async-process"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-process
#!RemoteAsset:  sha256:ea6438ba0a08d81529c69b36700fa2f95837bfe3e776ab39cde9c14d9149da88
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-io-1/default) >= 1.8.0
Requires:       crate(async-lock-2/default) >= 2.6.0
Requires:       crate(async-signal-0.2/default) >= 0.2.3
Requires:       crate(blocking-1/default) >= 1.0.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(event-listener-3/default) >= 3.0.0
Requires:       crate(futures-lite-1/default) >= 1.11.0
Requires:       crate(rustix-0.38/fs) >= 0.38.0
Requires:       crate(rustix-0.38/std) >= 0.38.0
Requires:       crate(windows-sys-0.48/win32-foundation) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-threading) >= 0.48.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-process"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
