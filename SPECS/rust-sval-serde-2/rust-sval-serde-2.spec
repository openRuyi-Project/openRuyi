# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sval_serde
%global full_version 2.22.0
%global pkgname sval-serde-2

Name:           rust-sval-serde-2
Version:        2.22.0
Release:        %autorelease
Summary:        Rust crate "sval_serde"
License:        Apache-2.0 OR MIT
URL:            https://github.com/sval-rs/sval
#!RemoteAsset:  sha256:8f33ec9edc42b12764d5c90ca0a1d84189c6bde81ed27507f1e661c6e4e05853
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-core-1) >= 1.0.0
Requires:       crate(sval-2/default) >= 2.22.0
Requires:       crate(sval-nested-2) >= 2.22.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sval_serde"

%package     -n %{name}+alloc
Summary:        Integration between serde::Serialize and sval::Value - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/alloc) >= 1.0.0
Requires:       crate(sval-2/alloc) >= 2.22.0
Requires:       crate(sval-nested-2/alloc) >= 2.22.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust sval_serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Integration between serde::Serialize and sval::Value - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(serde-core-1/std) >= 1.0.0
Requires:       crate(sval-2/std) >= 2.22.0
Requires:       crate(sval-nested-2/std) >= 2.22.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sval_serde crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
