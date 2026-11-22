# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name databake-derive
%global full_version 0.2.0
%global pkgname databake-derive-0.2

Name:           rust-databake-derive-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "databake-derive"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:6834770958c7b84223607e49758ec0dde273c4df915e734aad50f62968a4c134
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.61
Requires:       crate(quote-1/default) >= 1.0.28
Requires:       crate(syn-2/default) >= 2.0.21
Requires:       crate(synstructure-0.13/default) >= 0.13.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "databake-derive"

%files
%license %{_datadir}/cargo/registry/%{crate_name}-%{version}/LICENSE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
