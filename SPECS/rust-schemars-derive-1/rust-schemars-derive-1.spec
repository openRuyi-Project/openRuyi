# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name schemars_derive
%global full_version 1.2.1
%global pkgname schemars-derive-1

Name:           rust-schemars-derive-1
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "schemars_derive"
License:        MIT
URL:            https://graham.cool/schemars/
#!RemoteAsset:  sha256:7d115b50f4aaeea07e79c1912f645c7513d81715d0420f8bc77a18c6260b307f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.74
Requires:       crate(quote-1/default) >= 1.0.35
Requires:       crate(serde-derive-internals-0.29/default) >= 0.29.1
Requires:       crate(syn-2/default) >= 2.0.46
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "schemars_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
