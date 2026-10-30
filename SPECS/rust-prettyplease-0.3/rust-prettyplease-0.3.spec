# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prettyplease
%global full_version 0.3.0
%global pkgname prettyplease-0.3

Name:           rust-prettyplease-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "prettyplease"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/prettyplease
#!RemoteAsset:  sha256:2bfe0f4c752e450fc2faf62654f1c134747922825d5b04ca717b8874f41a40c0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.80
Requires:       crate(syn-3/full) >= 3.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
A minimal syn syntax tree pretty-printer.
Source code for takopackized Rust crate "prettyplease"

%package     -n %{name}+verbatim
Summary:        Minimal syn syntax tree pretty-printer - feature "verbatim"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-3/parsing) >= 3.0.0
Provides:       crate(%{pkgname}/verbatim) = %{version}

%description -n %{name}+verbatim
This metapackage enables feature "verbatim" for the Rust prettyplease crate.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
