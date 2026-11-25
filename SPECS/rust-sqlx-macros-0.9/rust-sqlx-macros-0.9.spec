# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sqlx-macros
%global full_version 0.9.0
%global pkgname sqlx-macros-0.9

Name:           rust-sqlx-macros-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "sqlx-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/launchbadge/sqlx
#!RemoteAsset:  sha256:bd2b84f2bc39a5705ef27ec785a11c934a41bbd4a24941e257927cddc26b60bf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1) >= 1.0.83
Requires:       crate(quote-1) >= 1.0.35
Requires:       crate(sqlx-core-0.9/any) >= 0.9.0
Requires:       crate(sqlx-core-0.9/default) >= 0.9.0
Requires:       crate(sqlx-macros-core-0.9/default) >= 0.9.0
Requires:       crate(syn-2/parsing) >= 2.0.87
Requires:       crate(syn-2/proc-macro) >= 2.0.87

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Not intended to be used directly.
Source code for takopackized Rust crate "sqlx-macros"

%package     -n %{name}+rt-async-global-executor
Summary:        Macros for SQLx, the rust SQL toolkit - feature "_rt-async-global-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/rt-async-global-executor) >= 0.9.0
Provides:       crate(%{pkgname}/rt-async-global-executor) = %{version}

%description -n %{name}+rt-async-global-executor
Not intended to be used directly.
This metapackage enables feature "_rt-async-global-executor" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-async-std
Summary:        Macros for SQLx, the rust SQL toolkit - feature "_rt-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/rt-async-std) >= 0.9.0
Provides:       crate(%{pkgname}/rt-async-std) = %{version}

%description -n %{name}+rt-async-std
Not intended to be used directly.
This metapackage enables feature "_rt-async-std" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-smol
Summary:        Macros for SQLx, the rust SQL toolkit - feature "_rt-smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/rt-smol) >= 0.9.0
Provides:       crate(%{pkgname}/rt-smol) = %{version}

%description -n %{name}+rt-smol
Not intended to be used directly.
This metapackage enables feature "_rt-smol" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-tokio
Summary:        Macros for SQLx, the rust SQL toolkit - feature "_rt-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/rt-tokio) >= 0.9.0
Provides:       crate(%{pkgname}/rt-tokio) = %{version}

%description -n %{name}+rt-tokio
Not intended to be used directly.
This metapackage enables feature "_rt-tokio" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-native-tls
Summary:        Macros for SQLx, the rust SQL toolkit - feature "_tls-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/tls-native-tls) >= 0.9.0
Provides:       crate(%{pkgname}/tls-native-tls) = %{version}

%description -n %{name}+tls-native-tls
Not intended to be used directly.
This metapackage enables feature "_tls-native-tls" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-aws-lc-rs
Summary:        Macros for SQLx, the rust SQL toolkit - feature "_tls-rustls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/tls-rustls-aws-lc-rs) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-aws-lc-rs) = %{version}

%description -n %{name}+tls-rustls-aws-lc-rs
Not intended to be used directly.
This metapackage enables feature "_tls-rustls-aws-lc-rs" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring-native-roots
Summary:        Macros for SQLx, the rust SQL toolkit - feature "_tls-rustls-ring-native-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/tls-rustls-ring-native-roots) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-ring-native-roots) = %{version}

%description -n %{name}+tls-rustls-ring-native-roots
Not intended to be used directly.
This metapackage enables feature "_tls-rustls-ring-native-roots" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring-webpki
Summary:        Macros for SQLx, the rust SQL toolkit - feature "_tls-rustls-ring-webpki"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/tls-rustls-ring-webpki) >= 0.9.0
Provides:       crate(%{pkgname}/tls-rustls-ring-webpki) = %{version}

%description -n %{name}+tls-rustls-ring-webpki
Not intended to be used directly.
This metapackage enables feature "_tls-rustls-ring-webpki" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigdecimal
Summary:        Macros for SQLx, the rust SQL toolkit - feature "bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/bigdecimal) >= 0.9.0
Provides:       crate(%{pkgname}/bigdecimal) = %{version}

%description -n %{name}+bigdecimal
Not intended to be used directly.
This metapackage enables feature "bigdecimal" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bit-vec
Summary:        Macros for SQLx, the rust SQL toolkit - feature "bit-vec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/bit-vec) >= 0.9.0
Provides:       crate(%{pkgname}/bit-vec) = %{version}

%description -n %{name}+bit-vec
Not intended to be used directly.
This metapackage enables feature "bit-vec" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Macros for SQLx, the rust SQL toolkit - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/chrono) >= 0.9.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
Not intended to be used directly.
This metapackage enables feature "chrono" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Macros for SQLx, the rust SQL toolkit - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/derive) >= 0.9.0
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
Not intended to be used directly.
This metapackage enables feature "derive" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnet
Summary:        Macros for SQLx, the rust SQL toolkit - feature "ipnet"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/ipnet) >= 0.9.0
Provides:       crate(%{pkgname}/ipnet) = %{version}

%description -n %{name}+ipnet
Not intended to be used directly.
This metapackage enables feature "ipnet" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnetwork
Summary:        Macros for SQLx, the rust SQL toolkit - feature "ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/ipnetwork) >= 0.9.0
Provides:       crate(%{pkgname}/ipnetwork) = %{version}

%description -n %{name}+ipnetwork
Not intended to be used directly.
This metapackage enables feature "ipnetwork" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Macros for SQLx, the rust SQL toolkit - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/json) >= 0.9.0
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
Not intended to be used directly.
This metapackage enables feature "json" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mac-address
Summary:        Macros for SQLx, the rust SQL toolkit - feature "mac_address"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/mac-address) >= 0.9.0
Provides:       crate(%{pkgname}/mac-address) = %{version}

%description -n %{name}+mac-address
Not intended to be used directly.
This metapackage enables feature "mac_address" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Macros for SQLx, the rust SQL toolkit - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/macros) >= 0.9.0
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
Not intended to be used directly.
This metapackage enables feature "macros" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+migrate
Summary:        Macros for SQLx, the rust SQL toolkit - feature "migrate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/migrate) >= 0.9.0
Provides:       crate(%{pkgname}/migrate) = %{version}

%description -n %{name}+migrate
Not intended to be used directly.
This metapackage enables feature "migrate" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mysql
Summary:        Macros for SQLx, the rust SQL toolkit - feature "mysql"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/mysql) >= 0.9.0
Provides:       crate(%{pkgname}/mysql) = %{version}

%description -n %{name}+mysql
Not intended to be used directly.
This metapackage enables feature "mysql" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mysql-rsa
Summary:        Macros for SQLx, the rust SQL toolkit - feature "mysql-rsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/mysql-rsa) >= 0.9.0
Provides:       crate(%{pkgname}/mysql-rsa) = %{version}

%description -n %{name}+mysql-rsa
Not intended to be used directly.
This metapackage enables feature "mysql-rsa" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postgres
Summary:        Macros for SQLx, the rust SQL toolkit - feature "postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/postgres) >= 0.9.0
Provides:       crate(%{pkgname}/postgres) = %{version}

%description -n %{name}+postgres
Not intended to be used directly.
This metapackage enables feature "postgres" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        Macros for SQLx, the rust SQL toolkit - feature "rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/rust-decimal) >= 0.9.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
Not intended to be used directly.
This metapackage enables feature "rust_decimal" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite
Summary:        Macros for SQLx, the rust SQL toolkit - feature "sqlite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/sqlite) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite) = %{version}

%description -n %{name}+sqlite
Not intended to be used directly.
This metapackage enables feature "sqlite" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite-load-extension
Summary:        Macros for SQLx, the rust SQL toolkit - feature "sqlite-load-extension"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/sqlite-load-extension) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite-load-extension) = %{version}

%description -n %{name}+sqlite-load-extension
Not intended to be used directly.
This metapackage enables feature "sqlite-load-extension" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlite-unbundled
Summary:        Macros for SQLx, the rust SQL toolkit - feature "sqlite-unbundled"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/sqlite-unbundled) >= 0.9.0
Provides:       crate(%{pkgname}/sqlite-unbundled) = %{version}

%description -n %{name}+sqlite-unbundled
Not intended to be used directly.
This metapackage enables feature "sqlite-unbundled" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-toml
Summary:        Macros for SQLx, the rust SQL toolkit - feature "sqlx-toml"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/sqlx-toml) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-toml) = %{version}

%description -n %{name}+sqlx-toml
Not intended to be used directly.
This metapackage enables feature "sqlx-toml" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Macros for SQLx, the rust SQL toolkit - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/time) >= 0.9.0
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
Not intended to be used directly.
This metapackage enables feature "time" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Macros for SQLx, the rust SQL toolkit - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-macros-core-0.9/uuid) >= 0.9.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
Not intended to be used directly.
This metapackage enables feature "uuid" for the Rust sqlx-macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
