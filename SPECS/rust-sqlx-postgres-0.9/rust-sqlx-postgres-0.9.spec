# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sqlx-postgres
%global full_version 0.9.0
%global pkgname sqlx-postgres-0.9

Name:           rust-sqlx-postgres-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "sqlx-postgres"
License:        MIT OR Apache-2.0
URL:            https://github.com/launchbadge/sqlx
#!RemoteAsset:  sha256:87a2bdd6e83f6b3ea525ca9fee568030508b58355a43d0b2c1674d5f79dcd65e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atoi-2/default) >= 2.0.0
Requires:       crate(base64-0.22/alloc) >= 0.22.1
Requires:       crate(bitflags-2) >= 2.4.0
Requires:       crate(byteorder-1/std) >= 1.4.3
Requires:       crate(dotenvy-0.15) >= 0.15.7
Requires:       crate(etcetera-0.11/default) >= 0.11.0
Requires:       crate(futures-channel-0.3/alloc) >= 0.3.32
Requires:       crate(futures-channel-0.3/sink) >= 0.3.32
Requires:       crate(futures-channel-0.3/std) >= 0.3.32
Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(futures-util-0.3/alloc) >= 0.3.32
Requires:       crate(futures-util-0.3/io) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(hkdf-0.13/default) >= 0.13.0
Requires:       crate(hmac-0.13) >= 0.13.0
Requires:       crate(itoa-1/default) >= 1.0.5
Requires:       crate(log-0.4/default) >= 0.4.18
Requires:       crate(md-5-0.11) >= 0.11.0
Requires:       crate(memchr-2) >= 2.5.0
Requires:       crate(rand-0.10/thread-rng) >= 0.10.1
Requires:       crate(sha2-0.11) >= 0.11.0
Requires:       crate(smallvec-1/default) >= 1.13.1
Requires:       crate(sqlx-core-0.9/default) >= 0.9.0
Requires:       crate(stringprep-0.1/default) >= 0.1.2
Requires:       crate(thiserror-2/std) >= 2.0.18
Requires:       crate(tracing-0.1/default) >= 0.1.37
Requires:       crate(tracing-0.1/log) >= 0.1.37
Requires:       crate(whoami-2) >= 2.0.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Not for direct use; see the `sqlx` crate for details.
Source code for takopackized Rust crate "sqlx-postgres"

%package     -n %{name}+any
Summary:        PostgreSQL driver implementation for SQLx - feature "any"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/any) >= 0.9.0
Provides:       crate(%{pkgname}/any) = %{version}

%description -n %{name}+any
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "any" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigdecimal
Summary:        PostgreSQL driver implementation for SQLx - feature "bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bigdecimal-0.4/default) >= 0.4.0
Requires:       crate(num-bigint-0.4/default) >= 0.4.3
Requires:       crate(sqlx-core-0.9/bigdecimal) >= 0.9.0
Provides:       crate(%{pkgname}/bigdecimal) = %{version}

%description -n %{name}+bigdecimal
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "bigdecimal" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bit-vec
Summary:        PostgreSQL driver implementation for SQLx - feature "bit-vec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bit-vec-0.8/default) >= 0.8.0
Requires:       crate(sqlx-core-0.9/bit-vec) >= 0.9.0
Provides:       crate(%{pkgname}/bit-vec) = %{version}

%description -n %{name}+bit-vec
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "bit-vec" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        PostgreSQL driver implementation for SQLx - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.34
Requires:       crate(chrono-0.4/std) >= 0.4.34
Requires:       crate(sqlx-core-0.9/chrono) >= 0.9.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "chrono" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnet
Summary:        PostgreSQL driver implementation for SQLx - feature "ipnet"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnet-2/default) >= 2.3.0
Requires:       crate(sqlx-core-0.9/ipnet) >= 0.9.0
Provides:       crate(%{pkgname}/ipnet) = %{version}

%description -n %{name}+ipnet
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "ipnet" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnetwork
Summary:        PostgreSQL driver implementation for SQLx - feature "ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnetwork-0.21/default) >= 0.21.1
Requires:       crate(sqlx-core-0.9/ipnetwork) >= 0.9.0
Provides:       crate(%{pkgname}/ipnetwork) = %{version}

%description -n %{name}+ipnetwork
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "ipnetwork" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        PostgreSQL driver implementation for SQLx - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(serde-json-1/default) >= 1.0.142
Requires:       crate(serde-json-1/raw-value) >= 1.0.142
Requires:       crate(sqlx-core-0.9/json) >= 0.9.0
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "json" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mac-address
Summary:        PostgreSQL driver implementation for SQLx - feature "mac_address"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mac-address-1/default) >= 1.1.5
Requires:       crate(sqlx-core-0.9/mac-address) >= 0.9.0
Provides:       crate(%{pkgname}/mac-address) = %{version}

%description -n %{name}+mac-address
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "mac_address" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+migrate
Summary:        PostgreSQL driver implementation for SQLx - feature "migrate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crc-3/default) >= 3.0.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Provides:       crate(%{pkgname}/migrate) = %{version}

%description -n %{name}+migrate
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "migrate" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+offline
Summary:        PostgreSQL driver implementation for SQLx - feature "offline"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/json) = %{version}
Requires:       crate(smallvec-1/serde) >= 1.13.1
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/offline) = %{version}

%description -n %{name}+offline
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "offline" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        PostgreSQL driver implementation for SQLx - feature "rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1/maths) >= 1.36.0
Requires:       crate(rust-decimal-1/std) >= 1.36.0
Requires:       crate(sqlx-core-0.9/rust-decimal) >= 0.9.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "rust_decimal" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        PostgreSQL driver implementation for SQLx - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/time) >= 0.9.0
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/macros) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "time" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        PostgreSQL driver implementation for SQLx - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/uuid) >= 0.9.0
Requires:       crate(uuid-1/default) >= 1.12.1
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "uuid" for the Rust sqlx-postgres crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
