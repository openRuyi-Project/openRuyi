# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num
%global full_version 0.4.3
%global pkgname num-0.4

Name:           rust-num-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "num"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num
#!RemoteAsset:  sha256:35bd024e8b2ff75562e5f34e7f4905839deb4b22955ef5e73d2fea1b9813cb23
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-complex-0.4) >= 0.4.6
Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-iter-0.1/i128) >= 0.1.45
Requires:       crate(num-rational-0.4) >= 0.4.2
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "num"

%package     -n %{name}+alloc
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(num-bigint-0.4) >= 0.4.6
Requires:       crate(num-rational-0.4/num-bigint) >= 0.4.2
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "libm"
Requires:       crate(%{pkgname})
Requires:       crate(num-complex-0.4/libm) >= 0.4.6
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Requires:       crate(num-traits-0.2/libm) >= 0.2.19
Provides:       crate(%{pkgname}/libm)

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "num-bigint"
Requires:       crate(%{pkgname})
Requires:       crate(num-bigint-0.4) >= 0.4.6
Provides:       crate(%{pkgname}/num-bigint)

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(num-bigint-0.4/rand) >= 0.4.6
Requires:       crate(num-complex-0.4/rand) >= 0.4.6
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(num-bigint-0.4/serde) >= 0.4.6
Requires:       crate(num-complex-0.4/serde) >= 0.4.6
Requires:       crate(num-rational-0.4/serde) >= 0.4.2
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(num-bigint-0.4) >= 0.4.6
Requires:       crate(num-bigint-0.4/std) >= 0.4.6
Requires:       crate(num-complex-0.4/std) >= 0.4.6
Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-integer-0.1/std) >= 0.1.46
Requires:       crate(num-iter-0.1/i128) >= 0.1.45
Requires:       crate(num-iter-0.1/std) >= 0.1.45
Requires:       crate(num-rational-0.4/num-bigint-std) >= 0.4.2
Requires:       crate(num-rational-0.4/std) >= 0.4.2
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
