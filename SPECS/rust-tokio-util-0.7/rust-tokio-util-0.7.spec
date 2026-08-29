# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-util
%global full_version 0.7.18
%global pkgname tokio-util-0.7

Name:           rust-tokio-util-0.7
Version:        0.7.18
Release:        %autorelease
Summary:        Rust crate "tokio-util"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:9ae9cec805b01e8fc3fd2fe289f89149a9b66dd16786abd8b19cfa7b48cb0098
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.5.0
Requires:       crate(futures-core-0.3/default) >= 0.3.0
Requires:       crate(futures-sink-0.3/default) >= 0.3.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.11
Requires:       crate(tokio-1/default) >= 1.44.0
Requires:       crate(tokio-1/sync) >= 1.44.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/codec) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/io) = %{version}

%description
Source code for takopackized Rust crate "tokio-util"

%package     -n %{name}+full
Summary:        Additional utilities for working with Tokio - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/codec) = %{version}
Requires:       crate(%{pkgname}/compat) = %{version}
Requires:       crate(%{pkgname}/io-util) = %{version}
Requires:       crate(%{pkgname}/join-map) = %{version}
Requires:       crate(%{pkgname}/net) = %{version}
Requires:       crate(%{pkgname}/rt) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-io
Summary:        Additional utilities for working with Tokio - feature "futures-io" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/compat) = %{version}
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compat" feature.

%package     -n %{name}+futures-util
Summary:        Additional utilities for working with Tokio - feature "futures-util" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/docs-rs) = %{version}
Provides:       crate(%{pkgname}/futures-util) = %{version}

%description -n %{name}+futures-util
This metapackage enables feature "futures-util" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "__docs_rs" feature.

%package     -n %{name}+hashbrown
Summary:        Additional utilities for working with Tokio - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.15) >= 0.15.0
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-util
Summary:        Additional utilities for working with Tokio - feature "io-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/io) = %{version}
Requires:       crate(tokio-1/io-util) >= 1.44.0
Requires:       crate(tokio-1/rt) >= 1.44.0
Requires:       crate(tokio-1/sync) >= 1.44.0
Provides:       crate(%{pkgname}/io-util) = %{version}

%description -n %{name}+io-util
This metapackage enables feature "io-util" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+join-map
Summary:        Additional utilities for working with Tokio - feature "join-map"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hashbrown) = %{version}
Requires:       crate(%{pkgname}/rt) = %{version}
Provides:       crate(%{pkgname}/join-map) = %{version}

%description -n %{name}+join-map
This metapackage enables feature "join-map" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+net
Summary:        Additional utilities for working with Tokio - feature "net"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/net) >= 1.44.0
Requires:       crate(tokio-1/sync) >= 1.44.0
Provides:       crate(%{pkgname}/net) = %{version}

%description -n %{name}+net
This metapackage enables feature "net" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt
Summary:        Additional utilities for working with Tokio - feature "rt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-util) = %{version}
Requires:       crate(tokio-1/rt) >= 1.44.0
Requires:       crate(tokio-1/sync) >= 1.44.0
Provides:       crate(%{pkgname}/rt) = %{version}

%description -n %{name}+rt
This metapackage enables feature "rt" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+slab
Summary:        Additional utilities for working with Tokio - feature "slab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(slab-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/slab) = %{version}

%description -n %{name}+slab
This metapackage enables feature "slab" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Additional utilities for working with Tokio - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/slab) = %{version}
Requires:       crate(tokio-1/sync) >= 1.44.0
Requires:       crate(tokio-1/time) >= 1.44.0
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Additional utilities for working with Tokio - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/std) >= 0.1.29
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust tokio-util crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
