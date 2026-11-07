# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quasi_codegen
%global full_version 0.3.1
%global pkgname quasi-codegen-0.3

Name:           rust-quasi-codegen-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "quasi_codegen"
License:        MIT OR Apache-2.0
URL:            https://github.com/erickt/rust-quasi
#!RemoteAsset:  sha256:fe9a1caa140852b8e885e3fe52ed41cdb25b19a8f53146f3bad1b0fe7a9041e3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aster-0.3) >= 0.3.3

Provides:       crate(%{pkgname}) = %{version}
Patch2000:      2000-Use-compatible-versioned-dependencies.patch

%description
Source code for takopackized Rust crate "quasi_codegen"

%package     -n %{name}+syntex
Summary:        Quasi-quoting macro system - feature "syntex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/syntex) = %{version}

%description -n %{name}+syntex
This metapackage enables feature "syntex" for the Rust quasi_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntex-syntax
Summary:        Quasi-quoting macro system - feature "syntex_syntax"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-syntax-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/syntex-syntax) = %{version}

%description -n %{name}+syntex-syntax
This metapackage enables feature "syntex_syntax" for the Rust quasi_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-syntex
Summary:        Quasi-quoting macro system - feature "with-syntex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/syntex) = %{version}
Requires:       crate(%{pkgname}/syntex-syntax) = %{version}
Requires:       crate(aster-0.3/with-syntex) >= 0.3.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/with-syntex) = %{version}

%description -n %{name}+with-syntex
This metapackage enables feature "with-syntex" for the Rust quasi_codegen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
