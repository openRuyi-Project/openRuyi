# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prettyplease
%global full_version 0.2.37
%global pkgname prettyplease-0.2

Name:           rust-prettyplease-0.2
Version:        0.2.37
Release:        %autorelease
Summary:        Rust crate "prettyplease"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/prettyplease
#!RemoteAsset:  sha256:479ca8adacdd7ce8f1fb39ce9ecccbfe93a3f1344b3d0d97f20bc0196208f62b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0) >= 1.0.106
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "prettyplease"

%package     -n %{name}+verbatim
Summary:        Minimal `syn` syntax tree pretty-printer - feature "verbatim"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Provides:       crate(%{pkgname}/verbatim)

%description -n %{name}+verbatim
This metapackage enables feature "verbatim" for the Rust prettyplease crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
