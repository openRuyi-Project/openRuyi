# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyper-util
%global full_version 0.1.20
%global pkgname hyper-util-0.1

Name:           rust-hyper-util-0.1
Version:        0.1.20
Release:        %autorelease
Summary:        Rust crate "hyper-util"
License:        MIT
URL:            https://hyper.rs
#!RemoteAsset:  sha256:96547c2556ec9d12fb1578c4eaf448b04993e7fb79cbaad930a656880a6bdfa0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1.0/default) >= 1.11.1
Requires:       crate(http-1.0/default) >= 1.4.0
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(hyper-1.0/default) >= 1.9.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/internal-happy-eyeballs-tests)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "hyper-util"

%package     -n %{name}+client
Summary:        Hyper utilities - feature "client"
Requires:       crate(%{pkgname})
Requires:       crate(futures-channel-0.3/default) >= 0.3.32
Requires:       crate(hyper-1.0/client) >= 1.9.0
Requires:       crate(tokio-1.0/net) >= 1.50.0
Requires:       crate(tower-service-0.3/default) >= 0.3.3
Requires:       crate(tracing-0.1/std) >= 0.1.44
Provides:       crate(%{pkgname}/client)

%description -n %{name}+client
This metapackage enables feature "client" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+client-legacy
Summary:        Hyper utilities - feature "client-legacy"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/client)
Requires:       crate(futures-util-0.3) >= 0.3.32
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(socket2-0.6/all) >= 0.6.3
Requires:       crate(socket2-0.6/default) >= 0.6.3
Requires:       crate(tokio-1.0/sync) >= 1.50.0
Provides:       crate(%{pkgname}/client-legacy)

%description -n %{name}+client-legacy
This metapackage enables feature "client-legacy" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+client-pool
Summary:        Hyper utilities - feature "client-pool"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/client)
Requires:       crate(futures-util-0.3) >= 0.3.32
Requires:       crate(tower-layer-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/client-pool)

%description -n %{name}+client-pool
This metapackage enables feature "client-pool" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+client-proxy
Summary:        Hyper utilities - feature "client-proxy"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/client)
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(ipnet-2.0/default) >= 2.12.0
Requires:       crate(percent-encoding-2.0/default) >= 2.3.2
Provides:       crate(%{pkgname}/client-proxy)

%description -n %{name}+client-proxy
This metapackage enables feature "client-proxy" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+client-proxy-system
Summary:        Hyper utilities - feature "client-proxy-system"
Requires:       crate(%{pkgname})
Requires:       crate(system-configuration-0.7/default) >= 0.7.0
Requires:       crate(windows-registry-0.6/default) >= 0.6.1
Provides:       crate(%{pkgname}/client-proxy-system)

%description -n %{name}+client-proxy-system
This metapackage enables feature "client-proxy-system" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Hyper utilities - feature "full"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/client)
Requires:       crate(%{pkgname}/client-legacy)
Requires:       crate(%{pkgname}/client-pool)
Requires:       crate(%{pkgname}/client-proxy)
Requires:       crate(%{pkgname}/client-proxy-system)
Requires:       crate(%{pkgname}/http1)
Requires:       crate(%{pkgname}/http2)
Requires:       crate(%{pkgname}/server)
Requires:       crate(%{pkgname}/server-auto)
Requires:       crate(%{pkgname}/server-graceful)
Requires:       crate(%{pkgname}/service)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/tracing)
Provides:       crate(%{pkgname}/full)

%description -n %{name}+full
This metapackage enables feature "full" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http1
Summary:        Hyper utilities - feature "http1"
Requires:       crate(%{pkgname})
Requires:       crate(hyper-1.0/http1) >= 1.9.0
Provides:       crate(%{pkgname}/http1)

%description -n %{name}+http1
This metapackage enables feature "http1" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http2
Summary:        Hyper utilities - feature "http2"
Requires:       crate(%{pkgname})
Requires:       crate(hyper-1.0/http2) >= 1.9.0
Provides:       crate(%{pkgname}/http2)

%description -n %{name}+http2
This metapackage enables feature "http2" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+server
Summary:        Hyper utilities - feature "server"
Requires:       crate(%{pkgname})
Requires:       crate(hyper-1.0/server) >= 1.9.0
Provides:       crate(%{pkgname}/server)

%description -n %{name}+server
This metapackage enables feature "server" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+server-auto
Summary:        Hyper utilities - feature "server-auto"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/http1)
Requires:       crate(%{pkgname}/http2)
Requires:       crate(%{pkgname}/server)
Provides:       crate(%{pkgname}/server-auto)

%description -n %{name}+server-auto
This metapackage enables feature "server-auto" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+server-graceful
Summary:        Hyper utilities - feature "server-graceful"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/server)
Requires:       crate(tokio-1.0/sync) >= 1.50.0
Provides:       crate(%{pkgname}/server-graceful)

%description -n %{name}+server-graceful
This metapackage enables feature "server-graceful" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+service
Summary:        Hyper utilities - feature "service"
Requires:       crate(%{pkgname})
Requires:       crate(tower-service-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname}/service)

%description -n %{name}+service
This metapackage enables feature "service" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Hyper utilities - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0) >= 1.50.0
Requires:       crate(tokio-1.0/rt) >= 1.50.0
Requires:       crate(tokio-1.0/time) >= 1.50.0
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Hyper utilities - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1/std) >= 0.1.44
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust hyper-util crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
