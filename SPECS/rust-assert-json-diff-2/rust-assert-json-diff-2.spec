# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name assert-json-diff
%global full_version 2.0.2
%global pkgname assert-json-diff-2

Name:           rust-assert-json-diff-2
Version:        2.0.2
Release:        %autorelease
Summary:        Rust crate "assert-json-diff"
License:        MIT
URL:            https://github.com/davidpdrsn/assert-json-diff
#!RemoteAsset:  sha256:47e4f2b81832e72834d7518d8487a0396a28cc408186a2e8854c0f98011faf12
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "assert-json-diff"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
