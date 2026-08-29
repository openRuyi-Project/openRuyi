# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_urlencoded
%global full_version 0.7.1
%global pkgname serde-urlencoded-0.7

Name:           rust-serde-urlencoded-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "serde_urlencoded"
License:        MIT OR Apache-2.0
URL:            https://github.com/nox/serde_urlencoded
#!RemoteAsset:  sha256:d3491c14715ca2294c4d6a88f15e84739788c1d030eed8c110436aafdaa2f3fd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(form-urlencoded-1/default) >= 1.0.0
Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(ryu-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.69
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_urlencoded"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
