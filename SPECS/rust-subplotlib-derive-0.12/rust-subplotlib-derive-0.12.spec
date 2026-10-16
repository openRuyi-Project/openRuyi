# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name subplotlib-derive
%global full_version 0.12.0
%global pkgname subplotlib-derive-0.12

Name:           rust-subplotlib-derive-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "subplotlib-derive"
License:        MIT-0
URL:            https://subplot.tech/
#!RemoteAsset:  sha256:f37c9bc08dcdd72eb2a5f0d2f405c5384466c7c199921b00d4ab9d8f60972efb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(culpa-1/default) >= 1.0.1
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(subplot-0.12/default) >= 0.12.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "subplotlib-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
