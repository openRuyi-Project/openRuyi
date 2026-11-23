# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name automod
%global full_version 1.0.15
%global pkgname automod-1

Name:           rust-automod-1
Version:        1.0.15
Release:        %autorelease
Summary:        Rust crate "automod"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/automod
#!RemoteAsset:  sha256:ebb4bd301db2e2ca1f5be131c24eb8ebf2d9559bc3744419e93baf8ddea7e670
Source:         https://static.crates.io/crates/automod/1.0.15/download#/rust-automod-1-1.0.15.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.74
Requires:       crate(quote-1/default) >= 1.0.35
Requires:       crate(syn-2/default) >= 2.0.46
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "automod"

%package     -n %{name}+default
Summary:        Pull in every source file in a directory as a module - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust automod crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
