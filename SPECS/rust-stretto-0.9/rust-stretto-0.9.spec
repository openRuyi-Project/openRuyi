# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stretto
%global full_version 0.9.0
%global pkgname stretto-0.9

Name:           rust-stretto-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "stretto"
License:        MIT OR Apache-2.0
URL:            https://github.com/al8n/stretto
#!RemoteAsset:  sha256:a1d042915dad0991b1dc54d0b5005029901a9705113389050d53503f2a182f28
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atomic-0.6/default) >= 0.6.0
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.0
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Requires:       crate(getrandom-0.4/wasm-js) >= 0.4.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(rand-0.10/default) >= 0.10.0
Requires:       crate(seahash-4/default) >= 4.1.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.0
Requires:       crate(wg-1/default) >= 1.0.0
Requires:       crate(xxhash-rust-0.8/default) >= 0.8.0
Requires:       crate(xxhash-rust-0.8/xxh64) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "stretto"

%package     -n %{name}+agnostic-lite
Summary:        High performance thread-safe memory-bound Rust cache - feature "agnostic-lite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(agnostic-lite-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/agnostic-lite) = %{version}

%description -n %{name}+agnostic-lite
This metapackage enables feature "agnostic-lite" for the Rust stretto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async
Summary:        High performance thread-safe memory-bound Rust cache - feature "async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-channel) = %{version}
Requires:       crate(%{pkgname}/crossbeam-channel) = %{version}
Requires:       crate(%{pkgname}/event-listener) = %{version}
Requires:       crate(agnostic-lite-0.6/time) >= 0.6.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(wg-1/future) >= 1.0.0
Provides:       crate(%{pkgname}/async) = %{version}

%description -n %{name}+async
This metapackage enables feature "async" for the Rust stretto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-channel
Summary:        High performance thread-safe memory-bound Rust cache - feature "async-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-channel-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/async-channel) = %{version}

%description -n %{name}+async-channel
This metapackage enables feature "async-channel" for the Rust stretto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossbeam-channel
Summary:        High performance thread-safe memory-bound Rust cache - feature "crossbeam-channel" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/crossbeam-channel) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}

%description -n %{name}+crossbeam-channel
This metapackage enables feature "crossbeam-channel" for the Rust stretto crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "sync" features.

%package     -n %{name}+event-listener
Summary:        High performance thread-safe memory-bound Rust cache - feature "event-listener"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(event-listener-5/default) >= 5.0.0
Provides:       crate(%{pkgname}/event-listener) = %{version}

%description -n %{name}+event-listener
This metapackage enables feature "event-listener" for the Rust stretto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        High performance thread-safe memory-bound Rust cache - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust stretto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+send-guard
Summary:        High performance thread-safe memory-bound Rust cache - feature "send_guard"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-0.12/send-guard) >= 0.12.0
Provides:       crate(%{pkgname}/send-guard) = %{version}

%description -n %{name}+send-guard
This metapackage enables feature "send_guard" for the Rust stretto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        High performance thread-safe memory-bound Rust cache - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust stretto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol
Summary:        High performance thread-safe memory-bound Rust cache - feature "smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(agnostic-lite-0.6/smol) >= 0.6.0
Provides:       crate(%{pkgname}/smol) = %{version}

%description -n %{name}+smol
This metapackage enables feature "smol" for the Rust stretto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        High performance thread-safe memory-bound Rust cache - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(agnostic-lite-0.6/tokio) >= 0.6.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust stretto crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
