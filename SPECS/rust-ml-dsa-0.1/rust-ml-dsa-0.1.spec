# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ml-dsa
%global full_version 0.1.1
%global pkgname ml-dsa-0.1

Name:           rust-ml-dsa-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "ml-dsa"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/ml-dsa
#!RemoteAsset:  sha256:add6b9d92e496f16f4526d68ff29da1483aba4b119baeab8bed3b9e3544a6f3d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.2) >= 0.2.0
Requires:       crate(ctutils-0.4) >= 0.4.0
Requires:       crate(hybrid-array-0.4/default) >= 0.4.0
Requires:       crate(hybrid-array-0.4/extra-sizes) >= 0.4.0
Requires:       crate(module-lattice-0.2/ctutils) >= 0.2.3
Requires:       crate(module-lattice-0.2/default) >= 0.2.3
Requires:       crate(shake-0.1) >= 0.1.0
Requires:       crate(signature-3/digest) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ml-dsa"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilithium) as described in FIPS-204 (final) - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hybrid-array-0.4/alloc) >= 0.4.0
Requires:       crate(hybrid-array-0.4/extra-sizes) >= 0.4.0
Requires:       crate(module-lattice-0.2/alloc) >= 0.2.3
Requires:       crate(module-lattice-0.2/ctutils) >= 0.2.3
Requires:       crate(pkcs8-0.11/alloc) >= 0.11.0
Requires:       crate(signature-3/alloc) >= 3.0.0
Requires:       crate(signature-3/digest) >= 3.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ml-dsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilithium) as described in FIPS-204 (final) - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ml-dsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilithium) as described in FIPS-204 (final) - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(crypto-common-0.2/getrandom) >= 0.2.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust ml-dsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilithium) as described in FIPS-204 (final) - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-oid-0.10/db) >= 0.10.0
Requires:       crate(const-oid-0.10/default) >= 0.10.0
Requires:       crate(pkcs8-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ml-dsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilithium) as described in FIPS-204 (final) - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.0
Requires:       crate(signature-3/digest) >= 3.0.0
Requires:       crate(signature-3/rand-core) >= 3.0.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust ml-dsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilithium) as described in FIPS-204 (final) - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hybrid-array-0.4/extra-sizes) >= 0.4.0
Requires:       crate(hybrid-array-0.4/zeroize) >= 0.4.0
Requires:       crate(module-lattice-0.2/ctutils) >= 0.2.3
Requires:       crate(module-lattice-0.2/zeroize) >= 0.2.3
Requires:       crate(zeroize-1) >= 1.8.1
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ml-dsa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
