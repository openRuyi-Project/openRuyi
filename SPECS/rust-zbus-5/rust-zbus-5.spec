# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zbus
%global full_version 5.15.0
%global pkgname zbus-5

Name:           rust-zbus-5
Version:        5.15.0
Release:        %autorelease
Summary:        Rust crate "zbus"
License:        MIT
URL:            https://github.com/z-galaxy/zbus/
#!RemoteAsset:  sha256:c3bcbf15c8708d7fc1be0c993622e0a5cbd5e8b52bfa40afa4c3e0cd8d724ac1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-broadcast-0.7/default) >= 0.7.0
Requires:       crate(async-recursion-1/default) >= 1.1.1
Requires:       crate(async-trait-0.1/default) >= 0.1.80
Requires:       crate(enumflags2-0.7/default) >= 0.7.9
Requires:       crate(enumflags2-0.7/serde) >= 0.7.9
Requires:       crate(event-listener-5/default) >= 5.3.0
Requires:       crate(futures-core-0.3/default) >= 0.3.30
Requires:       crate(futures-lite-2/std) >= 2.6.0
Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(libc-0.2) >= 0.2.0
Requires:       crate(ordered-stream-0.2/default) >= 0.2.0
Requires:       crate(rustix-1/net) >= 1.1.2
Requires:       crate(rustix-1/process) >= 1.1.2
Requires:       crate(rustix-1/std) >= 1.1.2
Requires:       crate(serde-1/default) >= 1.0.200
Requires:       crate(serde-1/derive) >= 1.0.200
Requires:       crate(serde-repr-0.1/default) >= 0.1.19
Requires:       crate(tracing-0.1/default) >= 0.1.40
Requires:       crate(uds-windows-1/default) >= 1.1.0
Requires:       crate(uuid-1/default) >= 1.8.0
Requires:       crate(uuid-1/serde) >= 1.8.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-networking) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-networkmanagement) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-networkmanagement-iphelper) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-security-authorization) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-memory) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-windowsprogramming) >= 0.61.0
Requires:       crate(winnow-1/default) >= 1.0.0
Requires:       crate(zbus-macros-5/default) >= 5.15.0
Requires:       crate(zbus-names-4/default) >= 4.3.2
Requires:       crate(zvariant-5/default) >= 5.10.1
Requires:       crate(zvariant-5/enumflags2) >= 5.10.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async-fs) = %{version}

%description
Source code for takopackized Rust crate "zbus"

%package     -n %{name}+async-executor
Summary:        API for D-Bus communication - feature "async-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-executor-1/default) >= 1.11.0
Provides:       crate(%{pkgname}/async-executor) = %{version}

%description -n %{name}+async-executor
This metapackage enables feature "async-executor" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-io
Summary:        API for D-Bus communication - feature "async-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-executor) = %{version}
Requires:       crate(%{pkgname}/async-fs) = %{version}
Requires:       crate(%{pkgname}/async-lock) = %{version}
Requires:       crate(%{pkgname}/async-process) = %{version}
Requires:       crate(%{pkgname}/async-task) = %{version}
Requires:       crate(%{pkgname}/blocking) = %{version}
Requires:       crate(async-io-2/default) >= 2.3.2
Provides:       crate(%{pkgname}/async-io) = %{version}

%description -n %{name}+async-io
This metapackage enables feature "async-io" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-lock
Summary:        API for D-Bus communication - feature "async-lock"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-lock-3/default) >= 3.3.0
Provides:       crate(%{pkgname}/async-lock) = %{version}

%description -n %{name}+async-lock
This metapackage enables feature "async-lock" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-process
Summary:        API for D-Bus communication - feature "async-process"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-process-2/default) >= 2.2.2
Provides:       crate(%{pkgname}/async-process) = %{version}

%description -n %{name}+async-process
This metapackage enables feature "async-process" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-task
Summary:        API for D-Bus communication - feature "async-task"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-task-4/default) >= 4.7.1
Provides:       crate(%{pkgname}/async-task) = %{version}

%description -n %{name}+async-task
This metapackage enables feature "async-task" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking
Summary:        API for D-Bus communication - feature "blocking"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(blocking-1/default) >= 1.6.0
Provides:       crate(%{pkgname}/blocking) = %{version}

%description -n %{name}+blocking
This metapackage enables feature "blocking" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-api
Summary:        API for D-Bus communication - feature "blocking-api"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zbus-macros-5/blocking-api) >= 5.15.0
Provides:       crate(%{pkgname}/blocking-api) = %{version}

%description -n %{name}+blocking-api
This metapackage enables feature "blocking-api" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+camino
Summary:        API for D-Bus communication - feature "camino"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zvariant-5/camino) >= 5.10.1
Requires:       crate(zvariant-5/enumflags2) >= 5.10.1
Provides:       crate(%{pkgname}/camino) = %{version}

%description -n %{name}+camino
This metapackage enables feature "camino" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        API for D-Bus communication - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zvariant-5/chrono) >= 5.10.1
Requires:       crate(zvariant-5/enumflags2) >= 5.10.1
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        API for D-Bus communication - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-io) = %{version}
Requires:       crate(%{pkgname}/blocking-api) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+heapless
Summary:        API for D-Bus communication - feature "heapless"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zvariant-5/enumflags2) >= 5.10.1
Requires:       crate(zvariant-5/heapless) >= 5.10.1
Provides:       crate(%{pkgname}/heapless) = %{version}

%description -n %{name}+heapless
This metapackage enables feature "heapless" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+option-as-array
Summary:        API for D-Bus communication - feature "option-as-array"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zvariant-5/enumflags2) >= 5.10.1
Requires:       crate(zvariant-5/option-as-array) >= 5.10.1
Provides:       crate(%{pkgname}/option-as-array) = %{version}

%description -n %{name}+option-as-array
This metapackage enables feature "option-as-array" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+p2p
Summary:        API for D-Bus communication - feature "p2p" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1/serde) >= 1.8.0
Requires:       crate(uuid-1/v4) >= 1.8.0
Provides:       crate(%{pkgname}/bus-impl) = %{version}
Provides:       crate(%{pkgname}/p2p) = %{version}

%description -n %{name}+p2p
This metapackage enables feature "p2p" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bus-impl" feature.

%package     -n %{name}+serde-bytes
Summary:        API for D-Bus communication - feature "serde_bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zvariant-5/enumflags2) >= 5.10.1
Requires:       crate(zvariant-5/serde-bytes) >= 5.10.1
Provides:       crate(%{pkgname}/serde-bytes) = %{version}

%description -n %{name}+serde-bytes
This metapackage enables feature "serde_bytes" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        API for D-Bus communication - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zvariant-5/enumflags2) >= 5.10.1
Requires:       crate(zvariant-5/time) >= 5.10.1
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        API for D-Bus communication - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.37.0
Requires:       crate(tokio-1/fs) >= 1.37.0
Requires:       crate(tokio-1/io-util) >= 1.37.0
Requires:       crate(tokio-1/net) >= 1.37.0
Requires:       crate(tokio-1/process) >= 1.37.0
Requires:       crate(tokio-1/rt) >= 1.37.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.37.0
Requires:       crate(tokio-1/sync) >= 1.37.0
Requires:       crate(tokio-1/time) >= 1.37.0
Requires:       crate(tokio-1/tracing) >= 1.37.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-vsock
Summary:        API for D-Bus communication - feature "tokio-vsock"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(tokio-vsock-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-vsock) = %{version}

%description -n %{name}+tokio-vsock
This metapackage enables feature "tokio-vsock" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+url
Summary:        API for D-Bus communication - feature "url"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zvariant-5/enumflags2) >= 5.10.1
Requires:       crate(zvariant-5/url) >= 5.10.1
Provides:       crate(%{pkgname}/url) = %{version}

%description -n %{name}+url
This metapackage enables feature "url" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        API for D-Bus communication - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zvariant-5/enumflags2) >= 5.10.1
Requires:       crate(zvariant-5/uuid) >= 5.10.1
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vsock
Summary:        API for D-Bus communication - feature "vsock"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-io-2/default) >= 2.3.2
Requires:       crate(vsock-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/vsock) = %{version}

%description -n %{name}+vsock
This metapackage enables feature "vsock" for the Rust zbus crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
