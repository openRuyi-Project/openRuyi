# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name enum-map-derive
%global full_version 0.17.0
%global pkgname enum-map-derive-0.17

Name:           rust-enum-map-derive-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "enum-map-derive"
License:        MIT OR Apache-2.0
URL:            https://codeberg.org/xfix/enum-map
#!RemoteAsset:  sha256:f282cfdfe92516eb26c2af8589c274c7c17681f5ecc03c18255fe741c6aa64eb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.60
Requires:       crate(quote-1/default) >= 1.0.7
Requires:       crate(syn-2/derive) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Requires:       crate(syn-2/proc-macro) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "enum-map-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
