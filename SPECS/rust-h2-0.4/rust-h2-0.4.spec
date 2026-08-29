# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name h2
%global full_version 0.4.13
%global pkgname h2-0.4

Name:           rust-h2-0.4
Version:        0.4.13
Release:        %autorelease
Summary:        Rust crate "h2"
License:        MIT
URL:            https://github.com/hyperium/h2
#!RemoteAsset:  sha256:2f44da3a8150a6703ed5d34e164b875fd14c2cdab9af1252a9a1020bde2bdc54
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atomic-waker-1/default) >= 1.0.0
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(fnv-1/default) >= 1.0.5
Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(futures-sink-0.3) >= 0.3.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(indexmap-2/std) >= 2.0.0
Requires:       crate(slab-0.4/default) >= 0.4.2
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-util-0.7/codec) >= 0.7.1
Requires:       crate(tokio-util-0.7/default) >= 0.7.1
Requires:       crate(tokio-util-0.7/io) >= 0.7.1
Requires:       crate(tracing-0.1/std) >= 0.1.35
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/stream) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "h2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
