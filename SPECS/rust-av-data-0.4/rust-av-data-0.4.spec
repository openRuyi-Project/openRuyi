# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name av-data
%global full_version 0.4.4
%global pkgname av-data-0.4

Name:           rust-av-data-0.4
Version:        0.4.4
Release:        %autorelease
Summary:        Rust crate "av-data"
License:        MIT
URL:            https://github.com/rust-av/rust-av
#!RemoteAsset:  sha256:fca67ba5d317924c02180c576157afd54babe48a76ebc66ce6d34bb8ba08308e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byte-slice-cast-1/default) >= 1.2.1
Requires:       crate(bytes-1/default) >= 1.2.1
Requires:       crate(num-derive-0.4/default) >= 0.4.0
Requires:       crate(num-rational-0.4/default) >= 0.4.0
Requires:       crate(num-traits-0.2/default) >= 0.2.8
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "av-data"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
