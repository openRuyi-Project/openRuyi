# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name enum_dispatch
%global full_version 0.3.13
%global pkgname enum-dispatch-0.3

Name:           rust-enum-dispatch-0.3
Version:        0.3.13
Release:        %autorelease
Summary:        Rust crate "enum_dispatch"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/antonok/enum_dispatch
#!RemoteAsset:  sha256:aa18ce2bc66555b3218614519ac839ddb759a7d6720732f979ef8d13be147ecd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/default) >= 1.0.1
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "enum_dispatch"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
