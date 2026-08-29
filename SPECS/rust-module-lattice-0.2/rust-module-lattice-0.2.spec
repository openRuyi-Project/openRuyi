# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name module-lattice
%global full_version 0.2.3
%global pkgname module-lattice-0.2

Name:           rust-module-lattice-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "module-lattice"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/KEMs/tree/master/module-lattice
#!RemoteAsset:  sha256:0c61b87c9683ab7cb1c6871d261ad5479b6b10ceb52c4352aaca3b5d35a8febe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hybrid-array-0.4/default) >= 0.4.8
Requires:       crate(hybrid-array-0.4/extra-sizes) >= 0.4.8
Requires:       crate(num-traits-0.2) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "module-lattice"

%package     -n %{name}+ctutils
Summary:        Functionality shared between the `ml-kem` and `ml-dsa` crates, including linear algebra with degree-256 polynomials over a prime-order field, vectors of such polynomials, and NTT polynomials and vectors, as well as packing of polynomials into coefficients with a specified number of bits - feature "ctutils"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ctutils-0.4/default) >= 0.4.0
Requires:       crate(hybrid-array-0.4/ctutils) >= 0.4.8
Requires:       crate(hybrid-array-0.4/extra-sizes) >= 0.4.8
Provides:       crate(%{pkgname}/ctutils) = %{version}

%description -n %{name}+ctutils
This metapackage enables feature "ctutils" for the Rust module-lattice crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Functionality shared between the `ml-kem` and `ml-dsa` crates, including linear algebra with degree-256 polynomials over a prime-order field, vectors of such polynomials, and NTT polynomials and vectors, as well as packing of polynomials into coefficients with a specified number of bits - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hybrid-array-0.4/extra-sizes) >= 0.4.8
Requires:       crate(hybrid-array-0.4/zeroize) >= 0.4.8
Requires:       crate(zeroize-1) >= 1.8.1
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust module-lattice crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
