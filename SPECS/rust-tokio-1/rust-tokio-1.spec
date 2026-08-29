# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio
%global full_version 1.52.3
%global pkgname tokio-1

Name:           rust-tokio-1
Version:        1.52.3
Release:        %autorelease
Summary:        Rust crate "tokio"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:8fc7f01b389ac15039e4dc9531aa973a135d7a4135281b12d7c1bc79fd57fffe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pin-project-lite-0.2/default) >= 0.2.11
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fs) = %{version}
Provides:       crate(%{pkgname}/io-std) = %{version}
Provides:       crate(%{pkgname}/rt) = %{version}
Provides:       crate(%{pkgname}/rt-multi-thread) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}
Provides:       crate(%{pkgname}/time) = %{version}

%description
Source code for takopackized Rust crate "tokio"

%package     -n %{name}+bytes
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "bytes" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.2.1
Provides:       crate(%{pkgname}/bytes) = %{version}
Provides:       crate(%{pkgname}/io-util) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "io-util" feature.

%package     -n %{name}+full
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/io-std) = %{version}
Requires:       crate(%{pkgname}/io-util) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/net) = %{version}
Requires:       crate(%{pkgname}/parking-lot) = %{version}
Requires:       crate(%{pkgname}/process) = %{version}
Requires:       crate(%{pkgname}/rt) = %{version}
Requires:       crate(%{pkgname}/rt-multi-thread) = %{version}
Requires:       crate(%{pkgname}/signal) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-uring
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "io-uring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(io-uring-0.7) >= 0.7.11
Requires:       crate(mio-1/os-ext) >= 1.2.0
Requires:       crate(mio-1/os-poll) >= 1.2.0
Requires:       crate(slab-0.4/default) >= 0.4.9
Provides:       crate(%{pkgname}/io-uring) = %{version}

%description -n %{name}+io-uring
This metapackage enables feature "io-uring" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.168
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "mio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-1) >= 1.2.0
Requires:       crate(mio-1/os-ext) >= 1.2.0
Requires:       crate(mio-1/os-poll) >= 1.2.0
Provides:       crate(%{pkgname}/mio) = %{version}

%description -n %{name}+mio
This metapackage enables feature "mio" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+net
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "net"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/socket2) = %{version}
Requires:       crate(mio-1/net) >= 1.2.0
Requires:       crate(mio-1/os-ext) >= 1.2.0
Requires:       crate(mio-1/os-poll) >= 1.2.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-security) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-pipes) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-systemservices) >= 0.61.0
Provides:       crate(%{pkgname}/net) = %{version}

%description -n %{name}+net
This metapackage enables feature "net" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking-lot
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "parking_lot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/parking-lot) = %{version}

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+process
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "process"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytes) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/signal-hook-registry) = %{version}
Requires:       crate(mio-1/net) >= 1.2.0
Requires:       crate(mio-1/os-ext) >= 1.2.0
Requires:       crate(mio-1/os-poll) >= 1.2.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-windowsprogramming) >= 0.61.0
Provides:       crate(%{pkgname}/process) = %{version}

%description -n %{name}+process
This metapackage enables feature "process" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signal
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "signal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/signal-hook-registry) = %{version}
Requires:       crate(mio-1/net) >= 1.2.0
Requires:       crate(mio-1/os-ext) >= 1.2.0
Requires:       crate(mio-1/os-poll) >= 1.2.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-console) >= 0.61.0
Provides:       crate(%{pkgname}/signal) = %{version}

%description -n %{name}+signal
This metapackage enables feature "signal" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signal-hook-registry
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "signal-hook-registry"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signal-hook-registry-1/default) >= 1.1.1
Provides:       crate(%{pkgname}/signal-hook-registry) = %{version}

%description -n %{name}+signal-hook-registry
This metapackage enables feature "signal-hook-registry" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socket2
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "socket2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(socket2-0.6/all) >= 0.6.3
Requires:       crate(socket2-0.6/default) >= 0.6.3
Provides:       crate(%{pkgname}/socket2) = %{version}

%description -n %{name}+socket2
This metapackage enables feature "socket2" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+taskdump
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "taskdump"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.58
Provides:       crate(%{pkgname}/taskdump) = %{version}

%description -n %{name}+taskdump
This metapackage enables feature "taskdump" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-util
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "test-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rt) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/test-util) = %{version}

%description -n %{name}+test-util
This metapackage enables feature "test-util" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-macros
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-macros" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-macros-2/default) >= 2.7.0
Provides:       crate(%{pkgname}/macros) = %{version}
Provides:       crate(%{pkgname}/tokio-macros) = %{version}

%description -n %{name}+tokio-macros
This metapackage enables feature "tokio-macros" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "macros" feature.

%package     -n %{name}+tracing
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/std) >= 0.1.29
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-sys
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "windows-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Provides:       crate(%{pkgname}/windows-sys) = %{version}

%description -n %{name}+windows-sys
This metapackage enables feature "windows-sys" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
