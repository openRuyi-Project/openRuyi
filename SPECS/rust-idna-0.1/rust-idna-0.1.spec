# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name idna
%global full_version 0.1.5
%global pkgname idna-0.1

Name:           rust-idna-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "idna"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-url/
#!RemoteAsset:  sha256:38f09e0f0b1fb55fdee1f17470ad800da77af5186a1a76c026b679358b7e844e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(matches-0.1/default) >= 0.1.0
Requires:       crate(unicode-bidi-0.3/default) >= 0.3.0
Requires:       crate(unicode-normalization-0.1/default) >= 0.1.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "idna"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
