# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rust-argon2
%global full_version 0.8.3
%global pkgname rust-argon2-0.8

Name:           rust-rust-argon2-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "rust-argon2"
License:        MIT OR Apache-2.0
URL:            https://github.com/sru-systems/rust-argon2
#!RemoteAsset:  sha256:4b18820d944b33caa75a71378964ac46f58517c92b6ae5f762636247c09e78fb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.13/default) >= 0.13.0
Requires:       crate(blake2b-simd-0.5/default) >= 0.5.0
Requires:       crate(constant-time-eq-0.1/default) >= 0.1.4

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rust-argon2"

%package     -n %{name}+crossbeam-utils
Summary:        The Argon2 password hashing function - feature "crossbeam-utils" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/crossbeam-utils) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+crossbeam-utils
This metapackage enables feature "crossbeam-utils" for the Rust rust-argon2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+serde
Summary:        The Argon2 password hashing function - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.116
Requires:       crate(serde-1/derive) >= 1.0.116
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rust-argon2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
