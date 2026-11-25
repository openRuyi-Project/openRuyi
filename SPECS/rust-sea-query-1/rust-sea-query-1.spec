# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sea-query
%global full_version 1.0.1
%global pkgname sea-query-1

Name:           rust-sea-query-1
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "sea-query"
License:        MIT OR Apache-2.0
URL:            https://github.com/SeaQL/sea-query
#!RemoteAsset:  sha256:8d190cfb3bcceb8a8d7d04dee5a0c77f60c7627979cdcb47fdcb8934f009badf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/audit) = %{version}
Provides:       crate(%{pkgname}/backend-mysql) = %{version}
Provides:       crate(%{pkgname}/backend-postgres) = %{version}
Provides:       crate(%{pkgname}/backend-sqlite) = %{version}
Provides:       crate(%{pkgname}/option-more-parentheses) = %{version}
Provides:       crate(%{pkgname}/option-postgres-use-serial) = %{version}
Provides:       crate(%{pkgname}/option-sqlite-exact-column-type) = %{version}
Provides:       crate(%{pkgname}/postgres-array) = %{version}
Provides:       crate(%{pkgname}/postgres-interval) = %{version}
Provides:       crate(%{pkgname}/tests-cfg) = %{version}
Provides:       crate(%{pkgname}/thread-safe) = %{version}

%description
Source code for takopackized Rust crate "sea-query"

%package     -n %{name}+all-features
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "all-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/all-types) = %{version}
Requires:       crate(%{pkgname}/attr) = %{version}
Requires:       crate(%{pkgname}/audit) = %{version}
Requires:       crate(%{pkgname}/backend-mysql) = %{version}
Requires:       crate(%{pkgname}/backend-postgres) = %{version}
Requires:       crate(%{pkgname}/backend-sqlite) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/hashable-value) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/sqlx-utils) = %{version}
Requires:       crate(%{pkgname}/thread-safe) = %{version}
Provides:       crate(%{pkgname}/all-features) = %{version}

%description -n %{name}+all-features
This metapackage enables feature "all-features" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-types
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "all-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/postgres-array) = %{version}
Requires:       crate(%{pkgname}/postgres-interval) = %{version}
Requires:       crate(%{pkgname}/postgres-range) = %{version}
Requires:       crate(%{pkgname}/postgres-vector) = %{version}
Requires:       crate(%{pkgname}/with-bigdecimal) = %{version}
Requires:       crate(%{pkgname}/with-chrono) = %{version}
Requires:       crate(%{pkgname}/with-ipnetwork) = %{version}
Requires:       crate(%{pkgname}/with-jiff) = %{version}
Requires:       crate(%{pkgname}/with-json) = %{version}
Requires:       crate(%{pkgname}/with-mac-address) = %{version}
Requires:       crate(%{pkgname}/with-rust-decimal) = %{version}
Requires:       crate(%{pkgname}/with-time) = %{version}
Requires:       crate(%{pkgname}/with-uuid) = %{version}
Provides:       crate(%{pkgname}/all-types) = %{version}

%description -n %{name}+all-types
This metapackage enables feature "all-types" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigdecimal
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "bigdecimal" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bigdecimal-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/bigdecimal) = %{version}
Provides:       crate(%{pkgname}/with-bigdecimal) = %{version}

%description -n %{name}+bigdecimal
This metapackage enables feature "bigdecimal" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-bigdecimal" feature.

%package     -n %{name}+chrono
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "chrono" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Provides:       crate(%{pkgname}/chrono) = %{version}
Provides:       crate(%{pkgname}/with-chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-chrono" feature.

%package     -n %{name}+default
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/audit) = %{version}
Requires:       crate(%{pkgname}/backend-mysql) = %{version}
Requires:       crate(%{pkgname}/backend-postgres) = %{version}
Requires:       crate(%{pkgname}/backend-sqlite) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/itoa) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnetwork
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "ipnetwork" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnetwork-0.21) >= 0.21.1
Provides:       crate(%{pkgname}/ipnetwork) = %{version}
Provides:       crate(%{pkgname}/with-ipnetwork) = %{version}

%description -n %{name}+ipnetwork
This metapackage enables feature "ipnetwork" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-ipnetwork" feature.

%package     -n %{name}+itoa
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "itoa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(itoa-1/default) >= 1.0.15
Provides:       crate(%{pkgname}/itoa) = %{version}

%description -n %{name}+itoa
This metapackage enables feature "itoa" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jiff
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "jiff" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-0.2/perf-inline) >= 0.2.15
Requires:       crate(jiff-0.2/std) >= 0.2.15
Provides:       crate(%{pkgname}/jiff) = %{version}
Provides:       crate(%{pkgname}/with-jiff) = %{version}

%description -n %{name}+jiff
This metapackage enables feature "jiff" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-jiff" feature.

%package     -n %{name}+mac-address
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "mac_address" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mac-address-1) >= 1.1.0
Provides:       crate(%{pkgname}/mac-address) = %{version}
Provides:       crate(%{pkgname}/with-mac-address) = %{version}

%description -n %{name}+mac-address
This metapackage enables feature "mac_address" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-mac_address" feature.

%package     -n %{name}+ordered-float
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "ordered-float" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ordered-float-4) >= 4.6.0
Provides:       crate(%{pkgname}/hashable-value) = %{version}
Provides:       crate(%{pkgname}/ordered-float) = %{version}

%description -n %{name}+ordered-float
This metapackage enables feature "ordered-float" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "hashable-value" feature.

%package     -n %{name}+pgvector
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "pgvector" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pgvector-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/pgvector) = %{version}
Provides:       crate(%{pkgname}/postgres-vector) = %{version}

%description -n %{name}+pgvector
This metapackage enables feature "pgvector" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "postgres-vector" feature.

%package     -n %{name}+postgres-range
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "postgres-range"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-postgres-types-0.1/range) >= 0.1.1
Provides:       crate(%{pkgname}/postgres-range) = %{version}

%description -n %{name}+postgres-range
This metapackage enables feature "postgres-range" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "rust_decimal" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1) >= 1.0.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}
Provides:       crate(%{pkgname}/with-rust-decimal) = %{version}

%description -n %{name}+rust-decimal
This metapackage enables feature "rust_decimal" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-rust_decimal" feature.

%package     -n %{name}+sea-query-derive
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "sea-query-derive" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-derive-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/attr) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/sea-orm) = %{version}
Provides:       crate(%{pkgname}/sea-query-derive) = %{version}
Provides:       crate(%{pkgname}/sqlx-utils) = %{version}

%description -n %{name}+sea-query-derive
This metapackage enables feature "sea-query-derive" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "attr", "derive", "sea-orm", and "sqlx-utils" features.

%package     -n %{name}+sea-query-postgres-types
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "sea-query-postgres-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-postgres-types-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}/sea-query-postgres-types) = %{version}

%description -n %{name}+sea-query-postgres-types
This metapackage enables feature "sea-query-postgres-types" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bigdecimal-0.4/serde) >= 0.4.0
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(chrono-0.4/serde) >= 0.4.40
Requires:       crate(ipnetwork-0.21/serde) >= 0.21.1
Requires:       crate(jiff-0.2/perf-inline) >= 0.2.15
Requires:       crate(jiff-0.2/serde) >= 0.2.15
Requires:       crate(jiff-0.2/std) >= 0.2.15
Requires:       crate(mac-address-1/serde) >= 1.1.0
Requires:       crate(pgvector-0.4/serde) >= 0.4.0
Requires:       crate(rust-decimal-1/serde) >= 1.0.0
Requires:       crate(sea-query-postgres-types-0.1/serde) >= 0.1.1
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/rc) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/macros) >= 0.3.47
Requires:       crate(time-0.3/serde) >= 0.3.47
Requires:       crate(uuid-1/serde) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "serde_json" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/with-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-json" feature.

%package     -n %{name}+time
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "time" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/macros) >= 0.3.47
Provides:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/with-time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-time" feature.

%package     -n %{name}+uuid
Summary:        🔱 A dynamic query builder for MySQL, Postgres and SQLite - feature "uuid" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1) >= 1.0.0
Provides:       crate(%{pkgname}/uuid) = %{version}
Provides:       crate(%{pkgname}/with-uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust sea-query crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-uuid" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
