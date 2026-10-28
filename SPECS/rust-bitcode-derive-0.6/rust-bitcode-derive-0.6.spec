# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitcode_derive
%global full_version 0.6.9
%global pkgname bitcode-derive-0.6

Name:           rust-bitcode-derive-0.6
Version:        0.6.9
Release:        %autorelease
Summary:        Rust crate "bitcode_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/SoftbearStudios/bitcode/
#!RemoteAsset:  sha256:238b90427dfad9da4a9abd60f3ec1cdee6b80454bde49ed37f1781dd8e9dc7f9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.3
Requires:       crate(syn-2/extra-traits) >= 2.0.3
Requires:       crate(syn-2/visit-mut) >= 2.0.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bitcode_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
