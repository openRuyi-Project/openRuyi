# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gumdrop_derive
%global full_version 0.8.1
%global pkgname gumdrop-derive-0.8

Name:           rust-gumdrop-derive-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "gumdrop_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/murarth/gumdrop
#!RemoteAsset:  sha256:729f9bd3449d77e7831a18abfb7ba2f99ee813dfd15b8c2167c9a54ba20aa99d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gumdrop_derive"

%package     -n %{name}+default-expr
Summary:        Custom derive support for gumdrop - feature "default_expr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-1/full) >= 1.0.0
Provides:       crate(%{pkgname}/default-expr) = %{version}

%description -n %{name}+default-expr
This metapackage enables feature "default_expr" for the Rust gumdrop_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
