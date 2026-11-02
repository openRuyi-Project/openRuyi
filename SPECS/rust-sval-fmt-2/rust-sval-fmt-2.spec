# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sval_fmt
%global full_version 2.22.0
%global pkgname sval-fmt-2

Name:           rust-sval-fmt-2
Version:        2.22.0
Release:        %autorelease
Summary:        Rust crate "sval_fmt"
License:        Apache-2.0 OR MIT
URL:            https://github.com/sval-rs/sval
#!RemoteAsset:  sha256:e6b5888e40f80568733217f27b7317b845f463400ced36c424b1a804730e53b2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(ryu-1/default) >= 1.0.0
Requires:       crate(sval-2/default) >= 2.22.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sval_fmt"

%package     -n %{name}+alloc
Summary:        Integration between std::fmt::Debug and sval::Value - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-2/alloc) >= 2.22.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust sval_fmt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Integration between std::fmt::Debug and sval::Value - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(sval-2/std) >= 2.22.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sval_fmt crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
