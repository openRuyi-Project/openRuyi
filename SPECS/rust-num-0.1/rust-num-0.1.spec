# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num
%global full_version 0.1.43
%global pkgname num-0.1

Name:           rust-num-0.1
Version:        0.1.43
Release:        %autorelease
Summary:        Rust crate "num"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num
#!RemoteAsset:  sha256:c9bdb1fb680e609c2e0930c1866cafdd0be7e7c7a1ecf92aec71ed8d99d3e133
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-integer-0.1/default) >= 0.1.36
Requires:       crate(num-iter-0.1/default) >= 0.1.35
Requires:       crate(num-traits-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "num"

%package     -n %{name}+default
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bigint) = %{version}
Requires:       crate(%{pkgname}/complex) = %{version}
Requires:       crate(%{pkgname}/rational) = %{version}
Requires:       crate(%{pkgname}/rustc-serialize) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "num-bigint" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.1/default) >= 0.1.45
Provides:       crate(%{pkgname}/bigint) = %{version}
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bigint" feature.

%package     -n %{name}+num-complex
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "num-complex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-complex-0.1/default) >= 0.1.44
Provides:       crate(%{pkgname}/complex) = %{version}
Provides:       crate(%{pkgname}/num-complex) = %{version}

%description -n %{name}+num-complex
This metapackage enables feature "num-complex" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "complex" feature.

%package     -n %{name}+num-rational
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "num-rational" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-rational-0.1/default) >= 0.1.43
Provides:       crate(%{pkgname}/num-rational) = %{version}
Provides:       crate(%{pkgname}/rational) = %{version}

%description -n %{name}+num-rational
This metapackage enables feature "num-rational" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rational" feature.

%package     -n %{name}+rustc-serialize
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "rustc-serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.1/rustc-serialize) >= 0.1.45
Requires:       crate(num-complex-0.1/rustc-serialize) >= 0.1.44
Requires:       crate(num-rational-0.1/rustc-serialize) >= 0.1.43
Provides:       crate(%{pkgname}/rustc-serialize) = %{version}

%description -n %{name}+rustc-serialize
This metapackage enables feature "rustc-serialize" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.1/serde) >= 0.1.45
Requires:       crate(num-complex-0.1/serde) >= 0.1.44
Requires:       crate(num-rational-0.1/serde) >= 0.1.43
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
