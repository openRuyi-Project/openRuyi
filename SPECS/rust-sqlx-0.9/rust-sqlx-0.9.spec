# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sqlx
%global full_version 0.9.0
%global pkgname sqlx-0.9

Name:           rust-sqlx-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "sqlx"
License:        MIT OR Apache-2.0
URL:            https://github.com/launchbadge/sqlx
#!RemoteAsset:  sha256:378620ccc25c62c89d8be1c819e76a88d59bdcc3304733330788948e619bfd71
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(sqlx-core-0.9/default) >= 0.9.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/rt-async-global-executor) = %{version}
Provides:       crate(%{pkgname}/rt-async-std) = %{version}
Provides:       crate(%{pkgname}/rt-smol) = %{version}
Provides:       crate(%{pkgname}/rt-tokio) = %{version}
Provides:       crate(%{pkgname}/sqlite) = %{version}
Provides:       crate(%{pkgname}/tls-none) = %{version}

%description
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
Source code for takopackized Rust crate "sqlx"

%package     -n %{name}+unstable-all-types
Summary:        🧰 The Rust SQL Toolkit - feature "_unstable-all-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bigdecimal) = %{version}
Requires:       crate(%{pkgname}/bit-vec) = %{version}
Requires:       crate(%{pkgname}/bstr) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/ipnet) = %{version}
Requires:       crate(%{pkgname}/ipnetwork) = %{version}
Requires:       crate(%{pkgname}/json) = %{version}
Requires:       crate(%{pkgname}/mac-address) = %{version}
Requires:       crate(%{pkgname}/rust-decimal) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Requires:       crate(%{pkgname}/uuid) = %{version}
Provides:       crate(%{pkgname}/unstable-all-types) = %{version}

%description -n %{name}+unstable-all-types
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "_unstable-all-types" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-docs
Summary:        🧰 The Rust SQL Toolkit - feature "_unstable-docs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/all-databases) = %{version}
Requires:       crate(%{pkgname}/unstable-all-types) = %{version}
Requires:       crate(sqlx-sqlite-0.9/unstable-docs) >= 0.9.0
Provides:       crate(%{pkgname}/unstable-docs) = %{version}

%description -n %{name}+unstable-docs
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "_unstable-docs" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-databases
Summary:        🧰 The Rust SQL Toolkit - feature "all-databases"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any) = %{version}
Requires:       crate(%{pkgname}/mysql) = %{version}
Requires:       crate(%{pkgname}/postgres) = %{version}
Requires:       crate(%{pkgname}/sqlite) = %{version}
Provides:       crate(%{pkgname}/all-databases) = %{version}

%description -n %{name}+all-databases
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "all-databases" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+any
Summary:        🧰 The Rust SQL Toolkit - feature "any"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/any) >= 0.9.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/any) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/any) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/any) >= 0.9.0
Provides:       crate(%{pkgname}/any) = %{version}

%description -n %{name}+any
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "any" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigdecimal
Summary:        🧰 The Rust SQL Toolkit - feature "bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/bigdecimal) >= 0.9.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/bigdecimal) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/bigdecimal) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/bigdecimal) >= 0.9.0
Provides:       crate(%{pkgname}/bigdecimal) = %{version}

%description -n %{name}+bigdecimal
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "bigdecimal" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bit-vec
Summary:        🧰 The Rust SQL Toolkit - feature "bit-vec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/bit-vec) >= 0.9.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/bit-vec) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/bit-vec) >= 0.9.0
Provides:       crate(%{pkgname}/bit-vec) = %{version}

%description -n %{name}+bit-vec
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "bit-vec" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bstr
Summary:        🧰 The Rust SQL Toolkit - feature "bstr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/bstr) >= 0.9.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Provides:       crate(%{pkgname}/bstr) = %{version}

%description -n %{name}+bstr
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "bstr" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        🧰 The Rust SQL Toolkit - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/chrono) >= 0.9.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/chrono) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/chrono) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/chrono) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/chrono) >= 0.9.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "chrono" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        🧰 The Rust SQL Toolkit - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any) = %{version}
Requires:       crate(%{pkgname}/json) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/migrate) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "default" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        🧰 The Rust SQL Toolkit - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-0.9/derive) >= 0.9.0
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "derive" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnet
Summary:        🧰 The Rust SQL Toolkit - feature "ipnet"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/ipnet) >= 0.9.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/ipnet) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/ipnet) >= 0.9.0
Provides:       crate(%{pkgname}/ipnet) = %{version}

%description -n %{name}+ipnet
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "ipnet" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnetwork
Summary:        🧰 The Rust SQL Toolkit - feature "ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/ipnetwork) >= 0.9.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/ipnetwork) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/ipnetwork) >= 0.9.0
Provides:       crate(%{pkgname}/ipnetwork) = %{version}

%description -n %{name}+ipnetwork
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "ipnetwork" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        🧰 The Rust SQL Toolkit - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/json) >= 0.9.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/json) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/json) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/json) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/json) >= 0.9.0
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "json" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mac-address
Summary:        🧰 The Rust SQL Toolkit - feature "mac_address"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/mac-address) >= 0.9.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/mac-address) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/mac-address) >= 0.9.0
Provides:       crate(%{pkgname}/mac-address) = %{version}

%description -n %{name}+mac-address
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "mac_address" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        🧰 The Rust SQL Toolkit - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/macros) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/offline) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "macros" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+migrate
Summary:        🧰 The Rust SQL Toolkit - feature "migrate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/migrate) >= 0.9.0
Provides:       crate(%{pkgname}/migrate) = %{version}

%description -n %{name}+migrate
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "migrate" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mysql
Summary:        🧰 The Rust SQL Toolkit - feature "mysql"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlx-mysql) = %{version}
Requires:       crate(sqlx-macros-0.9/mysql) >= 0.9.0
Provides:       crate(%{pkgname}/mysql) = %{version}

%description -n %{name}+mysql
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "mysql" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mysql-rsa
Summary:        🧰 The Rust SQL Toolkit - feature "mysql-rsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mysql) = %{version}
Requires:       crate(sqlx-macros-0.9/mysql-rsa) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/rsa) >= 0.9.0
Provides:       crate(%{pkgname}/mysql-rsa) = %{version}

%description -n %{name}+mysql-rsa
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "mysql-rsa" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postgres
Summary:        🧰 The Rust SQL Toolkit - feature "postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlx-postgres) = %{version}
Requires:       crate(sqlx-macros-0.9/postgres) >= 0.9.0
Provides:       crate(%{pkgname}/postgres) = %{version}

%description -n %{name}+postgres
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "postgres" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regexp
Summary:        🧰 The Rust SQL Toolkit - feature "regexp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-sqlite-0.9/regexp) >= 0.9.0
Provides:       crate(%{pkgname}/regexp) = %{version}

%description -n %{name}+regexp
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "regexp" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-global-executor
Summary:        🧰 The Rust SQL Toolkit - feature "runtime-async-global-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rt-async-global-executor) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/rt-async-global-executor) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/rt-async-global-executor) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-async-global-executor) = %{version}

%description -n %{name}+runtime-async-global-executor
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "runtime-async-global-executor" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std
Summary:        🧰 The Rust SQL Toolkit - feature "runtime-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rt-async-std) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/rt-async-std) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/rt-async-std) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-async-std) = %{version}

%description -n %{name}+runtime-async-std
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "runtime-async-std" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-smol
Summary:        🧰 The Rust SQL Toolkit - feature "runtime-smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rt-smol) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/rt-smol) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/rt-smol) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-smol) = %{version}

%description -n %{name}+runtime-smol
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "runtime-smol" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio
Summary:        🧰 The Rust SQL Toolkit - feature "runtime-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rt-tokio) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/rt-tokio) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/rt-tokio) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-tokio) = %{version}

%description -n %{name}+runtime-tokio
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "runtime-tokio" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        🧰 The Rust SQL Toolkit - feature "rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/rust-decimal) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/rust-decimal) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/rust-decimal) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/rust-decimal) >= 0.9.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "rust_decimal" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite
Summary:        🧰 The Rust SQL Toolkit - feature "sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlite-bundled) = %{version}
Requires:       crate(%{pkgname}/sqlite-deserialize) = %{version}
Requires:       crate(%{pkgname}/sqlite-load-extension) = %{version}
Requires:       crate(%{pkgname}/sqlite-unlock-notify) = %{version}
Provides:       crate(%{pkgname}/sqlite) = %{version}

%description -n %{name}+sqlite
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlite" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite-bundled
Summary:        🧰 The Rust SQL Toolkit - feature "sqlite-bundled"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlite) = %{version}
Requires:       crate(sqlx-macros-0.9/sqlite) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/bundled) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite-bundled) = %{version}

%description -n %{name}+sqlite-bundled
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlite-bundled" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite-deserialize
Summary:        🧰 The Rust SQL Toolkit - feature "sqlite-deserialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-sqlite-0.9/deserialize) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite-deserialize) = %{version}

%description -n %{name}+sqlite-deserialize
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlite-deserialize" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite-load-extension
Summary:        🧰 The Rust SQL Toolkit - feature "sqlite-load-extension"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-0.9/sqlite-load-extension) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/load-extension) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite-load-extension) = %{version}

%description -n %{name}+sqlite-load-extension
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlite-load-extension" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite-preupdate-hook
Summary:        🧰 The Rust SQL Toolkit - feature "sqlite-preupdate-hook"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-sqlite-0.9/preupdate-hook) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite-preupdate-hook) = %{version}

%description -n %{name}+sqlite-preupdate-hook
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlite-preupdate-hook" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite-unbundled
Summary:        🧰 The Rust SQL Toolkit - feature "sqlite-unbundled"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlite) = %{version}
Requires:       crate(sqlx-macros-0.9/sqlite-unbundled) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/unbundled) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite-unbundled) = %{version}

%description -n %{name}+sqlite-unbundled
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlite-unbundled" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite-unlock-notify
Summary:        🧰 The Rust SQL Toolkit - feature "sqlite-unlock-notify"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-sqlite-0.9/unlock-notify) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite-unlock-notify) = %{version}

%description -n %{name}+sqlite-unlock-notify
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlite-unlock-notify" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-macros
Summary:        🧰 The Rust SQL Toolkit - feature "sqlx-macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-macros) = %{version}

%description -n %{name}+sqlx-macros
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlx-macros" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-mysql
Summary:        🧰 The Rust SQL Toolkit - feature "sqlx-mysql"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-mysql-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-mysql) = %{version}

%description -n %{name}+sqlx-mysql
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlx-mysql" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-postgres
Summary:        🧰 The Rust SQL Toolkit - feature "sqlx-postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-postgres-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-postgres) = %{version}

%description -n %{name}+sqlx-postgres
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlx-postgres" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-sqlite
Summary:        🧰 The Rust SQL Toolkit - feature "sqlx-sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-sqlite-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-sqlite) = %{version}

%description -n %{name}+sqlx-sqlite
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlx-sqlite" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-toml
Summary:        🧰 The Rust SQL Toolkit - feature "sqlx-toml"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/sqlx-toml) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/sqlx-toml) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/sqlx-toml) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-toml) = %{version}

%description -n %{name}+sqlx-toml
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "sqlx-toml" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        🧰 The Rust SQL Toolkit - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/time) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/time) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/time) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/time) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/time) >= 0.9.0
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "time" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-native-tls
Summary:        🧰 The Rust SQL Toolkit - feature "tls-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/tls-native-tls) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/tls-native-tls) >= 0.9.0
Provides:       crate(%{pkgname}/tls-native-tls) = %{version}

%description -n %{name}+tls-native-tls
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "tls-native-tls" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-aws-lc-rs
Summary:        🧰 The Rust SQL Toolkit - feature "tls-rustls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/tls-rustls-aws-lc-rs) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/tls-rustls-aws-lc-rs) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-aws-lc-rs) = %{version}

%description -n %{name}+tls-rustls-aws-lc-rs
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "tls-rustls-aws-lc-rs" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring-native-roots
Summary:        🧰 The Rust SQL Toolkit - feature "tls-rustls-ring-native-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/tls-rustls-ring-native-roots) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/tls-rustls-ring-native-roots) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-ring-native-roots) = %{version}

%description -n %{name}+tls-rustls-ring-native-roots
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "tls-rustls-ring-native-roots" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring-webpki
Summary:        🧰 The Rust SQL Toolkit - feature "tls-rustls-ring-webpki" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/tls-rustls-ring-webpki) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/tls-rustls-ring-webpki) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls) = %{version}
Provides:       crate(%{pkgname}/tls-rustls-ring) = %{version}
Provides:       crate(%{pkgname}/tls-rustls-ring-webpki) = %{version}

%description -n %{name}+tls-rustls-ring-webpki
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "tls-rustls-ring-webpki" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tls-rustls", and "tls-rustls-ring" features.

%package     -n %{name}+uuid
Summary:        🧰 The Rust SQL Toolkit - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Requires:       crate(sqlx-core-0.9/uuid) >= 0.9.0
Requires:       crate(sqlx-macros-0.9/uuid) >= 0.9.0
Requires:       crate(sqlx-mysql-0.9/uuid) >= 0.9.0
Requires:       crate(sqlx-postgres-0.9/uuid) >= 0.9.0
Requires:       crate(sqlx-sqlite-0.9/uuid) >= 0.9.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.
This metapackage enables feature "uuid" for the Rust sqlx crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
