# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-channel
%global full_version 1.9.0
%global pkgname async-channel-1

Name:           rust-async-channel-1
Version:        1.9.0
Release:        %autorelease
Summary:        Rust crate "async-channel"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-channel
#!RemoteAsset:  sha256:81953c529336010edd6d8e358f886d9581267795c61b19475b71314bffa46d35
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(concurrent-queue-2/default) >= 2.0.0
Requires:       crate(event-listener-2/default) >= 2.4.0
Requires:       crate(futures-core-0.3/default) >= 0.3.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-channel"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
