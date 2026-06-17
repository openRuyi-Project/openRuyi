# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name markup5ever
%global full_version 0.35.0
%global pkgname markup5ever-0.35

Name:           rust-markup5ever-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "markup5ever"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/html5ever
#!RemoteAsset:  sha256:311fe69c934650f8f19652b3946075f0fc41ad8757dbb68f1ca14e7900ecc1c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(tendril-0.4/default) >= 0.4.0
Requires:       crate(web-atoms-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "markup5ever"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
