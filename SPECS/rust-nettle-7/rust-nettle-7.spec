# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nettle
%global full_version 7.5.0
%global pkgname nettle-7

Name:           rust-nettle-7
Version:        7.5.0
Release:        %autorelease
Summary:        Rust crate "nettle"
License:        LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://gitlab.com/sequoia-pgp/nettle-rs
#!RemoteAsset:  sha256:2578a3627c28fefb60f1680e20e85f38bd8c8bf98c288b370489a573b0640907
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.3/default) >= 0.3.0
Requires:       crate(libc-0.2/default) >= 0.2.33
Requires:       crate(nettle-sys-2/default) >= 2.2.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(typenum-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "nettle"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
