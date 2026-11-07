# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-uds
%global full_version 0.2.7
%global pkgname tokio-uds-0.2

Name:           rust-tokio-uds-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "tokio-uds"
License:        MIT
URL:            https://github.com/tokio-rs/tokio
#!RemoteAsset:  sha256:ab57a4ac4111c8c9dbcf70779f6fc8bc35ae4b2454809febac840ad19bd7e4e0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-0.4/default) >= 0.4.8
Requires:       crate(futures-0.1/default) >= 0.1.21
Requires:       crate(iovec-0.1/default) >= 0.1.2
Requires:       crate(libc-0.2/default) >= 0.2.42
Requires:       crate(log-0.4/default) >= 0.4.2
Requires:       crate(mio-0.6/default) >= 0.6.14
Requires:       crate(mio-uds-0.6/default) >= 0.6.5
Requires:       crate(tokio-codec-0.1/default) >= 0.1.0
Requires:       crate(tokio-io-0.1/default) >= 0.1.6
Requires:       crate(tokio-reactor-0.1/default) >= 0.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-uds"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
