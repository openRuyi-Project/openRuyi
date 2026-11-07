# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-rational
%global full_version 0.1.43
%global pkgname num-rational-0.1

Name:           rust-num-rational-0.1
Version:        0.1.43
Release:        %autorelease
Summary:        Rust crate "num-rational"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-rational
#!RemoteAsset:  sha256:fbfff0773e8a07fb033d726b9ff1327466709820788e5298afce4d752965ff1e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.4.0
Requires:       crate(num-integer-0.1) >= 0.1.36
Requires:       crate(num-traits-0.2/std) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "num-rational"

%package     -n %{name}+default
Summary:        Rational numbers implementation for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bigint) = %{version}
Requires:       crate(%{pkgname}/rustc-serialize) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust num-rational crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Rational numbers implementation for Rust - feature "num-bigint" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.1/default) >= 0.1.45
Provides:       crate(%{pkgname}/bigint) = %{version}
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust num-rational crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bigint" feature.

%package     -n %{name}+rustc-serialize
Summary:        Rational numbers implementation for Rust - feature "rustc-serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-serialize-0.3/default) >= 0.3.19
Provides:       crate(%{pkgname}/rustc-serialize) = %{version}

%description -n %{name}+rustc-serialize
This metapackage enables feature "rustc-serialize" for the Rust num-rational crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Rational numbers implementation for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-rational crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
