# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name primeorder
%global full_version 0.13.6
%global pkgname primeorder-0.13

Name:           rust-primeorder-0.13
Version:        0.13.6
Release:        %autorelease
Summary:        Rust crate "primeorder"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/primeorder
#!RemoteAsset:  sha256:353e1ca18966c16d9deb1c69278edbc5f194139612772bd9537af60ac231e1e6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.13/arithmetic) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/dev)

%description
Generic over field elements and curve equation coefficients
Source code for takopackized Rust crate "primeorder"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(elliptic-curve-0.13/alloc) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/arithmetic) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
Generic over field elements and curve equation coefficients
This metapackage enables feature "alloc" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serdect)
Requires:       crate(elliptic-curve-0.13/arithmetic) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/serde) >= 0.13.8
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
Generic over field elements and curve equation coefficients
This metapackage enables feature "serde" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "serdect"
Requires:       crate(%{pkgname})
Requires:       crate(serdect-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/serdect)

%description -n %{name}+serdect
Generic over field elements and curve equation coefficients
This metapackage enables feature "serdect" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(elliptic-curve-0.13/arithmetic) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/std) >= 0.13.8
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
Generic over field elements and curve equation coefficients
This metapackage enables feature "std" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
