# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tower-layer-0.3/default) >= 0.3.3
Requires:       crate(tower-service-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/steer)
Provides:       crate(%{pkgname}/tokio-stream)

%description
Source code for takopackized Rust crate "tower"

%package     -n %{name}+balance
Summary:        Modular and reusable components for building robust clients and servers - feature "balance"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/discover)
Requires:       crate(%{pkgname}/load)
Requires:       crate(%{pkgname}/make)
Requires:       crate(%{pkgname}/ready-cache)
Requires:       crate(%{pkgname}/slab)
Requires:       crate(%{pkgname}/util)
Provides:       crate(%{pkgname}/balance)

%description -n %{name}+balance
This metapackage enables feature "balance" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+buffer
Summary:        Modular and reusable components for building robust clients and servers - feature "buffer"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pin-project-lite)
Requires:       crate(%{pkgname}/tokio-util)
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(tokio-1.0/rt) >= 1.50.0
Requires:       crate(tokio-1.0/sync) >= 1.50.0
Provides:       crate(%{pkgname}/buffer)

%description -n %{name}+buffer
This metapackage enables feature "buffer" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+discover
Summary:        Modular and reusable components for building robust clients and servers - feature "discover"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/pin-project-lite)
Provides:       crate(%{pkgname}/discover)

%description -n %{name}+discover
This metapackage enables feature "discover" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+filter
Summary:        Modular and reusable components for building robust clients and servers - feature "filter"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-util)
Requires:       crate(%{pkgname}/pin-project-lite)
Provides:       crate(%{pkgname}/filter)

%description -n %{name}+filter
This metapackage enables feature "filter" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Modular and reusable components for building robust clients and servers - feature "full"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/balance)
Requires:       crate(%{pkgname}/buffer)
Requires:       crate(%{pkgname}/discover)
Requires:       crate(%{pkgname}/filter)
Requires:       crate(%{pkgname}/hedge)
Requires:       crate(%{pkgname}/limit)
Requires:       crate(%{pkgname}/load)
Requires:       crate(%{pkgname}/load-shed)
Requires:       crate(%{pkgname}/make)
Requires:       crate(%{pkgname}/ready-cache)
Requires:       crate(%{pkgname}/reconnect)
Requires:       crate(%{pkgname}/retry)
Requires:       crate(%{pkgname}/spawn-ready)
Requires:       crate(%{pkgname}/steer)
Requires:       crate(%{pkgname}/timeout)
Requires:       crate(%{pkgname}/util)
Provides:       crate(%{pkgname}/full)

%description -n %{name}+full
This metapackage enables feature "full" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core
Summary:        Modular and reusable components for building robust clients and servers - feature "futures-core"
Requires:       crate(%{pkgname})
Requires:       crate(futures-core-0.3/default) >= 0.3.32
Provides:       crate(%{pkgname}/futures-core)

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-util
Summary:        Modular and reusable components for building robust clients and servers - feature "futures-util"
Requires:       crate(%{pkgname})
Requires:       crate(futures-util-0.3/alloc) >= 0.3.32
Provides:       crate(%{pkgname}/futures-util)

%description -n %{name}+futures-util
This metapackage enables feature "futures-util" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hdrhistogram
Summary:        Modular and reusable components for building robust clients and servers - feature "hdrhistogram"
Requires:       crate(%{pkgname})
Requires:       crate(hdrhistogram-7.0) >= 7.0.0
Provides:       crate(%{pkgname}/hdrhistogram)

%description -n %{name}+hdrhistogram
This metapackage enables feature "hdrhistogram" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hedge
Summary:        Modular and reusable components for building robust clients and servers - feature "hedge"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/filter)
Requires:       crate(%{pkgname}/futures-util)
Requires:       crate(%{pkgname}/hdrhistogram)
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(%{pkgname}/util)
Requires:       crate(tokio-1.0/time) >= 1.50.0
Provides:       crate(%{pkgname}/hedge)

%description -n %{name}+hedge
This metapackage enables feature "hedge" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Modular and reusable components for building robust clients and servers - feature "indexmap"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/default) >= 2.0.2
Provides:       crate(%{pkgname}/indexmap)

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+limit
Summary:        Modular and reusable components for building robust clients and servers - feature "limit"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pin-project-lite)
Requires:       crate(%{pkgname}/tokio-util)
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(tokio-1.0/sync) >= 1.50.0
Requires:       crate(tokio-1.0/time) >= 1.50.0
Provides:       crate(%{pkgname}/limit)

%description -n %{name}+limit
This metapackage enables feature "limit" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+load
Summary:        Modular and reusable components for building robust clients and servers - feature "load"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pin-project-lite)
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(tokio-1.0/time) >= 1.50.0
Provides:       crate(%{pkgname}/load)

%description -n %{name}+load
This metapackage enables feature "load" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Modular and reusable components for building robust clients and servers - feature "log"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1/log) >= 0.1.2
Requires:       crate(tracing-0.1/std) >= 0.1.2
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+make
Summary:        Modular and reusable components for building robust clients and servers - feature "make"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pin-project-lite)
Requires:       crate(%{pkgname}/tokio)
Provides:       crate(%{pkgname}/make)

%description -n %{name}+make
This metapackage enables feature "make" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pin-project-lite
Summary:        Modular and reusable components for building robust clients and servers - feature "pin-project-lite" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Provides:       crate(%{pkgname}/load-shed)
Provides:       crate(%{pkgname}/pin-project-lite)

%description -n %{name}+pin-project-lite
This metapackage enables feature "pin-project-lite" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "load-shed" feature.

%package     -n %{name}+ready-cache
Summary:        Modular and reusable components for building robust clients and servers - feature "ready-cache"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/futures-util)
Requires:       crate(%{pkgname}/indexmap)
Requires:       crate(%{pkgname}/pin-project-lite)
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(tokio-1.0/sync) >= 1.50.0
Provides:       crate(%{pkgname}/ready-cache)

%description -n %{name}+ready-cache
This metapackage enables feature "ready-cache" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reconnect
Summary:        Modular and reusable components for building robust clients and servers - feature "reconnect"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/make)
Requires:       crate(%{pkgname}/tracing)
Provides:       crate(%{pkgname}/reconnect)

%description -n %{name}+reconnect
This metapackage enables feature "reconnect" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+retry
Summary:        Modular and reusable components for building robust clients and servers - feature "retry"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/util)
Requires:       crate(tokio-1.0/time) >= 1.50.0
Provides:       crate(%{pkgname}/retry)

%description -n %{name}+retry
This metapackage enables feature "retry" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+slab
Summary:        Modular and reusable components for building robust clients and servers - feature "slab"
Requires:       crate(%{pkgname})
Requires:       crate(slab-0.4/default) >= 0.4.9
Provides:       crate(%{pkgname}/slab)

%description -n %{name}+slab
This metapackage enables feature "slab" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spawn-ready
Summary:        Modular and reusable components for building robust clients and servers - feature "spawn-ready"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-util)
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(%{pkgname}/util)
Requires:       crate(tokio-1.0/rt) >= 1.50.0
Requires:       crate(tokio-1.0/sync) >= 1.50.0
Provides:       crate(%{pkgname}/spawn-ready)

%description -n %{name}+spawn-ready
This metapackage enables feature "spawn-ready" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sync-wrapper
Summary:        Modular and reusable components for building robust clients and servers - feature "sync_wrapper"
Requires:       crate(%{pkgname})
Requires:       crate(sync-wrapper-1.0/default) >= 1.0.2
Provides:       crate(%{pkgname}/sync-wrapper)

%description -n %{name}+sync-wrapper
This metapackage enables feature "sync_wrapper" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+timeout
Summary:        Modular and reusable components for building robust clients and servers - feature "timeout"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pin-project-lite)
Requires:       crate(tokio-1.0/time) >= 1.50.0
Provides:       crate(%{pkgname}/timeout)

%description -n %{name}+timeout
This metapackage enables feature "timeout" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Modular and reusable components for building robust clients and servers - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/default) >= 1.50.0
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-util
Summary:        Modular and reusable components for building robust clients and servers - feature "tokio-util"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-util-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-util)

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Modular and reusable components for building robust clients and servers - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1/std) >= 0.1.2
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+util
Summary:        Modular and reusable components for building robust clients and servers - feature "util"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/futures-util)
Requires:       crate(%{pkgname}/pin-project-lite)
Requires:       crate(%{pkgname}/sync-wrapper)
Provides:       crate(%{pkgname}/util)

%description -n %{name}+util
This metapackage enables feature "util" for the Rust tower crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
