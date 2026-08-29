# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proptest-derive
%global full_version 0.8.0
%global pkgname proptest-derive-0.8

Name:           rust-proptest-derive-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "proptest-derive"
License:        MIT OR Apache-2.0
URL:            https://proptest-rs.github.io/proptest/proptest-derive/index.html
#!RemoteAsset:  sha256:c57924a81864dddafba92e1bf92f9bf82f97096c44489548a60e888e1547549b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.114
Requires:       crate(syn-2/extra-traits) >= 2.0.114
Requires:       crate(syn-2/full) >= 2.0.114
Requires:       crate(syn-2/visit) >= 2.0.114
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/boxed-union) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proptest-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
