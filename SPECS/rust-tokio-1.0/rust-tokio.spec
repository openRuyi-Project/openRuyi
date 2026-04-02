# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio
%global full_version 1.50.0
%global pkgname tokio-1.0

Name:           rust-tokio-1.0
Version:        1.50.0
Release:        %autorelease
Summary:        Rust crate "tokio"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:27ad5e34374e03cfffefc301becb44e9dc3c17584f414349ebe29ed26661822d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/fs)
Provides:       crate(%{pkgname}/io-std)
Provides:       crate(%{pkgname}/rt)
Provides:       crate(%{pkgname}/rt-multi-thread)
Provides:       crate(%{pkgname}/sync)
Provides:       crate(%{pkgname}/time)

%description
Source code for takopackized Rust crate "tokio"

%package     -n %{name}+bytes
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "bytes" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(bytes-1.0/default) >= 1.11.1
Provides:       crate(%{pkgname}/bytes)
Provides:       crate(%{pkgname}/io-util)

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "io-util" feature.

%package     -n %{name}+full
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "full"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/fs)
Requires:       crate(%{pkgname}/io-std)
Requires:       crate(%{pkgname}/io-util)
Requires:       crate(%{pkgname}/macros)
Requires:       crate(%{pkgname}/net)
Requires:       crate(%{pkgname}/parking-lot)
Requires:       crate(%{pkgname}/process)
Requires:       crate(%{pkgname}/rt)
Requires:       crate(%{pkgname}/rt-multi-thread)
Requires:       crate(%{pkgname}/signal)
Requires:       crate(%{pkgname}/sync)
Requires:       crate(%{pkgname}/time)
Provides:       crate(%{pkgname}/full)

%description -n %{name}+full
This metapackage enables feature "full" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-uring
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "io-uring"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/libc)
Requires:       crate(io-uring-0.7) >= 0.7.11
Requires:       crate(mio-1.0/os-ext) >= 1.2.0
Requires:       crate(mio-1.0/os-poll) >= 1.2.0
Requires:       crate(slab-0.4/default) >= 0.4.9
Provides:       crate(%{pkgname}/io-uring)

%description -n %{name}+io-uring
This metapackage enables feature "io-uring" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2/default) >= 0.2.184
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "mio"
Requires:       crate(%{pkgname})
Requires:       crate(mio-1.0) >= 1.2.0
Requires:       crate(mio-1.0/os-ext) >= 1.2.0
Requires:       crate(mio-1.0/os-poll) >= 1.2.0
Provides:       crate(%{pkgname}/mio)

%description -n %{name}+mio
This metapackage enables feature "mio" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+net
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "net"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/socket2)
Requires:       crate(mio-1.0/net) >= 1.2.0
Requires:       crate(mio-1.0/os-ext) >= 1.2.0
Requires:       crate(mio-1.0/os-poll) >= 1.2.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-security) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-pipes) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-systemservices) >= 0.61.2
Provides:       crate(%{pkgname}/net)

%description -n %{name}+net
This metapackage enables feature "net" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking-lot
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "parking_lot"
Requires:       crate(%{pkgname})
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/parking-lot)

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+process
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "process"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bytes)
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/signal-hook-registry)
Requires:       crate(mio-1.0/net) >= 1.2.0
Requires:       crate(mio-1.0/os-ext) >= 1.2.0
Requires:       crate(mio-1.0/os-poll) >= 1.2.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-windowsprogramming) >= 0.61.2
Provides:       crate(%{pkgname}/process)

%description -n %{name}+process
This metapackage enables feature "process" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signal
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "signal"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/signal-hook-registry)
Requires:       crate(mio-1.0/net) >= 1.2.0
Requires:       crate(mio-1.0/os-ext) >= 1.2.0
Requires:       crate(mio-1.0/os-poll) >= 1.2.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-console) >= 0.61.2
Provides:       crate(%{pkgname}/signal)

%description -n %{name}+signal
This metapackage enables feature "signal" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signal-hook-registry
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "signal-hook-registry"
Requires:       crate(%{pkgname})
Requires:       crate(signal-hook-registry-1.0/default) >= 1.1.1
Provides:       crate(%{pkgname}/signal-hook-registry)

%description -n %{name}+signal-hook-registry
This metapackage enables feature "signal-hook-registry" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socket2
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "socket2"
Requires:       crate(%{pkgname})
Requires:       crate(socket2-0.6/all) >= 0.6.3
Requires:       crate(socket2-0.6/default) >= 0.6.3
Provides:       crate(%{pkgname}/socket2)

%description -n %{name}+socket2
This metapackage enables feature "socket2" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+taskdump
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "taskdump"
Requires:       crate(%{pkgname})
Requires:       crate(backtrace-0.3/default) >= 0.3.58
Provides:       crate(%{pkgname}/taskdump)

%description -n %{name}+taskdump
This metapackage enables feature "taskdump" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-util
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "test-util"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rt)
Requires:       crate(%{pkgname}/sync)
Requires:       crate(%{pkgname}/time)
Provides:       crate(%{pkgname}/test-util)

%description -n %{name}+test-util
This metapackage enables feature "test-util" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-macros
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tokio-macros" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(tokio-macros-2.0/default) >= 2.6.0
Provides:       crate(%{pkgname}/macros)
Provides:       crate(%{pkgname}/tokio-macros)

%description -n %{name}+tokio-macros
This metapackage enables feature "tokio-macros" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "macros" feature.

%package     -n %{name}+tracing
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1/std) >= 0.1.29
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-sys
Summary:        Event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications - feature "windows-sys"
Requires:       crate(%{pkgname})
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Provides:       crate(%{pkgname}/windows-sys)

%description -n %{name}+windows-sys
This metapackage enables feature "windows-sys" for the Rust tokio crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
