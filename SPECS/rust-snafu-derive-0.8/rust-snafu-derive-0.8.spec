# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name snafu-derive
%global full_version 0.8.9
%global pkgname snafu-derive-0.8

Name:           rust-snafu-derive-0.8
Version:        0.8.9
Release:        %autorelease
Summary:        Rust crate "snafu-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/shepmaster/snafu
#!RemoteAsset:  sha256:c1c97747dbf44bb1ca44a561ece23508e99cb592e862f22222dcf42f51d1e451
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.4) >= 0.4.0
Requires:       crate(proc-macro2-1/default) >= 1.0.52
Requires:       crate(quote-1/default) >= 1.0.25
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rust-1-61) = %{version}
Provides:       crate(%{pkgname}/unstable-provider-api) = %{version}

%description
Source code for takopackized Rust crate "snafu-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
