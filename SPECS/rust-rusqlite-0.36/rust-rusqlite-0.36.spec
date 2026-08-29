# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rusqlite
%global full_version 0.36.0
%global pkgname rusqlite-0.36

Name:           rust-rusqlite-0.36
Version:        0.36.0
Release:        %autorelease
Summary:        Rust crate "rusqlite"
License:        MIT
URL:            https://github.com/rusqlite/rusqlite
#!RemoteAsset:  sha256:3de23c3319433716cf134eed225fe9986bc24f63bed9be9f20c329029e672dc7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.6.0
Requires:       crate(fallible-iterator-0.3/default) >= 0.3.0
Requires:       crate(fallible-streaming-iterator-0.1/default) >= 0.1.0
Requires:       crate(hashlink-0.10/default) >= 0.10.0
Requires:       crate(libsqlite3-sys-0.34/default) >= 0.34.0
Requires:       crate(smallvec-1/default) >= 1.6.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/backup) = %{version}
Provides:       crate(%{pkgname}/blob) = %{version}
Provides:       crate(%{pkgname}/collation) = %{version}
Provides:       crate(%{pkgname}/column-decltype) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/extra-check) = %{version}
Provides:       crate(%{pkgname}/functions) = %{version}
Provides:       crate(%{pkgname}/hooks) = %{version}
Provides:       crate(%{pkgname}/i128-blob) = %{version}
Provides:       crate(%{pkgname}/limits) = %{version}
Provides:       crate(%{pkgname}/load-extension) = %{version}
Provides:       crate(%{pkgname}/series) = %{version}
Provides:       crate(%{pkgname}/trace) = %{version}
Provides:       crate(%{pkgname}/vtab) = %{version}

%description
Source code for takopackized Rust crate "rusqlite"

%package     -n %{name}+array
Summary:        Ergonomic wrapper for SQLite - feature "array"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/modern-sqlite) = %{version}
Requires:       crate(%{pkgname}/vtab) = %{version}
Provides:       crate(%{pkgname}/array) = %{version}

%description -n %{name}+array
This metapackage enables feature "array" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+buildtime-bindgen
Summary:        Ergonomic wrapper for SQLite - feature "buildtime_bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.34/buildtime-bindgen) >= 0.34.0
Provides:       crate(%{pkgname}/buildtime-bindgen) = %{version}

%description -n %{name}+buildtime-bindgen
This metapackage enables feature "buildtime_bindgen" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bundled
Summary:        Ergonomic wrapper for SQLite - feature "bundled"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/modern-sqlite) = %{version}
Requires:       crate(libsqlite3-sys-0.34/bundled) >= 0.34.0
Provides:       crate(%{pkgname}/bundled) = %{version}

%description -n %{name}+bundled
This metapackage enables feature "bundled" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bundled-full
Summary:        Ergonomic wrapper for SQLite - feature "bundled-full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bundled) = %{version}
Requires:       crate(%{pkgname}/modern-full) = %{version}
Provides:       crate(%{pkgname}/bundled-full) = %{version}

%description -n %{name}+bundled-full
This metapackage enables feature "bundled-full" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bundled-sqlcipher
Summary:        Ergonomic wrapper for SQLite - feature "bundled-sqlcipher"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bundled) = %{version}
Requires:       crate(libsqlite3-sys-0.34/bundled-sqlcipher) >= 0.34.0
Provides:       crate(%{pkgname}/bundled-sqlcipher) = %{version}

%description -n %{name}+bundled-sqlcipher
This metapackage enables feature "bundled-sqlcipher" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bundled-sqlcipher-vendored-openssl
Summary:        Ergonomic wrapper for SQLite - feature "bundled-sqlcipher-vendored-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bundled-sqlcipher) = %{version}
Requires:       crate(libsqlite3-sys-0.34/bundled-sqlcipher-vendored-openssl) >= 0.34.0
Provides:       crate(%{pkgname}/bundled-sqlcipher-vendored-openssl) = %{version}

%description -n %{name}+bundled-sqlcipher-vendored-openssl
This metapackage enables feature "bundled-sqlcipher-vendored-openssl" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bundled-windows
Summary:        Ergonomic wrapper for SQLite - feature "bundled-windows"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.34/bundled-windows) >= 0.34.0
Provides:       crate(%{pkgname}/bundled-windows) = %{version}

%description -n %{name}+bundled-windows
This metapackage enables feature "bundled-windows" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Ergonomic wrapper for SQLite - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.38
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+column-metadata
Summary:        Ergonomic wrapper for SQLite - feature "column_metadata"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.34/column-metadata) >= 0.34.0
Provides:       crate(%{pkgname}/column-metadata) = %{version}

%description -n %{name}+column-metadata
This metapackage enables feature "column_metadata" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+csv
Summary:        Ergonomic wrapper for SQLite - feature "csv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(csv-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/csv) = %{version}

%description -n %{name}+csv
This metapackage enables feature "csv" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+csvtab
Summary:        Ergonomic wrapper for SQLite - feature "csvtab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/csv) = %{version}
Requires:       crate(%{pkgname}/vtab) = %{version}
Provides:       crate(%{pkgname}/csvtab) = %{version}

%description -n %{name}+csvtab
This metapackage enables feature "csvtab" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+in-gecko
Summary:        Ergonomic wrapper for SQLite - feature "in_gecko"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/modern-sqlite) = %{version}
Requires:       crate(libsqlite3-sys-0.34/in-gecko) >= 0.34.0
Provides:       crate(%{pkgname}/in-gecko) = %{version}

%description -n %{name}+in-gecko
This metapackage enables feature "in_gecko" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jiff
Summary:        Ergonomic wrapper for SQLite - feature "jiff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/jiff) = %{version}

%description -n %{name}+jiff
This metapackage enables feature "jiff" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loadable-extension
Summary:        Ergonomic wrapper for SQLite - feature "loadable_extension"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.34/loadable-extension) >= 0.34.0
Provides:       crate(%{pkgname}/loadable-extension) = %{version}

%description -n %{name}+loadable-extension
This metapackage enables feature "loadable_extension" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+modern-full
Summary:        Ergonomic wrapper for SQLite - feature "modern-full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/array) = %{version}
Requires:       crate(%{pkgname}/backup) = %{version}
Requires:       crate(%{pkgname}/blob) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/collation) = %{version}
Requires:       crate(%{pkgname}/column-decltype) = %{version}
Requires:       crate(%{pkgname}/column-metadata) = %{version}
Requires:       crate(%{pkgname}/csvtab) = %{version}
Requires:       crate(%{pkgname}/extra-check) = %{version}
Requires:       crate(%{pkgname}/functions) = %{version}
Requires:       crate(%{pkgname}/hooks) = %{version}
Requires:       crate(%{pkgname}/i128-blob) = %{version}
Requires:       crate(%{pkgname}/jiff) = %{version}
Requires:       crate(%{pkgname}/limits) = %{version}
Requires:       crate(%{pkgname}/load-extension) = %{version}
Requires:       crate(%{pkgname}/modern-sqlite) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(%{pkgname}/serialize) = %{version}
Requires:       crate(%{pkgname}/series) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Requires:       crate(%{pkgname}/trace) = %{version}
Requires:       crate(%{pkgname}/unlock-notify) = %{version}
Requires:       crate(%{pkgname}/url) = %{version}
Requires:       crate(%{pkgname}/uuid) = %{version}
Requires:       crate(%{pkgname}/vtab) = %{version}
Requires:       crate(%{pkgname}/window) = %{version}
Provides:       crate(%{pkgname}/modern-full) = %{version}

%description -n %{name}+modern-full
This metapackage enables feature "modern-full" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+modern-sqlite
Summary:        Ergonomic wrapper for SQLite - feature "modern_sqlite" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.34/bundled-bindings) >= 0.34.0
Provides:       crate(%{pkgname}/modern-sqlite) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+modern-sqlite
This metapackage enables feature "modern_sqlite" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serialize" feature.

%package     -n %{name}+preupdate-hook
Summary:        Ergonomic wrapper for SQLite - feature "preupdate_hook"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hooks) = %{version}
Requires:       crate(libsqlite3-sys-0.34/preupdate-hook) >= 0.34.0
Provides:       crate(%{pkgname}/preupdate-hook) = %{version}

%description -n %{name}+preupdate-hook
This metapackage enables feature "preupdate_hook" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rusqlite-macros
Summary:        Ergonomic wrapper for SQLite - feature "rusqlite-macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rusqlite-macros-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/rusqlite-macros) = %{version}

%description -n %{name}+rusqlite-macros
This metapackage enables feature "rusqlite-macros" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Ergonomic wrapper for SQLite - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+session
Summary:        Ergonomic wrapper for SQLite - feature "session"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hooks) = %{version}
Requires:       crate(libsqlite3-sys-0.34/session) >= 0.34.0
Provides:       crate(%{pkgname}/session) = %{version}

%description -n %{name}+session
This metapackage enables feature "session" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlcipher
Summary:        Ergonomic wrapper for SQLite - feature "sqlcipher"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.34/sqlcipher) >= 0.34.0
Provides:       crate(%{pkgname}/sqlcipher) = %{version}

%description -n %{name}+sqlcipher
This metapackage enables feature "sqlcipher" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Ergonomic wrapper for SQLite - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/default) >= 0.3.36
Requires:       crate(time-0.3/formatting) >= 0.3.36
Requires:       crate(time-0.3/macros) >= 0.3.36
Requires:       crate(time-0.3/parsing) >= 0.3.36
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unlock-notify
Summary:        Ergonomic wrapper for SQLite - feature "unlock_notify"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.34/unlock-notify) >= 0.34.0
Provides:       crate(%{pkgname}/unlock-notify) = %{version}

%description -n %{name}+unlock-notify
This metapackage enables feature "unlock_notify" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+url
Summary:        Ergonomic wrapper for SQLite - feature "url"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(url-2/default) >= 2.1.0
Provides:       crate(%{pkgname}/url) = %{version}

%description -n %{name}+url
This metapackage enables feature "url" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Ergonomic wrapper for SQLite - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm32-wasi-vfs
Summary:        Ergonomic wrapper for SQLite - feature "wasm32-wasi-vfs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.34/wasm32-wasi-vfs) >= 0.34.0
Provides:       crate(%{pkgname}/wasm32-wasi-vfs) = %{version}

%description -n %{name}+wasm32-wasi-vfs
This metapackage enables feature "wasm32-wasi-vfs" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+window
Summary:        Ergonomic wrapper for SQLite - feature "window"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/functions) = %{version}
Requires:       crate(%{pkgname}/modern-sqlite) = %{version}
Provides:       crate(%{pkgname}/window) = %{version}

%description -n %{name}+window
This metapackage enables feature "window" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-asan
Summary:        Ergonomic wrapper for SQLite - feature "with-asan"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libsqlite3-sys-0.34/with-asan) >= 0.34.0
Provides:       crate(%{pkgname}/with-asan) = %{version}

%description -n %{name}+with-asan
This metapackage enables feature "with-asan" for the Rust rusqlite crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
