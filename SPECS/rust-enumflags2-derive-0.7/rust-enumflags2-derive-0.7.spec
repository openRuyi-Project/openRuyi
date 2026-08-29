# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name enumflags2_derive
%global full_version 0.7.12
%global pkgname enumflags2-derive-0.7

Name:           rust-enumflags2-derive-0.7
Version:        0.7.12
Release:        %autorelease
Summary:        Rust crate "enumflags2_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/meithecatte/enumflags2
#!RemoteAsset:  sha256:67c78a4d8fdf9953a5c9d458f9efe940fd97a0cab0941c075a813ac594733827
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/derive) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Requires:       crate(syn-2/proc-macro) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
This allows for better compatibility across versions.
Source code for takopackized Rust crate "enumflags2_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
