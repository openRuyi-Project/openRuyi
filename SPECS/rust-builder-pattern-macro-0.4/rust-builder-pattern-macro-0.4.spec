# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name builder-pattern-macro
%global full_version 0.4.2
%global pkgname builder-pattern-macro-0.4

Name:           rust-builder-pattern-macro-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "builder-pattern-macro"
License:        MIT
URL:            https://github.com/SeokminHong/builder-pattern-macro
#!RemoteAsset:  sha256:47d624ef88b39588d113f807ffb38ee968aafc388ca57dd7a9a7b82d3de1f5f4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.3.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.0
Requires:       crate(syn-1/full) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Do not use this crate directly.
Source code for takopackized Rust crate "builder-pattern-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
