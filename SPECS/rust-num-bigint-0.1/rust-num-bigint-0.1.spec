# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-bigint
%global full_version 0.1.45
%global pkgname num-bigint-0.1

Name:           rust-num-bigint-0.1
Version:        0.1.45
Release:        %autorelease
Summary:        Rust crate "num-bigint"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-bigint
#!RemoteAsset:  sha256:1357c02fa1d647dd0769ef5bc2bf86281f064231c09c192a46c71246e3ec9258
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.4.0
Requires:       crate(num-integer-0.1) >= 0.1.36
Requires:       crate(num-traits-0.2/std) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "num-bigint"

%package     -n %{name}+default
Summary:        Big integer implementation for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/rustc-serialize) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Big integer implementation for Rust - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.3/default) >= 0.3.14
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-serialize
Summary:        Big integer implementation for Rust - feature "rustc-serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-serialize-0.3/default) >= 0.3.19
Provides:       crate(%{pkgname}/rustc-serialize) = %{version}

%description -n %{name}+rustc-serialize
This metapackage enables feature "rustc-serialize" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Big integer implementation for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
