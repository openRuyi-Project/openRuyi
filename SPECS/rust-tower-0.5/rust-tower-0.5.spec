# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tower
%global full_version 0.5.3
%global pkgname tower-0.5

Name:           rust-tower-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "tower"
License:        MIT
URL:            https://github.com/tower-rs/tower
#!RemoteAsset:  sha256:ebe5ef63511595f1344e2d5cfa636d973292adc0eec1f0ad45fae9f0851ab1d4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tower-layer-0.3/default) >= 0.3.3
Requires:       crate(tower-service-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/steer) = %{version}
Provides:       crate(%{pkgname}/tokio-stream) = %{version}

%description
Source code for takopackized Rust crate "tower"

%package     -n %{name}+balance
Summary:        Modular and reusable components for building robust clients and servers - feature "balance"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/discover) = %{version}
Requires:       crate(%{pkgname}/load) = %{version}
Requires:       crate(%{pkgname}/make) = %{version}
Requires:       crate(%{pkgname}/ready-cache) = %{version}
Requires:       crate(%{pkgname}/slab) = %{version}
Requires:       crate(%{pkgname}/util) = %{version}
Provides:       crate(%{pkgname}/balance) = %{version}

%description -n %{name}+balance
This metapackage enables feature "balance" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+buffer
Summary:        Modular and reusable components for building robust clients and servers - feature "buffer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(tokio-1/rt) >= 1.6.2
Requires:       crate(tokio-1/sync) >= 1.6.2
Provides:       crate(%{pkgname}/buffer) = %{version}

%description -n %{name}+buffer
This metapackage enables feature "buffer" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+discover
Summary:        Modular and reusable components for building robust clients and servers - feature "discover"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Provides:       crate(%{pkgname}/discover) = %{version}

%description -n %{name}+discover
This metapackage enables feature "discover" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+filter
Summary:        Modular and reusable components for building robust clients and servers - feature "filter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-util) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Provides:       crate(%{pkgname}/filter) = %{version}

%description -n %{name}+filter
This metapackage enables feature "filter" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Modular and reusable components for building robust clients and servers - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/balance) = %{version}
Requires:       crate(%{pkgname}/buffer) = %{version}
Requires:       crate(%{pkgname}/discover) = %{version}
Requires:       crate(%{pkgname}/filter) = %{version}
Requires:       crate(%{pkgname}/hedge) = %{version}
Requires:       crate(%{pkgname}/limit) = %{version}
Requires:       crate(%{pkgname}/load) = %{version}
Requires:       crate(%{pkgname}/load-shed) = %{version}
Requires:       crate(%{pkgname}/make) = %{version}
Requires:       crate(%{pkgname}/ready-cache) = %{version}
Requires:       crate(%{pkgname}/reconnect) = %{version}
Requires:       crate(%{pkgname}/retry) = %{version}
Requires:       crate(%{pkgname}/spawn-ready) = %{version}
Requires:       crate(%{pkgname}/steer) = %{version}
Requires:       crate(%{pkgname}/timeout) = %{version}
Requires:       crate(%{pkgname}/util) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core
Summary:        Modular and reusable components for building robust clients and servers - feature "futures-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/default) >= 0.3.22
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-util
Summary:        Modular and reusable components for building robust clients and servers - feature "futures-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-0.3/alloc) >= 0.3.22
Provides:       crate(%{pkgname}/futures-util) = %{version}

%description -n %{name}+futures-util
This metapackage enables feature "futures-util" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hdrhistogram
Summary:        Modular and reusable components for building robust clients and servers - feature "hdrhistogram"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hdrhistogram-7) >= 7.0.0
Provides:       crate(%{pkgname}/hdrhistogram) = %{version}

%description -n %{name}+hdrhistogram
This metapackage enables feature "hdrhistogram" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hedge
Summary:        Modular and reusable components for building robust clients and servers - feature "hedge"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/filter) = %{version}
Requires:       crate(%{pkgname}/futures-util) = %{version}
Requires:       crate(%{pkgname}/hdrhistogram) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(%{pkgname}/util) = %{version}
Requires:       crate(tokio-1/time) >= 1.6.2
Provides:       crate(%{pkgname}/hedge) = %{version}

%description -n %{name}+hedge
This metapackage enables feature "hedge" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Modular and reusable components for building robust clients and servers - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.0.2
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+limit
Summary:        Modular and reusable components for building robust clients and servers - feature "limit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(tokio-1/sync) >= 1.6.2
Requires:       crate(tokio-1/time) >= 1.6.2
Provides:       crate(%{pkgname}/limit) = %{version}

%description -n %{name}+limit
This metapackage enables feature "limit" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+load
Summary:        Modular and reusable components for building robust clients and servers - feature "load"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(tokio-1/time) >= 1.6.2
Provides:       crate(%{pkgname}/load) = %{version}

%description -n %{name}+load
This metapackage enables feature "load" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Modular and reusable components for building robust clients and servers - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/log) >= 0.1.2
Requires:       crate(tracing-0.1/std) >= 0.1.2
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+make
Summary:        Modular and reusable components for building robust clients and servers - feature "make"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/make) = %{version}

%description -n %{name}+make
This metapackage enables feature "make" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pin-project-lite
Summary:        Modular and reusable components for building robust clients and servers - feature "pin-project-lite" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.7
Provides:       crate(%{pkgname}/load-shed) = %{version}
Provides:       crate(%{pkgname}/pin-project-lite) = %{version}

%description -n %{name}+pin-project-lite
This metapackage enables feature "pin-project-lite" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "load-shed" feature.

%package     -n %{name}+ready-cache
Summary:        Modular and reusable components for building robust clients and servers - feature "ready-cache"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/futures-util) = %{version}
Requires:       crate(%{pkgname}/indexmap) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(tokio-1/sync) >= 1.6.2
Provides:       crate(%{pkgname}/ready-cache) = %{version}

%description -n %{name}+ready-cache
This metapackage enables feature "ready-cache" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reconnect
Summary:        Modular and reusable components for building robust clients and servers - feature "reconnect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/make) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Provides:       crate(%{pkgname}/reconnect) = %{version}

%description -n %{name}+reconnect
This metapackage enables feature "reconnect" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+retry
Summary:        Modular and reusable components for building robust clients and servers - feature "retry"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/util) = %{version}
Requires:       crate(tokio-1/time) >= 1.6.2
Provides:       crate(%{pkgname}/retry) = %{version}

%description -n %{name}+retry
This metapackage enables feature "retry" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+slab
Summary:        Modular and reusable components for building robust clients and servers - feature "slab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(slab-0.4/default) >= 0.4.9
Provides:       crate(%{pkgname}/slab) = %{version}

%description -n %{name}+slab
This metapackage enables feature "slab" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spawn-ready
Summary:        Modular and reusable components for building robust clients and servers - feature "spawn-ready"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-util) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(%{pkgname}/util) = %{version}
Requires:       crate(tokio-1/rt) >= 1.6.2
Requires:       crate(tokio-1/sync) >= 1.6.2
Provides:       crate(%{pkgname}/spawn-ready) = %{version}

%description -n %{name}+spawn-ready
This metapackage enables feature "spawn-ready" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sync-wrapper
Summary:        Modular and reusable components for building robust clients and servers - feature "sync_wrapper"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sync-wrapper-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/sync-wrapper) = %{version}

%description -n %{name}+sync-wrapper
This metapackage enables feature "sync_wrapper" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+timeout
Summary:        Modular and reusable components for building robust clients and servers - feature "timeout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(tokio-1/time) >= 1.6.2
Provides:       crate(%{pkgname}/timeout) = %{version}

%description -n %{name}+timeout
This metapackage enables feature "timeout" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Modular and reusable components for building robust clients and servers - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.6.2
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-util
Summary:        Modular and reusable components for building robust clients and servers - feature "tokio-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-util-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-util) = %{version}

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Modular and reusable components for building robust clients and servers - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/std) >= 0.1.2
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+util
Summary:        Modular and reusable components for building robust clients and servers - feature "util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/futures-util) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/sync-wrapper) = %{version}
Provides:       crate(%{pkgname}/util) = %{version}

%description -n %{name}+util
This metapackage enables feature "util" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
