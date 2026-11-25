# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fluent-uri
%global full_version 0.1.4
%global pkgname fluent-uri-0.1

Name:           rust-fluent-uri-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "fluent-uri"
License:        MIT
URL:            https://github.com/yescallop/fluent-uri-rs
#!RemoteAsset:  sha256:17c704e9dbe1ddd863da1e6ff3567795087b1eb201ce80d8fa81162e1516500d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.3.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/ipv-future) = %{version}
Provides:       crate(%{pkgname}/rfc6874bis) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "fluent-uri"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
