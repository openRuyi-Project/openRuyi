# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name color-print-proc-macro
%global full_version 0.3.7
%global pkgname color-print-proc-macro-0.3

Name:           rust-color-print-proc-macro-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "color-print-proc-macro"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/dajoha/color-print
#!RemoteAsset:  sha256:692186b5ebe54007e45a59aea47ece9eb4108e141326c304cdc91699a7118a22
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(nom-7/default) >= 7.1.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/terminfo) = %{version}

%description
Source code for takopackized Rust crate "color-print-proc-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
