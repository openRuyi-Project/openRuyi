# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name more-asserts
%global full_version 0.3.1
%global pkgname more-asserts-0.3

Name:           rust-more-asserts-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "more-asserts"
License:        Unlicense OR MIT OR Apache-2.0 OR CC0-1.0
URL:            https://github.com/thomcc/rust-more-asserts
#!RemoteAsset:  sha256:1fafa6961cabd9c63bcd77a45d7e3b7f3b552b70417831fb0f56db717e72407e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "more-asserts"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
