# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mp4parse
%global full_version 0.17.0
%global pkgname mp4parse-0.17

Name:           rust-mp4parse-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "mp4parse"
License:        MPL-2.0
URL:            https://github.com/mozilla/mp4parse-rust
#!RemoteAsset:  sha256:63a35203d3c6ce92d5251c77520acb2e57108c88728695aa883f70023624c570
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitreader-0.3/default) >= 0.3.2
Requires:       crate(byteorder-1/default) >= 1.2.1
Requires:       crate(fallible-collections-0.4/default) >= 0.4.0
Requires:       crate(fallible-collections-0.4/std-io) >= 0.4.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(num-traits-0.2/default) >= 0.2.14
Requires:       crate(static-assertions-1/default) >= 1.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/3gpp) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/meta-xml) = %{version}
Provides:       crate(%{pkgname}/missing-pixi-permitted) = %{version}
Provides:       crate(%{pkgname}/mp4v) = %{version}
Provides:       crate(%{pkgname}/unstable-api) = %{version}

%description
Source code for takopackized Rust crate "mp4parse"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
