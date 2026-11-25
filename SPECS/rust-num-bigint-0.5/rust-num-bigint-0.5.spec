# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-bigint
%global full_version 0.5.1
%global pkgname num-bigint-0.5

Name:           rust-num-bigint-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "num-bigint"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-bigint
#!RemoteAsset:  sha256:93e7820bc0a80a0238e650327316f929ba18d5be054b647490a3a6a339f3e7c0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-traits-0.2/i128) >= 0.2.18

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "num-bigint"

%package     -n %{name}+arbitrary
Summary:        Big integer implementation for Rust - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Big integer implementation for Rust - feature "quickcheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-1) >= 1.0.0
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-0-10
Summary:        Big integer implementation for Rust - feature "rand_0_10"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core-0-10) = %{version}
Requires:       crate(rand-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand-0-10) = %{version}

%description -n %{name}+rand-0-10
This metapackage enables feature "rand_0_10" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-0-9
Summary:        Big integer implementation for Rust - feature "rand_0_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core-0-9) = %{version}
Requires:       crate(rand-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/rand-0-9) = %{version}

%description -n %{name}+rand-0-9
This metapackage enables feature "rand_0_9" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core-0-10
Summary:        Big integer implementation for Rust - feature "rand_core_0_10"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand-core-0-10) = %{version}

%description -n %{name}+rand-core-0-10
This metapackage enables feature "rand_core_0_10" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core-0-9
Summary:        Big integer implementation for Rust - feature "rand_core_0_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/rand-core-0-9) = %{version}

%description -n %{name}+rand-core-0-9
This metapackage enables feature "rand_core_0_9" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Big integer implementation for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

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
This metapackage enables feature "std" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
