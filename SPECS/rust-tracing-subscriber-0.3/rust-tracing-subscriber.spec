# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tracing-core-0.1) >= 0.1.36
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/regex)

%description
Source code for takopackized Rust crate "tracing-subscriber"

%package     -n %{name}+ansi
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "ansi"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/fmt)
Requires:       crate(%{pkgname}/nu-ansi-term)
Provides:       crate(%{pkgname}/ansi)

%description -n %{name}+ansi
This metapackage enables feature "ansi" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "chrono"
Requires:       crate(%{pkgname})
Requires:       crate(chrono-0.4/clock) >= 0.4.26
Requires:       crate(chrono-0.4/std) >= 0.4.26
Provides:       crate(%{pkgname}/chrono)

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/ansi)
Requires:       crate(%{pkgname}/fmt)
Requires:       crate(%{pkgname}/smallvec)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/tracing-log)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+env-filter
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "env-filter"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/matchers)
Requires:       crate(%{pkgname}/once-cell)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/thread-local)
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(regex-automata-0.4/std) >= 0.4.14
Provides:       crate(%{pkgname}/env-filter)

%description -n %{name}+env-filter
This metapackage enables feature "env-filter" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fmt
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "fmt"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/registry)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/fmt)

%description -n %{name}+fmt
This metapackage enables feature "fmt" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "json"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/serde-json)
Requires:       crate(%{pkgname}/tracing-serde)
Provides:       crate(%{pkgname}/json)

%description -n %{name}+json
This metapackage enables feature "json" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+local-time
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "local-time"
Requires:       crate(%{pkgname})
Requires:       crate(time-0.3/formatting) >= 0.3.2
Requires:       crate(time-0.3/local-offset) >= 0.3.2
Provides:       crate(%{pkgname}/local-time)

%description -n %{name}+local-time
This metapackage enables feature "local-time" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+matchers
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "matchers"
Requires:       crate(%{pkgname})
Requires:       crate(matchers-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/matchers)

%description -n %{name}+matchers
This metapackage enables feature "matchers" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nu-ansi-term
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "nu-ansi-term"
Requires:       crate(%{pkgname})
Requires:       crate(nu-ansi-term-0.50/default) >= 0.50.3
Provides:       crate(%{pkgname}/nu-ansi-term)

%description -n %{name}+nu-ansi-term
This metapackage enables feature "nu-ansi-term" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "once_cell"
Requires:       crate(%{pkgname})
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Provides:       crate(%{pkgname}/once-cell)

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking-lot
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "parking_lot"
Requires:       crate(%{pkgname})
Requires:       crate(parking-lot-0.12/default) >= 0.12.1
Provides:       crate(%{pkgname}/parking-lot)

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+registry
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "registry"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/sharded-slab)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/thread-local)
Provides:       crate(%{pkgname}/registry)

%description -n %{name}+registry
This metapackage enables feature "registry" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.140
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "serde_json"
Requires:       crate(%{pkgname})
Requires:       crate(serde-json-1.0/default) >= 1.0.82
Provides:       crate(%{pkgname}/serde-json)

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sharded-slab
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "sharded-slab"
Requires:       crate(%{pkgname})
Requires:       crate(sharded-slab-0.1/default) >= 0.1.7
Provides:       crate(%{pkgname}/sharded-slab)

%description -n %{name}+sharded-slab
This metapackage enables feature "sharded-slab" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "smallvec"
Requires:       crate(%{pkgname})
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Provides:       crate(%{pkgname}/smallvec)

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(tracing-core-0.1/std) >= 0.1.36
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thread-local
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "thread_local"
Requires:       crate(%{pkgname})
Requires:       crate(thread-local-1.0/default) >= 1.1.9
Provides:       crate(%{pkgname}/thread-local)

%description -n %{name}+thread-local
This metapackage enables feature "thread_local" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "time"
Requires:       crate(%{pkgname})
Requires:       crate(time-0.3/default) >= 0.3.2
Requires:       crate(time-0.3/formatting) >= 0.3.2
Provides:       crate(%{pkgname}/time)

%description -n %{name}+time
This metapackage enables feature "time" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1) >= 0.1.44
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-log
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "tracing-log"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-log-0.2/log-tracer) >= 0.2.0
Requires:       crate(tracing-log-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/tracing-log)

%description -n %{name}+tracing-log
This metapackage enables feature "tracing-log" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-serde
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "tracing-serde"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-serde-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/tracing-serde)

%description -n %{name}+tracing-serde
This metapackage enables feature "tracing-serde" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+valuable
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "valuable"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/valuable-crate)
Requires:       crate(%{pkgname}/valuable-serde)
Requires:       crate(tracing-core-0.1/valuable) >= 0.1.36
Requires:       crate(tracing-serde-0.2/valuable) >= 0.2.0
Provides:       crate(%{pkgname}/valuable)

%description -n %{name}+valuable
This metapackage enables feature "valuable" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+valuable-serde
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "valuable-serde"
Requires:       crate(%{pkgname})
Requires:       crate(valuable-serde-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/valuable-serde)

%description -n %{name}+valuable-serde
This metapackage enables feature "valuable-serde" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+valuable-crate
Summary:        Utilities for implementing and composing `tracing` subscribers - feature "valuable_crate"
Requires:       crate(%{pkgname})
Requires:       crate(valuable-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/valuable-crate)

%description -n %{name}+valuable-crate
This metapackage enables feature "valuable_crate" for the Rust tracing-subscriber crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
