# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name primeorder
%global full_version 0.14.0
%global pkgname primeorder-0.14

Name:           rust-primeorder-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "primeorder"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/primeorder
#!RemoteAsset:  sha256:5c9f42978c78a00e3d68f69fc03e57a234debae69da4020a4fb588fcdcd07b06
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.14/arithmetic) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Requires:       crate(primefield-0.14/default) >= 0.14.0
Requires:       crate(wnaf-0.14) >= 0.14.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/basepoint-table) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dev) = %{version}
Provides:       crate(%{pkgname}/hash2curve) = %{version}

%description
Generic over field elements and curve equation coefficients
Source code for takopackized Rust crate "primeorder"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.14/alloc) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/arithmetic) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Requires:       crate(serdect-0.4/alloc) >= 0.4.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
Generic over field elements and curve equation coefficients
This metapackage enables feature "alloc" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+critical-section
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "critical-section"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/basepoint-table) = %{version}
Requires:       crate(once-cell-1/critical-section) >= 1.21.0
Provides:       crate(%{pkgname}/critical-section) = %{version}

%description -n %{name}+critical-section
Generic over field elements and curve equation coefficients
This metapackage enables feature "critical-section" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1) >= 1.21.0
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
Generic over field elements and curve equation coefficients
This metapackage enables feature "once_cell" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serdect) = %{version}
Requires:       crate(elliptic-curve-0.14/arithmetic) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/serde) >= 0.14.1
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Generic over field elements and curve equation coefficients
This metapackage enables feature "serde" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "serdect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/serdect) = %{version}

%description -n %{name}+serdect
Generic over field elements and curve equation coefficients
This metapackage enables feature "serdect" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of complete addition formulas for prime order elliptic curves (Renes-Costello-Batina 2015) - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(elliptic-curve-0.14/arithmetic) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/std) >= 0.14.1
Requires:       crate(once-cell-1/std) >= 1.21.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
Generic over field elements and curve equation coefficients
This metapackage enables feature "std" for the Rust primeorder crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
