# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive-where
%global full_version 1.6.1
%global pkgname derive-where-1

Name:           rust-derive-where-1
Version:        1.6.1
Release:        %autorelease
Summary:        Rust crate "derive-where"
License:        MIT OR Apache-2.0
URL:            https://github.com/ModProg/derive-where
#!RemoteAsset:  sha256:d08b3a0bcc0d079199cd476b2cae8435016ec11d1c0986c6901c5ac223041534
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/proc-macro) >= 1.0.0
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(syn-2/clone-impls) >= 2.0.0
Requires:       crate(syn-2/derive) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/safe) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/zeroize) = %{version}
Provides:       crate(%{pkgname}/zeroize-on-drop) = %{version}

%description
Source code for takopackized Rust crate "derive-where"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
