# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name russh-sftp
%global full_version 3.0.0
%global pkgname russh-sftp-3

Name:           rust-russh-sftp-3
Version:        3.0.0
Release:        %autorelease
Summary:        Rust crate "russh-sftp"
License:        Apache-2.0
URL:            https://github.com/AspectUnk/russh-sftp
#!RemoteAsset:  sha256:093197e526668d92bba562e2bbbe98d1af9831bf080b619c736316ca1fa35101
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.13.1
Requires:       crate(bitflags-2/serde) >= 2.13.1
Requires:       crate(bytes-1/default) >= 1.12.1
Requires:       crate(chrono-0.4/default) >= 0.4.45
Requires:       crate(dashmap-6/default) >= 6.2.1
Requires:       crate(gloo-timers-0.4/default) >= 0.4.0
Requires:       crate(gloo-timers-0.4/futures) >= 0.4.0
Requires:       crate(log-0.4/default) >= 0.4.34
Requires:       crate(serde-1/default) >= 1.0.229
Requires:       crate(serde-1/derive) >= 1.0.229
Requires:       crate(serde-bytes-0.11/default) >= 0.11.19
Requires:       crate(thiserror-2/default) >= 2.0.20
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tokio-util-0.7/rt) >= 0.7.19
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.78

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "russh-sftp"

%package     -n %{name}+async-trait
Summary:        SFTP subsystem supported server and client for Russh - feature "async-trait"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-trait-0.1/default) >= 0.1.92
Provides:       crate(%{pkgname}/async-trait) = %{version}

%description -n %{name}+async-trait
This metapackage enables feature "async-trait" for the Rust russh-sftp
crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
