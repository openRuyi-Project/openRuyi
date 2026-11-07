# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name h3-quinn
%global full_version 0.0.4
%global pkgname h3-quinn-0.0.4

Name:           rust-h3-quinn-0.0.4
Version:        0.0.4
Release:        %autorelease
Summary:        Rust crate "h3-quinn"
License:        MIT
URL:            https://github.com/hyperium/h3
#!RemoteAsset:  sha256:ac9675014d703c3d516a121757bbc02e53f1ee838e0729fc7534b35024a81ae4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(futures-0.3/default) >= 0.3.28
Requires:       crate(h3-0.0.3/default) >= 0.0.3
Requires:       crate(quinn-0.10/futures-io) >= 0.10.0
Requires:       crate(quinn-proto-0.10) >= 0.10.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "h3-quinn"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
