# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-net
%global full_version 2.0.0
%global pkgname async-net-2

Name:           rust-async-net-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "async-net"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-net
#!RemoteAsset:  sha256:b948000fad4873c1c9339d60f2623323a0cfd3816e5181033c6a5cb68b2accf7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-io-2/default) >= 2.0.0
Requires:       crate(blocking-1/default) >= 1.0.0
Requires:       crate(futures-lite-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-net"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
