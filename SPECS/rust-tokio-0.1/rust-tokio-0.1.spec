# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio
%global full_version 0.1.22
%global pkgname tokio-0.1

Name:           rust-tokio-0.1
Version:        0.1.22
Release:        %autorelease
Summary:        Rust crate "tokio"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:5a09c0b5bb588872ab2f09afa13ee6e9dac11e10a0ec9e8e3ba39a5a5d530af6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-0.1/default) >= 0.1.20

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tokio"

%package     -n %{name}+bytes
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+codec
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "codec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/io) = %{version}
Requires:       crate(%{pkgname}/tokio-codec) = %{version}
Provides:       crate(%{pkgname}/codec) = %{version}

%description -n %{name}+codec
This metapackage enables feature "codec" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/codec) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/io) = %{version}
Requires:       crate(%{pkgname}/reactor) = %{version}
Requires:       crate(%{pkgname}/rt-full) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Requires:       crate(%{pkgname}/tcp) = %{version}
Requires:       crate(%{pkgname}/timer) = %{version}
Requires:       crate(%{pkgname}/udp) = %{version}
Requires:       crate(%{pkgname}/uds) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytes) = %{version}
Requires:       crate(%{pkgname}/tokio-io) = %{version}
Provides:       crate(%{pkgname}/io) = %{version}

%description -n %{name}+io
This metapackage enables feature "io" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "mio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-0.6/default) >= 0.6.14
Provides:       crate(%{pkgname}/mio) = %{version}

%description -n %{name}+mio
This metapackage enables feature "mio" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-cpus
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "num_cpus"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-cpus-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/num-cpus) = %{version}

%description -n %{name}+num-cpus
This metapackage enables feature "num_cpus" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reactor
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "reactor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/io) = %{version}
Requires:       crate(%{pkgname}/mio) = %{version}
Requires:       crate(%{pkgname}/tokio-reactor) = %{version}
Provides:       crate(%{pkgname}/reactor) = %{version}

%description -n %{name}+reactor
This metapackage enables feature "reactor" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-full
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "rt-full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-cpus) = %{version}
Requires:       crate(%{pkgname}/reactor) = %{version}
Requires:       crate(%{pkgname}/timer) = %{version}
Requires:       crate(%{pkgname}/tokio-current-thread) = %{version}
Requires:       crate(%{pkgname}/tokio-executor) = %{version}
Requires:       crate(%{pkgname}/tokio-threadpool) = %{version}
Provides:       crate(%{pkgname}/rt-full) = %{version}

%description -n %{name}+rt-full
This metapackage enables feature "rt-full" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-codec
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-codec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-codec-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/tokio-codec) = %{version}

%description -n %{name}+tokio-codec
This metapackage enables feature "tokio-codec" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-current-thread
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-current-thread"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-current-thread-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/tokio-current-thread) = %{version}

%description -n %{name}+tokio-current-thread
This metapackage enables feature "tokio-current-thread" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-executor
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-executor-0.1/default) >= 0.1.7
Provides:       crate(%{pkgname}/tokio-executor) = %{version}

%description -n %{name}+tokio-executor
This metapackage enables feature "tokio-executor" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-fs
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-fs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-fs-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/fs) = %{version}
Provides:       crate(%{pkgname}/tokio-fs) = %{version}

%description -n %{name}+tokio-fs
This metapackage enables feature "tokio-fs" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "fs" feature.

%package     -n %{name}+tokio-io
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-io-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/tokio-io) = %{version}

%description -n %{name}+tokio-io
This metapackage enables feature "tokio-io" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-reactor
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-reactor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-reactor-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}/tokio-reactor) = %{version}

%description -n %{name}+tokio-reactor
This metapackage enables feature "tokio-reactor" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-sync
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-sync" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-sync-0.1/default) >= 0.1.5
Provides:       crate(%{pkgname}/sync) = %{version}
Provides:       crate(%{pkgname}/tokio-sync) = %{version}

%description -n %{name}+tokio-sync
This metapackage enables feature "tokio-sync" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "sync" feature.

%package     -n %{name}+tokio-tcp
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-tcp" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-tcp-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/tcp) = %{version}
Provides:       crate(%{pkgname}/tokio-tcp) = %{version}

%description -n %{name}+tokio-tcp
This metapackage enables feature "tokio-tcp" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tcp" feature.

%package     -n %{name}+tokio-threadpool
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-threadpool"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-threadpool-0.1/default) >= 0.1.14
Provides:       crate(%{pkgname}/tokio-threadpool) = %{version}

%description -n %{name}+tokio-threadpool
This metapackage enables feature "tokio-threadpool" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-timer
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-timer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-timer-0.2/default) >= 0.2.8
Provides:       crate(%{pkgname}/timer) = %{version}
Provides:       crate(%{pkgname}/tokio-timer) = %{version}

%description -n %{name}+tokio-timer
This metapackage enables feature "tokio-timer" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "timer" feature.

%package     -n %{name}+tokio-udp
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-udp" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-udp-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/tokio-udp) = %{version}
Provides:       crate(%{pkgname}/udp) = %{version}

%description -n %{name}+tokio-udp
This metapackage enables feature "tokio-udp" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "udp" feature.

%package     -n %{name}+tokio-uds
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-uds" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-uds-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/tokio-uds) = %{version}
Provides:       crate(%{pkgname}/uds) = %{version}

%description -n %{name}+tokio-uds
This metapackage enables feature "tokio-uds" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "uds" feature.

%package     -n %{name}+tracing-core
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tracing-core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-core-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/experimental-tracing) = %{version}
Provides:       crate(%{pkgname}/tracing-core) = %{version}

%description -n %{name}+tracing-core
This metapackage enables feature "tracing-core" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "experimental-tracing" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
