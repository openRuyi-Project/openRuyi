# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(nom-7.0/default) >= 7.1.3
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/terminfo)

%description
Source code for takopackized Rust crate "color-print-proc-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
