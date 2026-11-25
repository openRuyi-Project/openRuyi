# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sea-orm
%global full_version 2.0.0
%global pkgname sea-orm-2

Name:           rust-sea-orm-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "sea-orm"
License:        MIT OR Apache-2.0
URL:            https://www.sea-ql.org/SeaORM
#!RemoteAsset:  sha256:549c6d29a2e7a84e35c5dfbc06370a62c4d35f2328c31005267bec586b34f682
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
Patch2000:      2000-pin-sea-orm-arrow-prerelease.patch
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-stream-0.3) >= 0.3.0
Requires:       crate(async-trait-0.1) >= 0.1.0
Requires:       crate(derive-more-2/debug) >= 2.0.0
Requires:       crate(derive-more-2/default) >= 2.0.0
Requires:       crate(derive-where-1/default) >= 1.6.1
Requires:       crate(futures-util-0.3/std) >= 0.3.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(log-0.4) >= 0.4.0
Requires:       crate(sea-orm-macros-2/async) >= 2.0.0
Requires:       crate(sea-orm-macros-2/strum) >= 2.0.0
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(strum-0.28) >= 0.28.0
Requires:       crate(thiserror-2) >= 2.0.0
Requires:       crate(tracing-0.1/attributes) >= 0.1.0
Requires:       crate(tracing-0.1/log) >= 0.1.0
Requires:       crate(url-2) >= 2.2.0
Requires:       crate(web-time-1) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug-print) = %{version}
Provides:       crate(%{pkgname}/mariadb-use-returning) = %{version}
Provides:       crate(%{pkgname}/mock) = %{version}
Provides:       crate(%{pkgname}/rusqlite) = %{version}
Provides:       crate(%{pkgname}/sea-orm-internal) = %{version}
Provides:       crate(%{pkgname}/sqlite-no-row-value-before-3-15) = %{version}
Provides:       crate(%{pkgname}/sqlite-use-returning-for-3-35) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}
Provides:       crate(%{pkgname}/tracing-spans) = %{version}

%description
Source code for takopackized Rust crate "sea-orm"

%package     -n %{name}+bigdecimal
Summary:        🐚 An async & dynamic ORM for Rust - feature "bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bigdecimal-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/bigdecimal) = %{version}

%description -n %{name}+bigdecimal
This metapackage enables feature "bigdecimal" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        🐚 An async & dynamic ORM for Rust - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4) >= 0.4.30
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        🐚 An async & dynamic ORM for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/sqlite-use-returning-for-3-35) = %{version}
Requires:       crate(%{pkgname}/stream) = %{version}
Requires:       crate(%{pkgname}/with-chrono) = %{version}
Requires:       crate(%{pkgname}/with-json) = %{version}
Requires:       crate(%{pkgname}/with-rust-decimal) = %{version}
Requires:       crate(%{pkgname}/with-time) = %{version}
Requires:       crate(%{pkgname}/with-uuid) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+entity-registry
Summary:        🐚 An async & dynamic ORM for Rust - feature "entity-registry"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/inventory) = %{version}
Requires:       crate(sea-orm-macros-2/async) >= 2.0.0
Requires:       crate(sea-orm-macros-2/entity-registry) >= 2.0.0
Requires:       crate(sea-orm-macros-2/strum) >= 2.0.0
Provides:       crate(%{pkgname}/entity-registry) = %{version}

%description -n %{name}+entity-registry
This metapackage enables feature "entity-registry" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inventory
Summary:        🐚 An async & dynamic ORM for Rust - feature "inventory"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(inventory-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/inventory) = %{version}

%description -n %{name}+inventory
This metapackage enables feature "inventory" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnetwork
Summary:        🐚 An async & dynamic ORM for Rust - feature "ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnetwork-0.21/serde) >= 0.21.0
Provides:       crate(%{pkgname}/ipnetwork) = %{version}

%description -n %{name}+ipnetwork
This metapackage enables feature "ipnetwork" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mac-address
Summary:        🐚 An async & dynamic ORM for Rust - feature "mac_address"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mac-address-1) >= 1.1.0
Provides:       crate(%{pkgname}/mac-address) = %{version}

%description -n %{name}+mac-address
This metapackage enables feature "mac_address" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        🐚 An async & dynamic ORM for Rust - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-orm-macros-2/async) >= 2.0.0
Requires:       crate(sea-orm-macros-2/derive) >= 2.0.0
Requires:       crate(sea-orm-macros-2/strum) >= 2.0.0
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pgvector
Summary:        🐚 An async & dynamic ORM for Rust - feature "pgvector"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pgvector-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/pgvector) = %{version}

%description -n %{name}+pgvector
This metapackage enables feature "pgvector" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postgres-array
Summary:        🐚 An async & dynamic ORM for Rust - feature "postgres-array" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-orm-macros-2/async) >= 2.0.0
Requires:       crate(sea-orm-macros-2/postgres-array) >= 2.0.0
Requires:       crate(sea-orm-macros-2/strum) >= 2.0.0
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/postgres-array) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/postgres-array) >= 0.9.0
Provides:       crate(%{pkgname}/json-array) = %{version}
Provides:       crate(%{pkgname}/postgres-array) = %{version}

%description -n %{name}+postgres-array
This metapackage enables feature "postgres-array" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json-array" feature.

%package     -n %{name}+postgres-use-serial-pk
Summary:        🐚 An async & dynamic ORM for Rust - feature "postgres-use-serial-pk"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/option-postgres-use-serial) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Provides:       crate(%{pkgname}/postgres-use-serial-pk) = %{version}

%description -n %{name}+postgres-use-serial-pk
This metapackage enables feature "postgres-use-serial-pk" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postgres-vector
Summary:        🐚 An async & dynamic ORM for Rust - feature "postgres-vector"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pgvector) = %{version}
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/postgres-vector) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/postgres-vector) >= 0.9.0
Provides:       crate(%{pkgname}/postgres-vector) = %{version}

%description -n %{name}+postgres-vector
This metapackage enables feature "postgres-vector" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proxy
Summary:        🐚 An async & dynamic ORM for Rust - feature "proxy" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/proxy) = %{version}
Provides:       crate(%{pkgname}/tests-cfg) = %{version}

%description -n %{name}+proxy
This metapackage enables feature "proxy" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tests-cfg" feature.

%package     -n %{name}+rbac
Summary:        🐚 An async & dynamic ORM for Rust - feature "rbac"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(sea-query-1/audit) >= 1.0.0
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Provides:       crate(%{pkgname}/rbac) = %{version}

%description -n %{name}+rbac
This metapackage enables feature "rbac" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std
Summary:        🐚 An async & dynamic ORM for Rust - feature "runtime-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/runtime-async-std) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-async-std) = %{version}

%description -n %{name}+runtime-async-std
This metapackage enables feature "runtime-async-std" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std-native-tls
Summary:        🐚 An async & dynamic ORM for Rust - feature "runtime-async-std-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/runtime-async-std) = %{version}
Requires:       crate(sqlx-0.9/tls-native-tls) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-async-std-native-tls) = %{version}

%description -n %{name}+runtime-async-std-native-tls
This metapackage enables feature "runtime-async-std-native-tls" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std-rustls
Summary:        🐚 An async & dynamic ORM for Rust - feature "runtime-async-std-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/runtime-async-std) = %{version}
Requires:       crate(sqlx-0.9/tls-rustls) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-async-std-rustls) = %{version}

%description -n %{name}+runtime-async-std-rustls
This metapackage enables feature "runtime-async-std-rustls" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio
Summary:        🐚 An async & dynamic ORM for Rust - feature "runtime-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-tokio) = %{version}

%description -n %{name}+runtime-tokio
This metapackage enables feature "runtime-tokio" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio-native-tls
Summary:        🐚 An async & dynamic ORM for Rust - feature "runtime-tokio-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/runtime-tokio) = %{version}
Requires:       crate(sqlx-0.9/tls-native-tls) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-tokio-native-tls) = %{version}

%description -n %{name}+runtime-tokio-native-tls
This metapackage enables feature "runtime-tokio-native-tls" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio-rustls
Summary:        🐚 An async & dynamic ORM for Rust - feature "runtime-tokio-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/runtime-tokio) = %{version}
Requires:       crate(sqlx-0.9/tls-rustls) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-tokio-rustls) = %{version}

%description -n %{name}+runtime-tokio-rustls
This metapackage enables feature "runtime-tokio-rustls" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        🐚 An async & dynamic ORM for Rust - feature "rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
This metapackage enables feature "rust_decimal" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sea-orm-arrow
Summary:        🐚 An async & dynamic ORM for Rust - feature "sea-orm-arrow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-orm-arrow-2.0.0-rc.3) = 2.0.0
Provides:       crate(%{pkgname}/sea-orm-arrow) = %{version}

%description -n %{name}+sea-orm-arrow
This metapackage enables feature "sea-orm-arrow" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sea-query-sqlx
Summary:        🐚 An async & dynamic ORM for Rust - feature "sea-query-sqlx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/sea-query-sqlx) = %{version}

%description -n %{name}+sea-query-sqlx
This metapackage enables feature "sea-query-sqlx" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sea-schema
Summary:        🐚 An async & dynamic ORM for Rust - feature "sea-schema" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-schema-0.18/discovery) >= 0.18.1
Requires:       crate(sea-schema-0.18/probe) >= 0.18.1
Requires:       crate(sea-schema-0.18/writer) >= 0.18.1
Provides:       crate(%{pkgname}/schema-sync) = %{version}
Provides:       crate(%{pkgname}/sea-schema) = %{version}

%description -n %{name}+sea-schema
This metapackage enables feature "sea-schema" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "schema-sync" feature.

%package     -n %{name}+seaography
Summary:        🐚 An async & dynamic ORM for Rust - feature "seaography"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-orm-macros-2/async) >= 2.0.0
Requires:       crate(sea-orm-macros-2/seaography) >= 2.0.0
Requires:       crate(sea-orm-macros-2/strum) >= 2.0.0
Provides:       crate(%{pkgname}/seaography) = %{version}

%description -n %{name}+seaography
This metapackage enables feature "seaography" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        🐚 An async & dynamic ORM for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(uuid-1/serde) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        🐚 An async & dynamic ORM for Rust - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx
Summary:        🐚 An async & dynamic ORM for Rust - feature "sqlx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx) = %{version}

%description -n %{name}+sqlx
This metapackage enables feature "sqlx" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-all
Summary:        🐚 An async & dynamic ORM for Rust - feature "sqlx-all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlx-mysql) = %{version}
Requires:       crate(%{pkgname}/sqlx-postgres) = %{version}
Requires:       crate(%{pkgname}/sqlx-sqlite) = %{version}
Provides:       crate(%{pkgname}/sqlx-all) = %{version}

%description -n %{name}+sqlx-all
This metapackage enables feature "sqlx-all" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-core
Summary:        🐚 An async & dynamic ORM for Rust - feature "sqlx-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-core) = %{version}

%description -n %{name}+sqlx-core
This metapackage enables feature "sqlx-core" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-dep
Summary:        🐚 An async & dynamic ORM for Rust - feature "sqlx-dep"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlx) = %{version}
Requires:       crate(%{pkgname}/sqlx-core) = %{version}
Provides:       crate(%{pkgname}/sqlx-dep) = %{version}

%description -n %{name}+sqlx-dep
This metapackage enables feature "sqlx-dep" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-mysql
Summary:        🐚 An async & dynamic ORM for Rust - feature "sqlx-mysql"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlx-dep) = %{version}
Requires:       crate(sea-query-sqlx-0.9/sqlx-mysql) >= 0.9.0
Requires:       crate(sea-schema-0.18/discovery) >= 0.18.1
Requires:       crate(sea-schema-0.18/probe) >= 0.18.1
Requires:       crate(sea-schema-0.18/sqlx-mysql) >= 0.18.1
Requires:       crate(sea-schema-0.18/writer) >= 0.18.1
Provides:       crate(%{pkgname}/sqlx-mysql) = %{version}

%description -n %{name}+sqlx-mysql
This metapackage enables feature "sqlx-mysql" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-postgres
Summary:        🐚 An async & dynamic ORM for Rust - feature "sqlx-postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/postgres-array) = %{version}
Requires:       crate(%{pkgname}/sqlx-dep) = %{version}
Requires:       crate(sea-orm-macros-2/async) >= 2.0.0
Requires:       crate(sea-orm-macros-2/sqlx-postgres) >= 2.0.0
Requires:       crate(sea-orm-macros-2/strum) >= 2.0.0
Requires:       crate(sea-query-sqlx-0.9/sqlx-postgres) >= 0.9.0
Requires:       crate(sea-schema-0.18/discovery) >= 0.18.1
Requires:       crate(sea-schema-0.18/probe) >= 0.18.1
Requires:       crate(sea-schema-0.18/sqlx-postgres) >= 0.18.1
Requires:       crate(sea-schema-0.18/writer) >= 0.18.1
Provides:       crate(%{pkgname}/sqlx-postgres) = %{version}

%description -n %{name}+sqlx-postgres
This metapackage enables feature "sqlx-postgres" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-sqlite
Summary:        🐚 An async & dynamic ORM for Rust - feature "sqlx-sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlx-dep) = %{version}
Requires:       crate(sea-query-sqlx-0.9/sqlx-sqlite) >= 0.9.0
Requires:       crate(sea-schema-0.18/discovery) >= 0.18.1
Requires:       crate(sea-schema-0.18/probe) >= 0.18.1
Requires:       crate(sea-schema-0.18/sqlx-sqlite) >= 0.18.1
Requires:       crate(sea-schema-0.18/writer) >= 0.18.1
Provides:       crate(%{pkgname}/sqlx-sqlite) = %{version}

%description -n %{name}+sqlx-sqlite
This metapackage enables feature "sqlx-sqlite" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stream
Summary:        🐚 An async & dynamic ORM for Rust - feature "stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ouroboros-0.18) >= 0.18.0
Provides:       crate(%{pkgname}/stream) = %{version}

%description -n %{name}+stream
This metapackage enables feature "stream" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tests-features
Summary:        🐚 An async & dynamic ORM for Rust - feature "tests-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/default) = %{version}
Requires:       crate(%{pkgname}/postgres-array) = %{version}
Requires:       crate(%{pkgname}/rbac) = %{version}
Requires:       crate(%{pkgname}/schema-sync) = %{version}
Requires:       crate(%{pkgname}/with-arrow) = %{version}
Requires:       crate(%{pkgname}/with-bigdecimal) = %{version}
Requires:       crate(%{pkgname}/with-ipnetwork) = %{version}
Provides:       crate(%{pkgname}/tests-features) = %{version}

%description -n %{name}+tests-features
This metapackage enables feature "tests-features" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        🐚 An async & dynamic ORM for Rust - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3) >= 0.3.36
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        🐚 An async & dynamic ORM for Rust - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1) >= 1.0.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-arrow
Summary:        🐚 An async & dynamic ORM for Rust - feature "with-arrow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sea-orm-arrow) = %{version}
Requires:       crate(sea-orm-macros-2/async) >= 2.0.0
Requires:       crate(sea-orm-macros-2/strum) >= 2.0.0
Requires:       crate(sea-orm-macros-2/with-arrow) >= 2.0.0
Provides:       crate(%{pkgname}/with-arrow) = %{version}

%description -n %{name}+with-arrow
This metapackage enables feature "with-arrow" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-bigdecimal
Summary:        🐚 An async & dynamic ORM for Rust - feature "with-bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bigdecimal) = %{version}
# Cargo enables this feature only when with-arrow is enabled.
Requires:       (crate(sea-orm-arrow-2.0.0-rc.3/with-bigdecimal) = 2.0.0 if crate(%{pkgname}/with-arrow) = %{version})
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-bigdecimal) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/with-bigdecimal) >= 0.9.0
Provides:       crate(%{pkgname}/with-bigdecimal) = %{version}

%description -n %{name}+with-bigdecimal
This metapackage enables feature "with-bigdecimal" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-chrono
Summary:        🐚 An async & dynamic ORM for Rust - feature "with-chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
# Cargo enables this feature only when with-arrow is enabled.
Requires:       (crate(sea-orm-arrow-2.0.0-rc.3/with-chrono) = 2.0.0 if crate(%{pkgname}/with-arrow) = %{version})
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-chrono) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/with-chrono) >= 0.9.0
Provides:       crate(%{pkgname}/with-chrono) = %{version}

%description -n %{name}+with-chrono
This metapackage enables feature "with-chrono" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-ipnetwork
Summary:        🐚 An async & dynamic ORM for Rust - feature "with-ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ipnetwork) = %{version}
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-ipnetwork) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/with-ipnetwork) >= 0.9.0
Provides:       crate(%{pkgname}/with-ipnetwork) = %{version}

%description -n %{name}+with-ipnetwork
This metapackage enables feature "with-ipnetwork" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-json
Summary:        🐚 An async & dynamic ORM for Rust - feature "with-json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(bigdecimal-0.4/serde) >= 0.4.0
Requires:       crate(bigdecimal-0.4/std) >= 0.4.0
Requires:       crate(chrono-0.4/serde) >= 0.4.30
Requires:       crate(mac-address-1/serde) >= 1.1.0
Requires:       crate(pgvector-0.4/serde) >= 0.4.0
Requires:       crate(rust-decimal-1/serde) >= 1.0.0
Requires:       crate(rust-decimal-1/std) >= 1.0.0
Requires:       crate(sea-orm-macros-2/async) >= 2.0.0
Requires:       crate(sea-orm-macros-2/strum) >= 2.0.0
Requires:       crate(sea-orm-macros-2/with-json) >= 2.0.0
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-json) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/with-json) >= 0.9.0
Requires:       crate(serde-1) >= 1.0.0
Requires:       crate(time-0.3/serde) >= 0.3.36
Requires:       crate(uuid-1/serde) >= 1.0.0
Provides:       crate(%{pkgname}/with-json) = %{version}

%description -n %{name}+with-json
This metapackage enables feature "with-json" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-mac-address
Summary:        🐚 An async & dynamic ORM for Rust - feature "with-mac_address"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mac-address) = %{version}
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-mac-address) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/with-mac-address) >= 0.9.0
Provides:       crate(%{pkgname}/with-mac-address) = %{version}

%description -n %{name}+with-mac-address
This metapackage enables feature "with-mac_address" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-rust-decimal
Summary:        🐚 An async & dynamic ORM for Rust - feature "with-rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rust-decimal) = %{version}
# Cargo enables this feature only when with-arrow is enabled.
Requires:       (crate(sea-orm-arrow-2.0.0-rc.3/with-rust-decimal) = 2.0.0 if crate(%{pkgname}/with-arrow) = %{version})
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-rust-decimal) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/with-rust-decimal) >= 0.9.0
Provides:       crate(%{pkgname}/with-rust-decimal) = %{version}

%description -n %{name}+with-rust-decimal
This metapackage enables feature "with-rust_decimal" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-time
Summary:        🐚 An async & dynamic ORM for Rust - feature "with-time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
# Cargo enables this feature only when with-arrow is enabled.
Requires:       (crate(sea-orm-arrow-2.0.0-rc.3/with-time) = 2.0.0 if crate(%{pkgname}/with-arrow) = %{version})
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-time) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/with-time) >= 0.9.0
Provides:       crate(%{pkgname}/with-time) = %{version}

%description -n %{name}+with-time
This metapackage enables feature "with-time" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-uuid
Summary:        🐚 An async & dynamic ORM for Rust - feature "with-uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/uuid) = %{version}
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/hashable-value) >= 1.0.0
Requires:       crate(sea-query-1/sea-orm) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-uuid) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/with-uuid) >= 0.9.0
Provides:       crate(%{pkgname}/with-uuid) = %{version}

%description -n %{name}+with-uuid
This metapackage enables feature "with-uuid" for the Rust sea-orm crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
