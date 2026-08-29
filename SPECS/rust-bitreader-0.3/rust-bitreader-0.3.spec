# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitreader
%global full_version 0.3.11
%global pkgname bitreader-0.3

Name:           rust-bitreader-0.3
Version:        0.3.11
Release:        %autorelease
Summary:        Rust crate "bitreader"
License:        MIT OR Apache-2.0
URL:            https://github.com/irauta/bitreader
#!RemoteAsset:  sha256:886559b1e163d56c765bc3a985febb4eee8009f625244511d8ee3c432e08c066
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
You can read "unusual" numbers of bits from the byte slice, for example 13 bits at once. The reader internally keeps track of position within the buffer.
Source code for takopackized Rust crate "bitreader"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
