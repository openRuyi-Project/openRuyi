# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quasi
%global full_version 0.3.1
%global pkgname quasi-0.3

Name:           rust-quasi-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "quasi"
License:        MIT OR Apache-2.0
URL:            https://github.com/erickt/rust-quasi
#!RemoteAsset:  sha256:4bbee0c3d97184eb804914bd2f4b99ad8a47c9359104d5c93cdb6863bd40286d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Patch2000:      2000-Use-compatible-versioned-dependencies.patch

%description
Source code for takopackized Rust crate "quasi"

%package     -n %{name}+syntex-syntax
Summary:        Quasi-quoting macro system - feature "syntex_syntax" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-syntax-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/syntex-syntax) = %{version}
Provides:       crate(%{pkgname}/with-syntex) = %{version}

%description -n %{name}+syntex-syntax
This metapackage enables feature "syntex_syntax" for the Rust quasi crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-syntex" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
