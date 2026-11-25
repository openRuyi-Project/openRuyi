# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name axum-macros
%global full_version 0.5.1
%global pkgname axum-macros-0.5

Name:           rust-axum-macros-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "axum-macros"
License:        MIT
URL:            https://github.com/tokio-rs/axum
#!RemoteAsset:  sha256:7aa268c23bfbbd2c4363b9cd302a4f504fb2a9dfe7e3451d66f35dd392e20aca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "axum-macros"

%package     -n %{name}+private
Summary:        Macros for axum - feature "__private"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/visit-mut) >= 2.0.0
Provides:       crate(%{pkgname}/private) = %{version}

%description -n %{name}+private
This metapackage enables feature "__private" for the Rust axum-macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
