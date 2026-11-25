# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sqlx-core
%global full_version 0.9.0
%global pkgname sqlx-core-0.9

Name:           rust-sqlx-core-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "sqlx-core"
License:        MIT OR Apache-2.0
URL:            https://github.com/launchbadge/sqlx
#!RemoteAsset:  sha256:05b44e85bf579a8eeb4ceaa77a3a523baf2bf0e9bac7e40f405d537b5d2d5ccb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/alloc) >= 0.22.1
Requires:       crate(bytes-1/default) >= 1.2.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(crossbeam-queue-0.3/default) >= 0.3.2
Requires:       crate(either-1/default) >= 1.6.1
Requires:       crate(event-listener-5/default) >= 5.2.0
Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(futures-intrusive-0.5/default) >= 0.5.0
Requires:       crate(futures-io-0.3/default) >= 0.3.32
Requires:       crate(futures-util-0.3/alloc) >= 0.3.32
Requires:       crate(futures-util-0.3/io) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Requires:       crate(hashbrown-0.16/default) >= 0.16.0
Requires:       crate(hashlink-0.11/default) >= 0.11.0
Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(log-0.4) >= 0.4.18
Requires:       crate(memchr-2) >= 2.5.0
Requires:       crate(percent-encoding-2/default) >= 2.3.0
Requires:       crate(smallvec-1/default) >= 1.13.1
Requires:       crate(thiserror-2/std) >= 2.0.18
Requires:       crate(tracing-0.1/default) >= 0.1.37
Requires:       crate(tracing-0.1/log) >= 0.1.37
Requires:       crate(url-2/default) >= 2.2.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/any) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/tls-none) = %{version}

%description
Not intended to be used directly.
Source code for takopackized Rust crate "sqlx-core"

%package     -n %{name}+rt-async-global-executor
Summary:        Core of SQLx, the rust SQL toolkit - feature "_rt-async-global-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-global-executor) = %{version}
Requires:       crate(%{pkgname}/rt-async-io) = %{version}
Requires:       crate(%{pkgname}/rt-async-task) = %{version}
Provides:       crate(%{pkgname}/rt-async-global-executor) = %{version}

%description -n %{name}+rt-async-global-executor
Not intended to be used directly.
This metapackage enables feature "_rt-async-global-executor" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-async-io
Summary:        Core of SQLx, the rust SQL toolkit - feature "_rt-async-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-fs) = %{version}
Requires:       crate(%{pkgname}/async-io) = %{version}
Provides:       crate(%{pkgname}/rt-async-io) = %{version}

%description -n %{name}+rt-async-io
Not intended to be used directly.
This metapackage enables feature "_rt-async-io" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-async-std
Summary:        Core of SQLx, the rust SQL toolkit - feature "_rt-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-std) = %{version}
Requires:       crate(%{pkgname}/rt-async-io) = %{version}
Provides:       crate(%{pkgname}/rt-async-std) = %{version}

%description -n %{name}+rt-async-std
Not intended to be used directly.
This metapackage enables feature "_rt-async-std" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-smol
Summary:        Core of SQLx, the rust SQL toolkit - feature "_rt-smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rt-async-io) = %{version}
Requires:       crate(%{pkgname}/rt-async-task) = %{version}
Requires:       crate(%{pkgname}/smol) = %{version}
Provides:       crate(%{pkgname}/rt-smol) = %{version}

%description -n %{name}+rt-smol
Not intended to be used directly.
This metapackage enables feature "_rt-smol" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-tokio
Summary:        Core of SQLx, the rust SQL toolkit - feature "_rt-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/tokio-stream) = %{version}
Provides:       crate(%{pkgname}/rt-tokio) = %{version}

%description -n %{name}+rt-tokio
Not intended to be used directly.
This metapackage enables feature "_rt-tokio" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-aws-lc-rs
Summary:        Core of SQLx, the rust SQL toolkit - feature "_tls-rustls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls-rustls) = %{version}
Requires:       crate(%{pkgname}/webpki-roots) = %{version}
Requires:       crate(rustls-0.23/aws-lc-rs) >= 0.23.24
Requires:       crate(rustls-0.23/std) >= 0.23.24
Requires:       crate(rustls-0.23/tls12) >= 0.23.24
Provides:       crate(%{pkgname}/tls-rustls-aws-lc-rs) = %{version}

%description -n %{name}+tls-rustls-aws-lc-rs
Not intended to be used directly.
This metapackage enables feature "_tls-rustls-aws-lc-rs" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring-native-roots
Summary:        Core of SQLx, the rust SQL toolkit - feature "_tls-rustls-ring-native-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-native-certs) = %{version}
Requires:       crate(%{pkgname}/tls-rustls) = %{version}
Requires:       crate(rustls-0.23/ring) >= 0.23.24
Requires:       crate(rustls-0.23/std) >= 0.23.24
Requires:       crate(rustls-0.23/tls12) >= 0.23.24
Provides:       crate(%{pkgname}/tls-rustls-ring-native-roots) = %{version}

%description -n %{name}+tls-rustls-ring-native-roots
Not intended to be used directly.
This metapackage enables feature "_tls-rustls-ring-native-roots" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls-ring-webpki
Summary:        Core of SQLx, the rust SQL toolkit - feature "_tls-rustls-ring-webpki"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls-rustls) = %{version}
Requires:       crate(%{pkgname}/webpki-roots) = %{version}
Requires:       crate(rustls-0.23/ring) >= 0.23.24
Requires:       crate(rustls-0.23/std) >= 0.23.24
Requires:       crate(rustls-0.23/tls12) >= 0.23.24
Provides:       crate(%{pkgname}/tls-rustls-ring-webpki) = %{version}

%description -n %{name}+tls-rustls-ring-webpki
Not intended to be used directly.
This metapackage enables feature "_tls-rustls-ring-webpki" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-fs
Summary:        Core of SQLx, the rust SQL toolkit - feature "async-fs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-fs-2/default) >= 2.1.0
Provides:       crate(%{pkgname}/async-fs) = %{version}

%description -n %{name}+async-fs
Not intended to be used directly.
This metapackage enables feature "async-fs" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-global-executor
Summary:        Core of SQLx, the rust SQL toolkit - feature "async-global-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-global-executor-3/async-io) >= 3.1.0
Provides:       crate(%{pkgname}/async-global-executor) = %{version}

%description -n %{name}+async-global-executor
Not intended to be used directly.
This metapackage enables feature "async-global-executor" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-io
Summary:        Core of SQLx, the rust SQL toolkit - feature "async-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-io-2/default) >= 2.4.1
Provides:       crate(%{pkgname}/async-io) = %{version}

%description -n %{name}+async-io
Not intended to be used directly.
This metapackage enables feature "async-io" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Core of SQLx, the rust SQL toolkit - feature "async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.13.0
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
Not intended to be used directly.
This metapackage enables feature "async-std" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-task
Summary:        Core of SQLx, the rust SQL toolkit - feature "async-task" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-task-4/default) >= 4.7.1
Provides:       crate(%{pkgname}/async-task) = %{version}
Provides:       crate(%{pkgname}/rt-async-task) = %{version}

%description -n %{name}+async-task
Not intended to be used directly.
This metapackage enables feature "async-task" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "_rt-async-task" feature.

%package     -n %{name}+bigdecimal
Summary:        Core of SQLx, the rust SQL toolkit - feature "bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bigdecimal-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/bigdecimal) = %{version}

%description -n %{name}+bigdecimal
Not intended to be used directly.
This metapackage enables feature "bigdecimal" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bit-vec
Summary:        Core of SQLx, the rust SQL toolkit - feature "bit-vec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bit-vec-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/bit-vec) = %{version}

%description -n %{name}+bit-vec
Not intended to be used directly.
This metapackage enables feature "bit-vec" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bstr
Summary:        Core of SQLx, the rust SQL toolkit - feature "bstr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/std) >= 1.0.1
Provides:       crate(%{pkgname}/bstr) = %{version}

%description -n %{name}+bstr
Not intended to be used directly.
This metapackage enables feature "bstr" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Core of SQLx, the rust SQL toolkit - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.34
Requires:       crate(chrono-0.4/std) >= 0.4.34
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
Not intended to be used directly.
This metapackage enables feature "chrono" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crc
Summary:        Core of SQLx, the rust SQL toolkit - feature "crc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crc-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/crc) = %{version}

%description -n %{name}+crc
Not intended to be used directly.
This metapackage enables feature "crc" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnet
Summary:        Core of SQLx, the rust SQL toolkit - feature "ipnet"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnet-2/default) >= 2.3.0
Provides:       crate(%{pkgname}/ipnet) = %{version}

%description -n %{name}+ipnet
Not intended to be used directly.
This metapackage enables feature "ipnet" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipnetwork
Summary:        Core of SQLx, the rust SQL toolkit - feature "ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnetwork-0.21/default) >= 0.21.1
Provides:       crate(%{pkgname}/ipnetwork) = %{version}

%description -n %{name}+ipnetwork
Not intended to be used directly.
This metapackage enables feature "ipnetwork" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Core of SQLx, the rust SQL toolkit - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
Not intended to be used directly.
This metapackage enables feature "json" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mac-address
Summary:        Core of SQLx, the rust SQL toolkit - feature "mac_address"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mac-address-1/default) >= 1.1.5
Provides:       crate(%{pkgname}/mac-address) = %{version}

%description -n %{name}+mac-address
Not intended to be used directly.
This metapackage enables feature "mac_address" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+migrate
Summary:        Core of SQLx, the rust SQL toolkit - feature "migrate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/crc) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/migrate) = %{version}

%description -n %{name}+migrate
Not intended to be used directly.
This metapackage enables feature "migrate" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        Core of SQLx, the rust SQL toolkit - feature "native-tls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(native-tls-0.2/default) >= 0.2.10
Provides:       crate(%{pkgname}/native-tls) = %{version}
Provides:       crate(%{pkgname}/tls-native-tls) = %{version}

%description -n %{name}+native-tls
Not intended to be used directly.
This metapackage enables feature "native-tls" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "_tls-native-tls" feature.

%package     -n %{name}+offline
Summary:        Core of SQLx, the rust SQL toolkit - feature "offline"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(either-1/serde) >= 1.6.1
Provides:       crate(%{pkgname}/offline) = %{version}

%description -n %{name}+offline
Not intended to be used directly.
This metapackage enables feature "offline" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        Core of SQLx, the rust SQL toolkit - feature "rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1/std) >= 1.36.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
Not intended to be used directly.
This metapackage enables feature "rust_decimal" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Core of SQLx, the rust SQL toolkit - feature "rustls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/std) >= 0.23.24
Requires:       crate(rustls-0.23/tls12) >= 0.23.24
Provides:       crate(%{pkgname}/rustls) = %{version}
Provides:       crate(%{pkgname}/tls-rustls) = %{version}

%description -n %{name}+rustls
Not intended to be used directly.
This metapackage enables feature "rustls" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "_tls-rustls" feature.

%package     -n %{name}+rustls-native-certs
Summary:        Core of SQLx, the rust SQL toolkit - feature "rustls-native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-native-certs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rustls-native-certs) = %{version}

%description -n %{name}+rustls-native-certs
Not intended to be used directly.
This metapackage enables feature "rustls-native-certs" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Core of SQLx, the rust SQL toolkit - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(serde-1/rc) >= 1.0.219
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Not intended to be used directly.
This metapackage enables feature "serde" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Core of SQLx, the rust SQL toolkit - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.142
Requires:       crate(serde-json-1/raw-value) >= 1.0.142
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
Not intended to be used directly.
This metapackage enables feature "serde_json" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Core of SQLx, the rust SQL toolkit - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
Not intended to be used directly.
This metapackage enables feature "sha2" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol
Summary:        Core of SQLx, the rust SQL toolkit - feature "smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smol-2) >= 2.0.0
Provides:       crate(%{pkgname}/smol) = %{version}

%description -n %{name}+smol
Not intended to be used directly.
This metapackage enables feature "smol" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sqlx-toml
Summary:        Core of SQLx, the rust SQL toolkit - feature "sqlx-toml" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(toml-0.8/parse) >= 0.8.16
Provides:       crate(%{pkgname}/sqlx-toml) = %{version}
Provides:       crate(%{pkgname}/unstable-doc) = %{version}

%description -n %{name}+sqlx-toml
Not intended to be used directly.
This metapackage enables feature "sqlx-toml" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "_unstable-doc" feature.

%package     -n %{name}+time
Summary:        Core of SQLx, the rust SQL toolkit - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/macros) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
Not intended to be used directly.
This metapackage enables feature "time" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Core of SQLx, the rust SQL toolkit - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/fs) >= 1.25.0
Requires:       crate(tokio-1/io-util) >= 1.25.0
Requires:       crate(tokio-1/net) >= 1.25.0
Requires:       crate(tokio-1/rt) >= 1.25.0
Requires:       crate(tokio-1/sync) >= 1.25.0
Requires:       crate(tokio-1/time) >= 1.25.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
Not intended to be used directly.
This metapackage enables feature "tokio" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-stream
Summary:        Core of SQLx, the rust SQL toolkit - feature "tokio-stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-stream-0.1/default) >= 0.1.8
Requires:       crate(tokio-stream-0.1/fs) >= 0.1.8
Provides:       crate(%{pkgname}/tokio-stream) = %{version}

%description -n %{name}+tokio-stream
Not intended to be used directly.
This metapackage enables feature "tokio-stream" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+toml
Summary:        Core of SQLx, the rust SQL toolkit - feature "toml"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-0.8/default) >= 0.8.16
Provides:       crate(%{pkgname}/toml) = %{version}

%description -n %{name}+toml
Not intended to be used directly.
This metapackage enables feature "toml" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Core of SQLx, the rust SQL toolkit - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1/default) >= 1.12.1
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
Not intended to be used directly.
This metapackage enables feature "uuid" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Core of SQLx, the rust SQL toolkit - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-roots-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
Not intended to be used directly.
This metapackage enables feature "webpki-roots" for the Rust sqlx-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
