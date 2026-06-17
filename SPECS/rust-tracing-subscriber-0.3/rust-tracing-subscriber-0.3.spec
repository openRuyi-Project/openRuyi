# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-subscriber
%global full_version 0.3.23
%global pkgname tracing-subscriber-0.3

Name:           rust-tracing-subscriber-0.3
Version:        0.3.23
Release:        %autorelease
Summary:        Rust crate "tracing-subscriber"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:cb7f578e5945fb242538965c2d0b04418d38ec25c79d160cd279bf0731c8d319
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tracing-core-0.1) >= 0.1.35
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/regex) = %{version}

%description
Source code for takopackized Rust crate "tracing-subscriber"

%package     -n %{name}+ansi
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "ansi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fmt) = %{version}
Requires:       crate(%{pkgname}/nu-ansi-term) = %{version}
Provides:       crate(%{pkgname}/ansi) = %{version}

%description -n %{name}+ansi
This metapackage enables feature "ansi" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.26
Requires:       crate(chrono-0.4/std) >= 0.4.26
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ansi) = %{version}
Requires:       crate(%{pkgname}/fmt) = %{version}
Requires:       crate(%{pkgname}/smallvec) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tracing-log) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+env-filter
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "env-filter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/matchers) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/thread-local) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(regex-automata-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/env-filter) = %{version}

%description -n %{name}+env-filter
This metapackage enables feature "env-filter" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fmt
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "fmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/registry) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/fmt) = %{version}

%description -n %{name}+fmt
This metapackage enables feature "fmt" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(%{pkgname}/tracing-serde) = %{version}
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+local-time
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "local-time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/formatting) >= 0.3.2
Requires:       crate(time-0.3/local-offset) >= 0.3.2
Provides:       crate(%{pkgname}/local-time) = %{version}

%description -n %{name}+local-time
This metapackage enables feature "local-time" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+matchers
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "matchers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(matchers-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/matchers) = %{version}

%description -n %{name}+matchers
This metapackage enables feature "matchers" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nu-ansi-term
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "nu-ansi-term"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nu-ansi-term-0.50/default) >= 0.50.0
Provides:       crate(%{pkgname}/nu-ansi-term) = %{version}

%description -n %{name}+nu-ansi-term
This metapackage enables feature "nu-ansi-term" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.13.0
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking-lot
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "parking_lot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-0.12/default) >= 0.12.1
Provides:       crate(%{pkgname}/parking-lot) = %{version}

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+registry
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "registry"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sharded-slab) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/thread-local) = %{version}
Provides:       crate(%{pkgname}/registry) = %{version}

%description -n %{name}+registry
This metapackage enables feature "registry" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.140
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.82
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sharded-slab
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "sharded-slab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sharded-slab-0.1/default) >= 0.1.4
Provides:       crate(%{pkgname}/sharded-slab) = %{version}

%description -n %{name}+sharded-slab
This metapackage enables feature "sharded-slab" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1/default) >= 1.9.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(tracing-core-0.1/std) >= 0.1.35
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thread-local
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "thread_local"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(thread-local-1/default) >= 1.1.4
Provides:       crate(%{pkgname}/thread-local) = %{version}

%description -n %{name}+thread-local
This metapackage enables feature "thread_local" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/default) >= 0.3.2
Requires:       crate(time-0.3/formatting) >= 0.3.2
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.43
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-log
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "tracing-log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-log-0.2/log-tracer) >= 0.2.0
Requires:       crate(tracing-log-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/tracing-log) = %{version}

%description -n %{name}+tracing-log
This metapackage enables feature "tracing-log" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-serde
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "tracing-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-serde-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/tracing-serde) = %{version}

%description -n %{name}+tracing-serde
This metapackage enables feature "tracing-serde" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+valuable
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "valuable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/valuable-crate) = %{version}
Requires:       crate(%{pkgname}/valuable-serde) = %{version}
Requires:       crate(tracing-core-0.1/valuable) >= 0.1.35
Requires:       crate(tracing-serde-0.2/valuable) >= 0.2.0
Provides:       crate(%{pkgname}/valuable) = %{version}

%description -n %{name}+valuable
This metapackage enables feature "valuable" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+valuable-serde
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "valuable-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(valuable-serde-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/valuable-serde) = %{version}

%description -n %{name}+valuable-serde
This metapackage enables feature "valuable-serde" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+valuable-crate
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "valuable_crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(valuable-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/valuable-crate) = %{version}

%description -n %{name}+valuable-crate
This metapackage enables feature "valuable_crate" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
