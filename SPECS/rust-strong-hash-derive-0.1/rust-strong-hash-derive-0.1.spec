# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name strong_hash_derive
%global full_version 0.1.0
%global pkgname strong-hash-derive-0.1

Name:           rust-strong-hash-derive-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "strong_hash_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/facebook/buck2
#!RemoteAsset:  sha256:ace6b48b7c4383a39bd3b966cca41bc999003aab9f690a2f355525c924296928
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1/default) >= 1.0.44
Requires:       crate(syn-2/default) >= 2.0.110
Requires:       crate(syn-2/extra-traits) >= 2.0.110
Requires:       crate(syn-2/full) >= 2.0.110
Requires:       crate(syn-2/visit) >= 2.0.110

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "strong_hash_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
