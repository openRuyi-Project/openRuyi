# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-bigint
%global full_version 0.4.6
%global pkgname num-bigint-0.4

Name:           rust-num-bigint-0.4
Version:        0.4.6
Release:        %autorelease
Summary:        Rust crate "num-bigint"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-bigint
#!RemoteAsset:  sha256:a5e44f723f1133c9deac646763579fdb3ac745e418f2a7af9cd0c431da1f20b9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "num-bigint"

%package     -n %{name}+arbitrary
Summary:        Big integer implementation for Rust - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Big integer implementation for Rust - feature "quickcheck"
Requires:       crate(%{pkgname})
Requires:       crate(quickcheck-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/quickcheck)

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Big integer implementation for Rust - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Big integer implementation for Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Big integer implementation for Rust - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-integer-0.1/std) >= 0.1.46
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num-bigint crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
