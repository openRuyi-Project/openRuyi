# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rust_decimal
%global full_version 1.42.1
%global pkgname rust-decimal-1

Name:           rust-rust-decimal-1
Version:        1.42.1
Release:        %autorelease
Summary:        Rust crate "rust_decimal"
License:        MIT
URL:            https://github.com/paupino/rust-decimal
#!RemoteAsset:  sha256:be2a24f50780bc85f09cc6ac299bdf1424302742d77221106859c9d8b102126a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayvec-0.7) >= 0.7.0
Requires:       crate(num-traits-0.2/i128) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/align16) = %{version}
Provides:       crate(%{pkgname}/c-repr) = %{version}
Provides:       crate(%{pkgname}/legacy-ops) = %{version}
Provides:       crate(%{pkgname}/maths) = %{version}
Provides:       crate(%{pkgname}/maths-nopanic) = %{version}

%description
Source code for takopackized Rust crate "rust_decimal"

%package     -n %{name}+borsh
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "borsh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(borsh-1/derive) >= 1.1.1
Requires:       crate(borsh-1/unstable--schema) >= 1.1.1
Provides:       crate(%{pkgname}/borsh) = %{version}

%description -n %{name}+borsh
This metapackage enables feature "borsh" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/c-repr) = %{version}
Requires:       crate(bytemuck-1) >= 1.17.1
Requires:       crate(bytemuck-derive-1) >= 1.7.1
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+db-diesel-mysql
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "db-diesel-mysql" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(diesel-2/mysql-backend) >= 2.2.3
Provides:       crate(%{pkgname}/db-diesel-mysql) = %{version}
Provides:       crate(%{pkgname}/db-diesel2-mysql) = %{version}

%description -n %{name}+db-diesel-mysql
This metapackage enables feature "db-diesel-mysql" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "db-diesel2-mysql" feature.

%package     -n %{name}+db-diesel-postgres
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "db-diesel-postgres" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(diesel-2/postgres-backend) >= 2.2.3
Provides:       crate(%{pkgname}/db-diesel-postgres) = %{version}
Provides:       crate(%{pkgname}/db-diesel2-postgres) = %{version}

%description -n %{name}+db-diesel-postgres
This metapackage enables feature "db-diesel-postgres" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "db-diesel2-postgres" feature.

%package     -n %{name}+db-postgres
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "db-postgres" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(bytes-1) >= 1.0.0
Requires:       crate(postgres-types-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/db-postgres) = %{version}
Provides:       crate(%{pkgname}/db-tokio-postgres) = %{version}
Provides:       crate(%{pkgname}/tokio-pg) = %{version}

%description -n %{name}+db-postgres
This metapackage enables feature "db-postgres" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "db-tokio-postgres", and "tokio-pg" features.

%package     -n %{name}+default
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+diesel
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "diesel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(diesel-2) >= 2.2.3
Provides:       crate(%{pkgname}/diesel) = %{version}

%description -n %{name}+diesel
This metapackage enables feature "diesel" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-macros-1) >= 1.0.0
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ndarray
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "ndarray"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ndarray-0.15) >= 0.15.6
Provides:       crate(%{pkgname}/ndarray) = %{version}

%description -n %{name}+ndarray
This metapackage enables feature "ndarray" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "proptest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proptest-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/proptest) = %{version}

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-0-9
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "rand-0_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/rand-0-9) = %{version}

%description -n %{name}+rand-0-9
This metapackage enables feature "rand-0_9" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "rkyv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.7/size-32) >= 0.7.46
Requires:       crate(rkyv-0.7/std) >= 0.7.46
Provides:       crate(%{pkgname}/rkyv) = %{version}

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-safe
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "rkyv-safe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.7/size-32) >= 0.7.46
Requires:       crate(rkyv-0.7/std) >= 0.7.46
Requires:       crate(rkyv-0.7/validation) >= 0.7.46
Provides:       crate(%{pkgname}/rkyv-safe) = %{version}

%description -n %{name}+rkyv-safe
This metapackage enables feature "rkyv-safe" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rocket-traits
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "rocket-traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(rocket-0.5.0-rc.3) >= 0.5.0-rc.3
Provides:       crate(%{pkgname}/rocket-traits) = %{version}

%description -n %{name}+rocket-traits
This metapackage enables feature "rocket-traits" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-fuzz
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "rust-fuzz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1) >= 1.0.0
Provides:       crate(%{pkgname}/rust-fuzz) = %{version}

%description -n %{name}+rust-fuzz
This metapackage enables feature "rust-fuzz" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "serde" and 5 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Requires:       crate(wasm-bindgen-0.2/serde) >= 0.2.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-bincode) = %{version}
Provides:       crate(%{pkgname}/serde-float) = %{version}
Provides:       crate(%{pkgname}/serde-str) = %{version}
Provides:       crate(%{pkgname}/serde-with-float) = %{version}
Provides:       crate(%{pkgname}/serde-with-str) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde-bincode", "serde-float", "serde-str", "serde-with-float", and "serde-with-str" features.

%package     -n %{name}+serde-with-arbitrary-precision
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "serde-with-arbitrary-precision" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/zmij) = %{version}
Requires:       crate(serde-json-1/arbitrary-precision) >= 1.0.0
Requires:       crate(serde-json-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde-arbitrary-precision) = %{version}
Provides:       crate(%{pkgname}/serde-with-arbitrary-precision) = %{version}

%description -n %{name}+serde-with-arbitrary-precision
This metapackage enables feature "serde-with-arbitrary-precision" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde-arbitrary-precision" feature.

%package     -n %{name}+serde-json
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7/std) >= 0.7.0
Requires:       crate(borsh-1/derive) >= 1.1.1
Requires:       crate(borsh-1/std) >= 1.1.1
Requires:       crate(borsh-1/unstable--schema) >= 1.1.1
Requires:       crate(bytes-1/std) >= 1.0.0
Requires:       crate(rand-0.8/std) >= 0.8.0
Requires:       crate(rkyv-0.7/size-32) >= 0.7.46
Requires:       crate(rkyv-0.7/std) >= 0.7.46
Requires:       crate(serde-1/std) >= 1.0.0
Requires:       crate(serde-json-1/std) >= 1.0.0
Requires:       crate(wasm-bindgen-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-postgres
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "tokio-postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-postgres-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-postgres) = %{version}

%description -n %{name}+tokio-postgres
This metapackage enables feature "tokio-postgres" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "wasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-bindgen-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/wasm) = %{version}

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zmij
Summary:        Decimal number implementation written in pure Rust suitable for financial and fixed-precision calculations - feature "zmij"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zmij-1) >= 1.0.0
Provides:       crate(%{pkgname}/zmij) = %{version}

%description -n %{name}+zmij
This metapackage enables feature "zmij" for the Rust rust_decimal crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
