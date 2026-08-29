# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name internal-russh-num-bigint
%global full_version 0.5.0
%global pkgname internal-russh-num-bigint-0.5

Name:           rust-internal-russh-num-bigint-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "internal-russh-num-bigint"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-bigint
#!RemoteAsset:  sha256:ae8e22120c32fb4d19ec55fba35015f57095cd95a2e3b732e44457f5915b2ee8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-traits-0.2/i128) >= 0.2.18
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "internal-russh-num-bigint"

%package     -n %{name}+arbitrary
Summary:        Big integer implementation for Rust - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust internal-russh-num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Big integer implementation for Rust - feature "quickcheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-1) >= 1.0.0
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust internal-russh-num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-0-10
Summary:        Big integer implementation for Rust - feature "rand_0_10"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core-0-10) = %{version}
Requires:       crate(rand-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand-0-10) = %{version}

%description -n %{name}+rand-0-10
This metapackage enables feature "rand_0_10" for the Rust internal-russh-num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-0-9
Summary:        Big integer implementation for Rust - feature "rand_0_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core-0-9) = %{version}
Requires:       crate(rand-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/rand-0-9) = %{version}

%description -n %{name}+rand-0-9
This metapackage enables feature "rand_0_9" for the Rust internal-russh-num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core-0-10
Summary:        Big integer implementation for Rust - feature "rand_core_0_10"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand-core-0-10) = %{version}

%description -n %{name}+rand-core-0-10
This metapackage enables feature "rand_core_0_10" for the Rust internal-russh-num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core-0-9
Summary:        Big integer implementation for Rust - feature "rand_core_0_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/rand-core-0-9) = %{version}

%description -n %{name}+rand-core-0-9
This metapackage enables feature "rand_core_0_9" for the Rust internal-russh-num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Big integer implementation for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust internal-russh-num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Big integer implementation for Rust - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-integer-0.1/std) >= 0.1.46
Requires:       crate(num-traits-0.2/i128) >= 0.2.18
Requires:       crate(num-traits-0.2/std) >= 0.2.18
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust internal-russh-num-bigint crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
