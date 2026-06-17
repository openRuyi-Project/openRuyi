# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-rational
%global full_version 0.4.2
%global pkgname num-rational-0.4

Name:           rust-num-rational-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "num-rational"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-rational
#!RemoteAsset:  sha256:f83d14da390562dca69fc84082e73e548e1ad308d24accdedd2720017cb37824
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-integer-0.1/i128) >= 0.1.42
Requires:       crate(num-traits-0.2/i128) >= 0.2.18
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "num-rational"

%package     -n %{name}+default
Summary:        Rational numbers implementation for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-bigint) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust num-rational crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Rational numbers implementation for Rust - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust num-rational crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint-std
Summary:        Rational numbers implementation for Rust - feature "num-bigint-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/num-bigint-std) = %{version}

%description -n %{name}+num-bigint-std
This metapackage enables feature "num-bigint-std" for the Rust num-rational crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Rational numbers implementation for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-rational crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Rational numbers implementation for Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/std) >= 0.4.0
Requires:       crate(num-integer-0.1/i128) >= 0.1.42
Requires:       crate(num-integer-0.1/std) >= 0.1.42
Requires:       crate(num-traits-0.2/i128) >= 0.2.18
Requires:       crate(num-traits-0.2/std) >= 0.2.18
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num-rational crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
