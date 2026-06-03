# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wit-bindgen-rt
%global full_version 0.39.0
%global pkgname wit-bindgen-rt-0.39

Name:           rust-wit-bindgen-rt-0.39
Version:        0.39.0
Release:        %autorelease
Summary:        Rust crate "wit-bindgen-rt"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wit-bindgen
#!RemoteAsset:  sha256:6f42320e61fe2cfd34354ecb597f86f413484a798ba44a8ca1165c58d42da6c1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wit-bindgen-rt"

%package     -n %{name}+async
Summary:        Runtime support for the `wit-bindgen` crate - feature "async"
Requires:       crate(%{pkgname})
Requires:       crate(futures-0.3/default) >= 0.3.30
Requires:       crate(once-cell-1.0/default) >= 1.19.0
Provides:       crate(%{pkgname}/async)

%description -n %{name}+async
This metapackage enables feature "async" for the Rust wit-bindgen-rt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Runtime support for the `wit-bindgen` crate - feature "bitflags"
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/default) >= 2.9.1
Provides:       crate(%{pkgname}/bitflags)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust wit-bindgen-rt crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
