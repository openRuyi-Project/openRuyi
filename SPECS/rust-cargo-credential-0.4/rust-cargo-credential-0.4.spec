# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-credential
%global full_version 0.4.9
%global pkgname cargo-credential-0.4

Name:           rust-cargo-credential-0.4
Version:        0.4.9
Release:        %autorelease
Summary:        Rust crate "cargo-credential"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:e36f089041deadf16226478a7737a833864fbda09408c7af237b9d615eeb6d69
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.98
Requires:       crate(libc-0.2/default) >= 0.2.174
Requires:       crate(serde-1/default) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(serde-json-1/default) >= 1.0.140
Requires:       crate(thiserror-2/default) >= 2.0.12
Requires:       crate(time-0.3/default) >= 0.3.41
Requires:       crate(time-0.3/formatting) >= 0.3.41
Requires:       crate(time-0.3/parsing) >= 0.3.41
Requires:       crate(time-0.3/serde) >= 0.3.41
Requires:       crate(windows-sys-0.60/default) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-console) >= 0.60.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cargo-credential"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
