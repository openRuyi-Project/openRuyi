# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde
%global full_version 0.4.3
%global pkgname serde-0.4

Name:           rust-serde-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "serde"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/serde
#!RemoteAsset:  sha256:2b046ea3ac241d682446d05e5344983adf9818308dba753091ff971bba57421b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-0.1/default) >= 0.1.27

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Patch2000:      2000-Use-a-versioned-compatible-dependency.patch

%description
Source code for takopackized Rust crate "serde"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
