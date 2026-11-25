# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sqlx-mysql
%global full_version 0.9.0
%global pkgname sqlx-mysql-0.9

Name:           rust-sqlx-mysql-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "sqlx-mysql"
License:        MIT OR Apache-2.0
URL:            https://github.com/launchbadge/sqlx
#!RemoteAsset:  sha256:90b8020fe17c5f2c245bfa2505d7ef59c5604839527c740266ad2214acebea27
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2) >= 2.4.0
Requires:       crate(byteorder-1/std) >= 1.4.3
Requires:       crate(bytes-1/default) >= 1.2.0
Requires:       crate(digest-0.11/alloc) >= 0.11.2
Requires:       crate(dotenvy-0.15) >= 0.15.7
Requires:       crate(either-1/default) >= 1.6.1
Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(futures-util-0.3/alloc) >= 0.3.32
Requires:       crate(futures-util-0.3/io) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Requires:       crate(generic-array-0.14) >= 0.14.4
Requires:       crate(log-0.4/default) >= 0.4.18
Requires:       crate(percent-encoding-2/default) >= 2.3.0
Requires:       crate(sha1-0.11) >= 0.11.0
Requires:       crate(sha2-0.11) >= 0.11.0
Requires:       crate(sqlx-core-0.9/default) >= 0.9.0
Requires:       crate(thiserror-2/std) >= 2.0.18
Requires:       crate(tracing-0.1/default) >= 0.1.37
Requires:       crate(tracing-0.1/log) >= 0.1.37

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Not for direct use; see the `sqlx` crate for details.
Source code for takopackized Rust crate "sqlx-mysql"

%package     -n %{name}+any
Summary:        MySQL driver implementation for SQLx - feature "any"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/any) >= 0.9.0
Provides:       crate(%{pkgname}/any) = %{version}

%description -n %{name}+any
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "any" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigdecimal
Summary:        MySQL driver implementation for SQLx - feature "bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bigdecimal-0.4/default) >= 0.4.0
Requires:       crate(sqlx-core-0.9/bigdecimal) >= 0.9.0
Provides:       crate(%{pkgname}/bigdecimal) = %{version}

%description -n %{name}+bigdecimal
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "bigdecimal" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        MySQL driver implementation for SQLx - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.34
Requires:       crate(chrono-0.4/std) >= 0.4.34
Requires:       crate(sqlx-core-0.9/chrono) >= 0.9.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "chrono" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        MySQL driver implementation for SQLx - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(sqlx-core-0.9/json) >= 0.9.0
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "json" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+migrate
Summary:        MySQL driver implementation for SQLx - feature "migrate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crc-3/default) >= 3.0.0
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Provides:       crate(%{pkgname}/migrate) = %{version}

%description -n %{name}+migrate
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "migrate" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+offline
Summary:        MySQL driver implementation for SQLx - feature "offline"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/serde) >= 2.4.0
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/offline) = %{version}

%description -n %{name}+offline
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "offline" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rsa
Summary:        MySQL driver implementation for SQLx - feature "rsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.10/thread-rng) >= 0.10.1
Requires:       crate(rsa-0.10.0-rc.18/default) >= 0.10.0-rc.18
Provides:       crate(%{pkgname}/rsa) = %{version}

%description -n %{name}+rsa
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "rsa" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        MySQL driver implementation for SQLx - feature "rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1/maths) >= 1.36.0
Requires:       crate(rust-decimal-1/std) >= 1.36.0
Requires:       crate(sqlx-core-0.9/rust-decimal) >= 0.9.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "rust_decimal" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        MySQL driver implementation for SQLx - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.219
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "serde" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        MySQL driver implementation for SQLx - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/time) >= 0.9.0
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/macros) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "time" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        MySQL driver implementation for SQLx - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/uuid) >= 0.9.0
Requires:       crate(uuid-1/default) >= 1.12.1
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "uuid" for the Rust sqlx-mysql crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
