# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smol
%global full_version 1.3.0
%global pkgname smol-1

Name:           rust-smol-1
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "smol"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/smol
#!RemoteAsset:  sha256:13f2b548cd8447f8de0fdf1c592929f70f4fc7039a05e47404b0d096ec6987a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-channel-1/default) >= 1.4.2
Requires:       crate(async-executor-1/default) >= 1.5.0
Requires:       crate(async-fs-1/default) >= 1.3.0
Requires:       crate(async-io-1/default) >= 1.12.0
Requires:       crate(async-lock-2/default) >= 2.6.0
Requires:       crate(async-net-1/default) >= 1.4.3
Requires:       crate(async-process-1/default) >= 1.6.0
Requires:       crate(blocking-1/default) >= 1.3.0
Requires:       crate(futures-lite-1/default) >= 1.11.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "smol"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
