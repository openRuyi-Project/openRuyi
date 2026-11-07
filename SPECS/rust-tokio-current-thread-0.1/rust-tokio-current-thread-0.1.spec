# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-current-thread
%global full_version 0.1.7
%global pkgname tokio-current-thread-0.1

Name:           rust-tokio-current-thread-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "tokio-current-thread"
License:        MIT
URL:            https://github.com/tokio-rs/tokio
#!RemoteAsset:  sha256:b1de0e32a83f131e002238d7ccde18211c0a5397f60cbfffcb112868c2e0e20e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-0.1/default) >= 0.1.19
Requires:       crate(tokio-executor-0.1/default) >= 0.1.7

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-current-thread"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
