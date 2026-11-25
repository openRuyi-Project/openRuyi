# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sqlx-sqlite
%global full_version 0.9.0
%global pkgname sqlx-sqlite-0.9

Name:           rust-sqlx-sqlite-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "sqlx-sqlite"
License:        MIT OR Apache-2.0
URL:            https://github.com/launchbadge/sqlx
#!RemoteAsset:  sha256:488e99c397a62007e4229aec669a179816339afc6d2620ca6fa420dbee2e982c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atoi-2/default) >= 2.0.0
Requires:       crate(flume-0.12/async) >= 0.12.0
Requires:       crate(form-urlencoded-1/default) >= 1.2.2
Requires:       crate(futures-channel-0.3/alloc) >= 0.3.32
Requires:       crate(futures-channel-0.3/sink) >= 0.3.32
Requires:       crate(futures-channel-0.3/std) >= 0.3.32
Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(futures-executor-0.3/default) >= 0.3.32
Requires:       crate(futures-intrusive-0.5/default) >= 0.5.0
Requires:       crate(futures-util-0.3/alloc) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Requires:       crate(libsqlite3-sys-0.30/pkg-config) >= 0.30.1
Requires:       crate(libsqlite3-sys-0.30/vcpkg) >= 0.30.1
Requires:       crate(log-0.4/default) >= 0.4.18
Requires:       crate(percent-encoding-2/default) >= 2.3.0
Requires:       crate(sqlx-core-0.9/default) >= 0.9.0
Requires:       crate(thiserror-2/std) >= 2.0.18
Requires:       crate(tracing-0.1/default) >= 0.1.37
Requires:       crate(tracing-0.1/log) >= 0.1.37
Requires:       crate(url-2/default) >= 2.2.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bigdecimal) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/deserialize) = %{version}
Provides:       crate(%{pkgname}/load-extension) = %{version}
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description
Not for direct use; see the `sqlx` crate for details.
Source code for takopackized Rust crate "sqlx-sqlite"

%package     -n %{name}+unstable-all-sqlite-features
Summary:        SQLite driver implementation for SQLx - feature "_unstable-all-sqlite-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deserialize) = %{version}
Requires:       crate(%{pkgname}/load-extension) = %{version}
Requires:       crate(%{pkgname}/preupdate-hook) = %{version}
Requires:       crate(%{pkgname}/unlock-notify) = %{version}
Provides:       crate(%{pkgname}/unstable-all-sqlite-features) = %{version}

%description -n %{name}+unstable-all-sqlite-features
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "_unstable-all-sqlite-features" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-all-types
Summary:        SQLite driver implementation for SQLx - feature "_unstable-all-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/json) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Requires:       crate(%{pkgname}/uuid) = %{version}
Provides:       crate(%{pkgname}/unstable-all-types) = %{version}

%description -n %{name}+unstable-all-types
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "_unstable-all-types" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-docs
Summary:        SQLite driver implementation for SQLx - feature "_unstable-docs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any) = %{version}
Requires:       crate(%{pkgname}/bundled) = %{version}
Requires:       crate(%{pkgname}/unstable-all-sqlite-features) = %{version}
Requires:       crate(%{pkgname}/unstable-all-types) = %{version}
Provides:       crate(%{pkgname}/unstable-docs) = %{version}

%description -n %{name}+unstable-docs
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "_unstable-docs" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+any
Summary:        SQLite driver implementation for SQLx - feature "any"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/any) >= 0.9.0
Provides:       crate(%{pkgname}/any) = %{version}

%description -n %{name}+any
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "any" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bundled
Summary:        SQLite driver implementation for SQLx - feature "bundled"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.30/bundled) >= 0.30.1
Requires:       crate(libsqlite3-sys-0.30/pkg-config) >= 0.30.1
Requires:       crate(libsqlite3-sys-0.30/vcpkg) >= 0.30.1
Provides:       crate(%{pkgname}/bundled) = %{version}

%description -n %{name}+bundled
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "bundled" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        SQLite driver implementation for SQLx - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.34
Requires:       crate(chrono-0.4/std) >= 0.4.34
Requires:       crate(sqlx-core-0.9/chrono) >= 0.9.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "chrono" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        SQLite driver implementation for SQLx - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(sqlx-core-0.9/json) >= 0.9.0
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "json" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+migrate
Summary:        SQLite driver implementation for SQLx - feature "migrate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/migrate) >= 0.9.0
Provides:       crate(%{pkgname}/migrate) = %{version}

%description -n %{name}+migrate
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "migrate" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+offline
Summary:        SQLite driver implementation for SQLx - feature "offline"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(sqlx-core-0.9/offline) >= 0.9.0
Provides:       crate(%{pkgname}/offline) = %{version}

%description -n %{name}+offline
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "offline" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preupdate-hook
Summary:        SQLite driver implementation for SQLx - feature "preupdate-hook"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.30/pkg-config) >= 0.30.1
Requires:       crate(libsqlite3-sys-0.30/preupdate-hook) >= 0.30.1
Requires:       crate(libsqlite3-sys-0.30/vcpkg) >= 0.30.1
Provides:       crate(%{pkgname}/preupdate-hook) = %{version}

%description -n %{name}+preupdate-hook
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "preupdate-hook" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regexp
Summary:        SQLite driver implementation for SQLx - feature "regexp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.6.0
Provides:       crate(%{pkgname}/regexp) = %{version}

%description -n %{name}+regexp
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "regexp" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        SQLite driver implementation for SQLx - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "serde" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-toml
Summary:        SQLite driver implementation for SQLx - feature "sqlx-toml"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/sqlx-toml) >= 0.9.0
Provides:       crate(%{pkgname}/sqlx-toml) = %{version}

%description -n %{name}+sqlx-toml
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "sqlx-toml" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        SQLite driver implementation for SQLx - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/time) >= 0.9.0
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/macros) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "time" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unbundled
Summary:        SQLite driver implementation for SQLx - feature "unbundled"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.30/buildtime-bindgen) >= 0.30.1
Requires:       crate(libsqlite3-sys-0.30/pkg-config) >= 0.30.1
Requires:       crate(libsqlite3-sys-0.30/vcpkg) >= 0.30.1
Provides:       crate(%{pkgname}/unbundled) = %{version}

%description -n %{name}+unbundled
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "unbundled" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unlock-notify
Summary:        SQLite driver implementation for SQLx - feature "unlock-notify"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.30/pkg-config) >= 0.30.1
Requires:       crate(libsqlite3-sys-0.30/unlock-notify) >= 0.30.1
Requires:       crate(libsqlite3-sys-0.30/vcpkg) >= 0.30.1
Provides:       crate(%{pkgname}/unlock-notify) = %{version}

%description -n %{name}+unlock-notify
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "unlock-notify" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        SQLite driver implementation for SQLx - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sqlx-core-0.9/uuid) >= 0.9.0
Requires:       crate(uuid-1/default) >= 1.12.1
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
Not for direct use; see the `sqlx` crate for details.
This metapackage enables feature "uuid" for the Rust sqlx-sqlite crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
