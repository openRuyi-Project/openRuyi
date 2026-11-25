# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sea-schema
%global full_version 0.18.1
%global pkgname sea-schema-0.18

Name:           rust-sea-schema-0.18
Version:        0.18.1
Release:        %autorelease
Summary:        Rust crate "sea-schema"
License:        MIT OR Apache-2.0
URL:            https://github.com/SeaQL/sea-schema
#!RemoteAsset:  sha256:3553c77dceed56e95bece9ea876c4dd67ca879ef51055a0b97a7bb89a8ae4fed
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1) >= 0.1.0
Requires:       crate(sea-query-1/derive) >= 1.0.0
Requires:       crate(sea-schema-derive-0.3) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/def) = %{version}
Provides:       crate(%{pkgname}/discovery) = %{version}
Provides:       crate(%{pkgname}/parser) = %{version}
Provides:       crate(%{pkgname}/planetscale) = %{version}
Provides:       crate(%{pkgname}/probe) = %{version}
Provides:       crate(%{pkgname}/query) = %{version}
Provides:       crate(%{pkgname}/rusqlite) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}
Provides:       crate(%{pkgname}/writer) = %{version}

%description
Source code for takopackized Rust crate "sea-schema"

%package     -n %{name}+default
Summary:        🌿 SQL schema definition and discovery - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/discovery) = %{version}
Requires:       crate(%{pkgname}/mysql) = %{version}
Requires:       crate(%{pkgname}/postgres) = %{version}
Requires:       crate(%{pkgname}/probe) = %{version}
Requires:       crate(%{pkgname}/sqlite) = %{version}
Requires:       crate(%{pkgname}/writer) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        🌿 SQL schema definition and discovery - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/debug-print) = %{version}
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "debug-print" feature.

%package     -n %{name}+mysql
Summary:        🌿 SQL schema definition and discovery - feature "mysql"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/backend-mysql) >= 1.0.0
Requires:       crate(sea-query-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/mysql) = %{version}

%description -n %{name}+mysql
This metapackage enables feature "mysql" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postgres
Summary:        🌿 SQL schema definition and discovery - feature "postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/backend-postgres) >= 1.0.0
Requires:       crate(sea-query-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/postgres) = %{version}

%description -n %{name}+postgres
This metapackage enables feature "postgres" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postgres-vector
Summary:        🌿 SQL schema definition and discovery - feature "postgres-vector"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/derive) >= 1.0.0
Requires:       crate(sea-query-1/postgres-vector) >= 1.0.0
Requires:       crate(sea-query-sqlx-0.9/postgres-vector) >= 0.9.0
Provides:       crate(%{pkgname}/postgres-vector) = %{version}

%description -n %{name}+postgres-vector
This metapackage enables feature "postgres-vector" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-actix
Summary:        🌿 SQL schema definition and discovery - feature "runtime-actix"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9/runtime-actix) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-actix) = %{version}

%description -n %{name}+runtime-actix
This metapackage enables feature "runtime-actix" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-actix-native-tls
Summary:        🌿 SQL schema definition and discovery - feature "runtime-actix-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9/runtime-actix-native-tls) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Requires:       crate(sqlx-0.9/tls-native-tls) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-actix-native-tls) = %{version}

%description -n %{name}+runtime-actix-native-tls
This metapackage enables feature "runtime-actix-native-tls" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-actix-rustls
Summary:        🌿 SQL schema definition and discovery - feature "runtime-actix-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9/runtime-actix-rustls) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Requires:       crate(sqlx-0.9/tls-rustls) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-actix-rustls) = %{version}

%description -n %{name}+runtime-actix-rustls
This metapackage enables feature "runtime-actix-rustls" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std
Summary:        🌿 SQL schema definition and discovery - feature "runtime-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9/runtime-async-std) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-async-std) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-async-std) = %{version}

%description -n %{name}+runtime-async-std
This metapackage enables feature "runtime-async-std" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std-native-tls
Summary:        🌿 SQL schema definition and discovery - feature "runtime-async-std-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9/runtime-async-std-native-tls) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-async-std) >= 0.9.0
Requires:       crate(sqlx-0.9/tls-native-tls) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-async-std-native-tls) = %{version}

%description -n %{name}+runtime-async-std-native-tls
This metapackage enables feature "runtime-async-std-native-tls" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std-rustls
Summary:        🌿 SQL schema definition and discovery - feature "runtime-async-std-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9/runtime-async-std-rustls) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-async-std) >= 0.9.0
Requires:       crate(sqlx-0.9/tls-rustls) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-async-std-rustls) = %{version}

%description -n %{name}+runtime-async-std-rustls
This metapackage enables feature "runtime-async-std-rustls" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio
Summary:        🌿 SQL schema definition and discovery - feature "runtime-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9/runtime-tokio) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-tokio) = %{version}

%description -n %{name}+runtime-tokio
This metapackage enables feature "runtime-tokio" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio-native-tls
Summary:        🌿 SQL schema definition and discovery - feature "runtime-tokio-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9/runtime-tokio-native-tls) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Requires:       crate(sqlx-0.9/tls-native-tls) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-tokio-native-tls) = %{version}

%description -n %{name}+runtime-tokio-native-tls
This metapackage enables feature "runtime-tokio-native-tls" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio-rustls
Summary:        🌿 SQL schema definition and discovery - feature "runtime-tokio-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9/runtime-tokio-rustls) >= 0.9.0
Requires:       crate(sqlx-0.9/runtime-tokio) >= 0.9.0
Requires:       crate(sqlx-0.9/tls-rustls) >= 0.9.0
Provides:       crate(%{pkgname}/runtime-tokio-rustls) = %{version}

%description -n %{name}+runtime-tokio-rustls
This metapackage enables feature "runtime-tokio-rustls" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sea-query-sqlx
Summary:        🌿 SQL schema definition and discovery - feature "sea-query-sqlx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-sqlx-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/sea-query-sqlx) = %{version}

%description -n %{name}+sea-query-sqlx
This metapackage enables feature "sea-query-sqlx" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        🌿 SQL schema definition and discovery - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/with-serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-serde" feature.

%package     -n %{name}+sqlite
Summary:        🌿 SQL schema definition and discovery - feature "sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/backend-sqlite) >= 1.0.0
Requires:       crate(sea-query-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/sqlite) = %{version}

%description -n %{name}+sqlite
This metapackage enables feature "sqlite" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx
Summary:        🌿 SQL schema definition and discovery - feature "sqlx" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx) = %{version}
Provides:       crate(%{pkgname}/sqlx-dep) = %{version}

%description -n %{name}+sqlx
This metapackage enables feature "sqlx" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "sqlx-dep" feature.

%package     -n %{name}+sqlx-all
Summary:        🌿 SQL schema definition and discovery - feature "sqlx-all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlx-mysql) = %{version}
Requires:       crate(%{pkgname}/sqlx-postgres) = %{version}
Requires:       crate(%{pkgname}/sqlx-sqlite) = %{version}
Provides:       crate(%{pkgname}/sqlx-all) = %{version}

%description -n %{name}+sqlx-all
This metapackage enables feature "sqlx-all" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-mysql
Summary:        🌿 SQL schema definition and discovery - feature "sqlx-mysql"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mysql) = %{version}
Requires:       crate(%{pkgname}/sqlx-dep) = %{version}
Requires:       crate(sea-query-sqlx-0.9/sqlx-mysql) >= 0.9.0
Requires:       crate(sqlx-0.9/mysql) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-mysql) = %{version}

%description -n %{name}+sqlx-mysql
This metapackage enables feature "sqlx-mysql" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-postgres
Summary:        🌿 SQL schema definition and discovery - feature "sqlx-postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/postgres) = %{version}
Requires:       crate(%{pkgname}/sqlx-dep) = %{version}
Requires:       crate(sea-query-sqlx-0.9/sqlx-postgres) >= 0.9.0
Requires:       crate(sqlx-0.9/postgres) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-postgres) = %{version}

%description -n %{name}+sqlx-postgres
This metapackage enables feature "sqlx-postgres" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-sqlite
Summary:        🌿 SQL schema definition and discovery - feature "sqlx-sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sqlite) = %{version}
Requires:       crate(%{pkgname}/sqlx-dep) = %{version}
Requires:       crate(sea-query-sqlx-0.9/sqlx-sqlite) >= 0.9.0
Requires:       crate(sqlx-0.9/sqlite) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-sqlite) = %{version}

%description -n %{name}+sqlx-sqlite
This metapackage enables feature "sqlx-sqlite" for the Rust sea-schema crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
