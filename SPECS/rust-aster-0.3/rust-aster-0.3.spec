# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aster
%global full_version 0.3.3
%global pkgname aster-0.3

Name:           rust-aster-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "aster"
License:        MIT OR Apache-2.0
URL:            https://github.com/erickt/rust-aster
#!RemoteAsset:  sha256:02777f32f673001a46df42f36801b9f8fa2cb29e22130a7f46c9bae3d919b5e9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "aster"

%package     -n %{name}+syntex-syntax
Summary:        Libsyntax ast builder - feature "syntex_syntax" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-syntax-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/syntex-syntax) = %{version}
Provides:       crate(%{pkgname}/with-syntex) = %{version}

%description -n %{name}+syntex-syntax
This metapackage enables feature "syntex_syntax" for the Rust aster crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-syntex" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
