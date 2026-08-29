# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smol
%global full_version 2.0.2
%global pkgname smol-2

Name:           rust-smol-2
Version:        2.0.2
Release:        %autorelease
Summary:        Rust crate "smol"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/smol
#!RemoteAsset:  sha256:a33bd3e260892199c3ccfc487c88b2da2265080acb316cd920da72fdfd7c599f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-channel-2/default) >= 2.0.0
Requires:       crate(async-executor-1/default) >= 1.5.0
Requires:       crate(async-fs-2/default) >= 2.0.0
Requires:       crate(async-io-2/default) >= 2.1.0
Requires:       crate(async-lock-3/default) >= 3.0.0
Requires:       crate(async-net-2/default) >= 2.0.0
Requires:       crate(async-process-2/default) >= 2.0.0
Requires:       crate(blocking-1/default) >= 1.3.0
Requires:       crate(futures-lite-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "smol"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
