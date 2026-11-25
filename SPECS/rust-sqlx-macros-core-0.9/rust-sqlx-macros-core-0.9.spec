# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sqlx-macros-core
%global full_version 0.9.0
%global pkgname sqlx-macros-core-0.9

Name:           rust-sqlx-macros-core-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "sqlx-macros-core"
License:        MIT OR Apache-2.0
URL:            https://github.com/launchbadge/sqlx
#!RemoteAsset:  sha256:fb8d96de5fdc85a5c4ec813432b523ec637e80ba98f046555f75f7908ddac7c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(dotenvy-0.15) >= 0.15.7
Requires:       crate(either-1/default) >= 1.6.1
Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(proc-macro2-1) >= 1.0.83
Requires:       crate(quote-1) >= 1.0.35
Requires:       crate(serde-1/default) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(serde-json-1/default) >= 1.0.142
Requires:       crate(sha2-0.10/default) >= 0.10.0
Requires:       crate(sqlx-core-0.9/default) >= 0.9.0
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(syn-2/clone-impls) >= 2.0.87
Requires:       crate(syn-2/derive) >= 2.0.87
Requires:       crate(syn-2/full) >= 2.0.87
Requires:       crate(syn-2/parsing) >= 2.0.87
Requires:       crate(syn-2/printing) >= 2.0.87
Requires:       crate(url-2/default) >= 2.2.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/sqlite) = %{version}

%description
Not intended to be used directly.
Source code for takopackized Rust crate "sqlx-macros-core"

%package     -n %{name}+rt-async-global-executor
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "_rt-async-global-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-global-executor) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/rt-async-global-executor) >= 0.9.0
Provides:       crate(%{pkgname}/rt-async-global-executor) = %{version}

%description -n %{name}+rt-async-global-executor
Not intended to be used directly.
This metapackage enables feature "_rt-async-global-executor" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-async-std
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "_rt-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-std) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/rt-async-std) >= 0.9.0
Provides:       crate(%{pkgname}/rt-async-std) = %{version}

%description -n %{name}+rt-async-std
Not intended to be used directly.
This metapackage enables feature "_rt-async-std" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-smol
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "_rt-smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/smol) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/rt-smol) >= 0.9.0
Provides:       crate(%{pkgname}/rt-smol) = %{version}

%description -n %{name}+rt-smol
Not intended to be used directly.
This metapackage enables feature "_rt-smol" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-tokio
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "_rt-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/rt-tokio) >= 0.9.0
Provides:       crate(%{pkgname}/rt-tokio) = %{version}

%description -n %{name}+rt-tokio
Not intended to be used directly.
This metapackage enables feature "_rt-tokio" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-native-tls
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "_tls-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/tls-native-tls) >= 0.9.0
Provides:       crate(%{pkgname}/tls-native-tls) = %{version}

%description -n %{name}+tls-native-tls
Not intended to be used directly.
This metapackage enables feature "_tls-native-tls" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-aws-lc-rs
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "_tls-rustls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/tls-rustls-aws-lc-rs) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-aws-lc-rs) = %{version}

%description -n %{name}+tls-rustls-aws-lc-rs
Not intended to be used directly.
This metapackage enables feature "_tls-rustls-aws-lc-rs" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring-native-roots
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "_tls-rustls-ring-native-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/tls-rustls-ring-native-roots) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-ring-native-roots) = %{version}

%description -n %{name}+tls-rustls-ring-native-roots
Not intended to be used directly.
This metapackage enables feature "_tls-rustls-ring-native-roots" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring-webpki
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "_tls-rustls-ring-webpki"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/tls-rustls-ring-webpki) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-ring-webpki) = %{version}

%description -n %{name}+tls-rustls-ring-webpki
Not intended to be used directly.
This metapackage enables feature "_tls-rustls-ring-webpki" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-global-executor
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "async-global-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-global-executor-3/async-io) >= 3.1.0
Provides:       crate(%{pkgname}/async-global-executor) = %{version}

%description -n %{name}+async-global-executor
Not intended to be used directly.
This metapackage enables feature "async-global-executor" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.13.0
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
Not intended to be used directly.
This metapackage enables feature "async-std" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigdecimal
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/bigdecimal) >= 0.9.0
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/bigdecimal) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/bigdecimal) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/bigdecimal) = %{version}

%description -n %{name}+bigdecimal
Not intended to be used directly.
This metapackage enables feature "bigdecimal" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bit-vec
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "bit-vec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/bit-vec) >= 0.9.0
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/bit-vec) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/bit-vec) = %{version}

%description -n %{name}+bit-vec
Not intended to be used directly.
This metapackage enables feature "bit-vec" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/chrono) >= 0.9.0
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/chrono) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/chrono) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/chrono) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
Not intended to be used directly.
This metapackage enables feature "chrono" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnet
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "ipnet"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/ipnet) >= 0.9.0
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/ipnet) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/ipnet) = %{version}

%description -n %{name}+ipnet
Not intended to be used directly.
This metapackage enables feature "ipnet" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnetwork
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/ipnetwork) >= 0.9.0
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/ipnetwork) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/ipnetwork) = %{version}

%description -n %{name}+ipnetwork
Not intended to be used directly.
This metapackage enables feature "ipnetwork" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/json) >= 0.9.0
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/json) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/json) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/json) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
Not intended to be used directly.
This metapackage enables feature "json" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mac-address
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "mac_address"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/mac-address) >= 0.9.0
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/mac-address) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/mac-address) = %{version}

%description -n %{name}+mac-address
Not intended to be used directly.
This metapackage enables feature "mac_address" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+migrate
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "migrate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/migrate) = %{version}

%description -n %{name}+migrate
Not intended to be used directly.
This metapackage enables feature "migrate" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mysql-rsa
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "mysql-rsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mysql) = %{version}
Requires:       crate(sqlx-mysql-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/rsa) >= 0.9.0
Provides:       crate(%{pkgname}/mysql-rsa) = %{version}

%description -n %{name}+mysql-rsa
Not intended to be used directly.
This metapackage enables feature "mysql-rsa" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/rust-decimal) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/rust-decimal) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/rust-decimal) >= 0.9.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
Not intended to be used directly.
This metapackage enables feature "rust_decimal" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smol-2) >= 2.0.0
Provides:       crate(%{pkgname}/smol) = %{version}

%description -n %{name}+smol
Not intended to be used directly.
This metapackage enables feature "smol" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlite) = %{version}
Requires:       crate(sqlx-sqlite-0.9/bundled) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite) = %{version}

%description -n %{name}+sqlite
Not intended to be used directly.
This metapackage enables feature "sqlite" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite-load-extension
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "sqlite-load-extension"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-sqlite-0.9/load-extension) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite-load-extension) = %{version}

%description -n %{name}+sqlite-load-extension
Not intended to be used directly.
This metapackage enables feature "sqlite-load-extension" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite-unbundled
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "sqlite-unbundled"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlite) = %{version}
Requires:       crate(sqlx-sqlite-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/unbundled) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite-unbundled) = %{version}

%description -n %{name}+sqlite-unbundled
Not intended to be used directly.
This metapackage enables feature "sqlite-unbundled" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-mysql
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "sqlx-mysql" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-mysql-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/mysql) = %{version}
Provides:       crate(%{pkgname}/sqlx-mysql) = %{version}

%description -n %{name}+sqlx-mysql
Not intended to be used directly.
This metapackage enables feature "sqlx-mysql" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "mysql" feature.

%package     -n %{name}+sqlx-postgres
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "sqlx-postgres" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-postgres-0.9/default) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/postgres) = %{version}
Provides:       crate(%{pkgname}/sqlx-postgres) = %{version}

%description -n %{name}+sqlx-postgres
Not intended to be used directly.
This metapackage enables feature "sqlx-postgres" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "postgres" feature.

%package     -n %{name}+sqlx-sqlite
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "sqlx-sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-sqlite-0.9/default) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-sqlite) = %{version}

%description -n %{name}+sqlx-sqlite
Not intended to be used directly.
This metapackage enables feature "sqlx-sqlite" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-toml
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "sqlx-toml"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/sqlx-toml) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/sqlx-toml) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-toml) = %{version}

%description -n %{name}+sqlx-toml
Not intended to be used directly.
This metapackage enables feature "sqlx-toml" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thiserror
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "thiserror" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(thiserror-2/std) >= 2.0.18
Provides:       crate(%{pkgname}/macros) = %{version}
Provides:       crate(%{pkgname}/thiserror) = %{version}

%description -n %{name}+thiserror
Not intended to be used directly.
This metapackage enables feature "thiserror" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "macros" feature.

%package     -n %{name}+time
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/time) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/time) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/time) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/time) >= 0.9.0
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
Not intended to be used directly.
This metapackage enables feature "time" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/fs) >= 1.25.0
Requires:       crate(tokio-1/io-util) >= 1.25.0
Requires:       crate(tokio-1/net) >= 1.25.0
Requires:       crate(tokio-1/rt) >= 1.25.0
Requires:       crate(tokio-1/sync) >= 1.25.0
Requires:       crate(tokio-1/time) >= 1.25.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
Not intended to be used directly.
This metapackage enables feature "tokio" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Macro support core for SQLx, the Rust SQL toolkit - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-core-0.9/uuid) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/uuid) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/uuid) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/uuid) >= 0.9.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
Not intended to be used directly.
This metapackage enables feature "uuid" for the Rust sqlx-macros-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
