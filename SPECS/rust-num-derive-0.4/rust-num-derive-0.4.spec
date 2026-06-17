# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-derive
%global full_version 0.4.2
%global pkgname num-derive-0.4

Name:           rust-num-derive-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "num-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-derive
#!RemoteAsset:  sha256:ed3955f1a9c7c0c15e092f9c887db08b1fc683305fdf6eb6684f22555355e202
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "num-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
