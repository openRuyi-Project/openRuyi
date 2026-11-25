# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sea-query-sqlx
%global full_version 0.9.1
%global pkgname sea-query-sqlx-0.9

Name:           rust-sea-query-sqlx-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "sea-query-sqlx"
License:        MIT OR Apache-2.0
URL:            https://github.com/SeaQL/sea-query
#!RemoteAsset:  sha256:4eaa419cdb9157da1361186b1959983eb2ea0dcb9a3c69dc45c449ecb2af8fef
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(sea-query-1/thread-safe) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unimplemented-jiff-sqlx) = %{version}
Provides:       crate(%{pkgname}/unimplemented-jiff-sqlx-mysql) = %{version}

%description
Source code for takopackized Rust crate "sea-query-sqlx"

%package     -n %{name}+ipnetwork
Summary:        Driver library for using SeaQuery with SQLx - feature "ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnetwork-0.21) >= 0.21.1
Provides:       crate(%{pkgname}/ipnetwork) = %{version}

%description -n %{name}+ipnetwork
This metapackage enables feature "ipnetwork" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jiff
Summary:        Driver library for using SeaQuery with SQLx - feature "jiff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-0.2/perf-inline) >= 0.2.15
Requires:       crate(jiff-0.2/std) >= 0.2.15
Provides:       crate(%{pkgname}/jiff) = %{version}

%description -n %{name}+jiff
This metapackage enables feature "jiff" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jiff-sqlx
Summary:        Driver library for using SeaQuery with SQLx - feature "jiff-sqlx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-sqlx-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/jiff-sqlx) = %{version}

%description -n %{name}+jiff-sqlx
This metapackage enables feature "jiff-sqlx" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pgvector
Summary:        Driver library for using SeaQuery with SQLx - feature "pgvector"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pgvector-0.4) >= 0.4.2
Provides:       crate(%{pkgname}/pgvector) = %{version}

%description -n %{name}+pgvector
This metapackage enables feature "pgvector" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postgres-array
Summary:        Driver library for using SeaQuery with SQLx - feature "postgres-array"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/postgres-array) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Provides:       crate(%{pkgname}/postgres-array) = %{version}

%description -n %{name}+postgres-array
This metapackage enables feature "postgres-array" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postgres-vector
Summary:        Driver library for using SeaQuery with SQLx - feature "postgres-vector"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pgvector-0.4/sqlx) >= 0.4.2
Requires:       crate(sea-query-1/postgres-vector) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Provides:       crate(%{pkgname}/postgres-vector) = %{version}

%description -n %{name}+postgres-vector
This metapackage enables feature "postgres-vector" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-actix
Summary:        Driver library for using SeaQuery with SQLx - feature "runtime-actix" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-actix) = %{version}
Provides:       crate(%{pkgname}/runtime-tokio) = %{version}

%description -n %{name}+runtime-actix
This metapackage enables feature "runtime-actix" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "runtime-tokio" feature.

%package     -n %{name}+runtime-actix-native-tls
Summary:        Driver library for using SeaQuery with SQLx - feature "runtime-actix-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/runtime-actix) = %{version}
Requires:       crate(%{pkgname}/tls-native-tls) = %{version}
Provides:       crate(%{pkgname}/runtime-actix-native-tls) = %{version}

%description -n %{name}+runtime-actix-native-tls
This metapackage enables feature "runtime-actix-native-tls" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-actix-rustls
Summary:        Driver library for using SeaQuery with SQLx - feature "runtime-actix-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/runtime-actix) = %{version}
Requires:       crate(%{pkgname}/tls-rustls) = %{version}
Provides:       crate(%{pkgname}/runtime-actix-rustls) = %{version}

%description -n %{name}+runtime-actix-rustls
This metapackage enables feature "runtime-actix-rustls" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std
Summary:        Driver library for using SeaQuery with SQLx - feature "runtime-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/runtime-async-std) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-async-std) = %{version}

%description -n %{name}+runtime-async-std
This metapackage enables feature "runtime-async-std" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std-native-tls
Summary:        Driver library for using SeaQuery with SQLx - feature "runtime-async-std-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/runtime-async-std) = %{version}
Requires:       crate(%{pkgname}/tls-native-tls) = %{version}
Provides:       crate(%{pkgname}/runtime-async-std-native-tls) = %{version}

%description -n %{name}+runtime-async-std-native-tls
This metapackage enables feature "runtime-async-std-native-tls" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std-rustls
Summary:        Driver library for using SeaQuery with SQLx - feature "runtime-async-std-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/runtime-async-std) = %{version}
Requires:       crate(%{pkgname}/tls-rustls) = %{version}
Provides:       crate(%{pkgname}/runtime-async-std-rustls) = %{version}

%description -n %{name}+runtime-async-std-rustls
This metapackage enables feature "runtime-async-std-rustls" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio-native-tls
Summary:        Driver library for using SeaQuery with SQLx - feature "runtime-tokio-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/runtime-tokio) = %{version}
Requires:       crate(%{pkgname}/tls-native-tls) = %{version}
Provides:       crate(%{pkgname}/runtime-tokio-native-tls) = %{version}

%description -n %{name}+runtime-tokio-native-tls
This metapackage enables feature "runtime-tokio-native-tls" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio-rustls
Summary:        Driver library for using SeaQuery with SQLx - feature "runtime-tokio-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/runtime-tokio) = %{version}
Requires:       crate(%{pkgname}/tls-rustls) = %{version}
Provides:       crate(%{pkgname}/runtime-tokio-rustls) = %{version}

%description -n %{name}+runtime-tokio-rustls
This metapackage enables feature "runtime-tokio-rustls" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx
Summary:        Driver library for using SeaQuery with SQLx - feature "sqlx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx) = %{version}

%description -n %{name}+sqlx
This metapackage enables feature "sqlx" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-any
Summary:        Driver library for using SeaQuery with SQLx - feature "sqlx-any"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/any) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-any) = %{version}

%description -n %{name}+sqlx-any
This metapackage enables feature "sqlx-any" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-mysql
Summary:        Driver library for using SeaQuery with SQLx - feature "sqlx-mysql"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/mysql) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-mysql) = %{version}

%description -n %{name}+sqlx-mysql
This metapackage enables feature "sqlx-mysql" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-postgres
Summary:        Driver library for using SeaQuery with SQLx - feature "sqlx-postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sqlx-0.9/postgres) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-postgres) = %{version}

%description -n %{name}+sqlx-postgres
This metapackage enables feature "sqlx-postgres" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-sqlite
Summary:        Driver library for using SeaQuery with SQLx - feature "sqlx-sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/sqlite) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-sqlite) = %{version}

%description -n %{name}+sqlx-sqlite
This metapackage enables feature "sqlx-sqlite" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-native-tls
Summary:        Driver library for using SeaQuery with SQLx - feature "tls-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/tls-native-tls) >= 0.9.0
Provides:       crate(%{pkgname}/tls-native-tls) = %{version}

%description -n %{name}+tls-native-tls
This metapackage enables feature "tls-native-tls" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-none
Summary:        Driver library for using SeaQuery with SQLx - feature "tls-none"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/tls-none) >= 0.9.0
Provides:       crate(%{pkgname}/tls-none) = %{version}

%description -n %{name}+tls-none
This metapackage enables feature "tls-none" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls
Summary:        Driver library for using SeaQuery with SQLx - feature "tls-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/tls-rustls) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls) = %{version}

%description -n %{name}+tls-rustls
This metapackage enables feature "tls-rustls" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-aws-lc-rs
Summary:        Driver library for using SeaQuery with SQLx - feature "tls-rustls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/tls-rustls-aws-lc-rs) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-aws-lc-rs) = %{version}

%description -n %{name}+tls-rustls-aws-lc-rs
This metapackage enables feature "tls-rustls-aws-lc-rs" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring
Summary:        Driver library for using SeaQuery with SQLx - feature "tls-rustls-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/tls-rustls-ring) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-ring) = %{version}

%description -n %{name}+tls-rustls-ring
This metapackage enables feature "tls-rustls-ring" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring-native-roots
Summary:        Driver library for using SeaQuery with SQLx - feature "tls-rustls-ring-native-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/tls-rustls-ring-native-roots) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-ring-native-roots) = %{version}

%description -n %{name}+tls-rustls-ring-native-roots
This metapackage enables feature "tls-rustls-ring-native-roots" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring-webpki
Summary:        Driver library for using SeaQuery with SQLx - feature "tls-rustls-ring-webpki"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9/tls-rustls-ring-webpki) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-ring-webpki) = %{version}

%description -n %{name}+tls-rustls-ring-webpki
This metapackage enables feature "tls-rustls-ring-webpki" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-bigdecimal
Summary:        Driver library for using SeaQuery with SQLx - feature "with-bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-bigdecimal) >= 1.0.0
Requires:       crate(sqlx-0.9/bigdecimal) >= 0.9.0
Provides:       crate(%{pkgname}/with-bigdecimal) = %{version}

%description -n %{name}+with-bigdecimal
This metapackage enables feature "with-bigdecimal" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-chrono
Summary:        Driver library for using SeaQuery with SQLx - feature "with-chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-chrono) >= 1.0.0
Requires:       crate(sqlx-0.9/chrono) >= 0.9.0
Provides:       crate(%{pkgname}/with-chrono) = %{version}

%description -n %{name}+with-chrono
This metapackage enables feature "with-chrono" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-ipnetwork
Summary:        Driver library for using SeaQuery with SQLx - feature "with-ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-ipnetwork) >= 1.0.0
Requires:       crate(sqlx-0.9/ipnetwork) >= 0.9.0
Provides:       crate(%{pkgname}/with-ipnetwork) = %{version}

%description -n %{name}+with-ipnetwork
This metapackage enables feature "with-ipnetwork" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-jiff
Summary:        Driver library for using SeaQuery with SQLx - feature "with-jiff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/jiff) = %{version}
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-jiff) >= 1.0.0
Provides:       crate(%{pkgname}/with-jiff) = %{version}

%description -n %{name}+with-jiff
This metapackage enables feature "with-jiff" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-json
Summary:        Driver library for using SeaQuery with SQLx - feature "with-json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-json) >= 1.0.0
Requires:       crate(sqlx-0.9/json) >= 0.9.0
Provides:       crate(%{pkgname}/with-json) = %{version}

%description -n %{name}+with-json
This metapackage enables feature "with-json" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-mac-address
Summary:        Driver library for using SeaQuery with SQLx - feature "with-mac_address"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-mac-address) >= 1.0.0
Requires:       crate(sqlx-0.9/mac-address) >= 0.9.0
Provides:       crate(%{pkgname}/with-mac-address) = %{version}

%description -n %{name}+with-mac-address
This metapackage enables feature "with-mac_address" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-rust-decimal
Summary:        Driver library for using SeaQuery with SQLx - feature "with-rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-rust-decimal) >= 1.0.0
Requires:       crate(sqlx-0.9/rust-decimal) >= 0.9.0
Provides:       crate(%{pkgname}/with-rust-decimal) = %{version}

%description -n %{name}+with-rust-decimal
This metapackage enables feature "with-rust_decimal" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-time
Summary:        Driver library for using SeaQuery with SQLx - feature "with-time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-time) >= 1.0.0
Requires:       crate(sqlx-0.9/time) >= 0.9.0
Provides:       crate(%{pkgname}/with-time) = %{version}

%description -n %{name}+with-time
This metapackage enables feature "with-time" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-uuid
Summary:        Driver library for using SeaQuery with SQLx - feature "with-uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) >= 1.0.0
Requires:       crate(sea-query-1/with-uuid) >= 1.0.0
Requires:       crate(sqlx-0.9/uuid) >= 0.9.0
Provides:       crate(%{pkgname}/with-uuid) = %{version}

%description -n %{name}+with-uuid
This metapackage enables feature "with-uuid" for the Rust sea-query-sqlx crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
