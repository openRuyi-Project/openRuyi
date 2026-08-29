# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-std
%global full_version 1.13.2
%global pkgname async-std-1

Name:           rust-async-std-1
Version:        1.13.2
Release:        %autorelease
Summary:        Rust crate "async-std"
License:        Apache-2.0 OR MIT
URL:            https://async.rs
#!RemoteAsset:  sha256:2c8e079a4ab67ae52b7403632e4618815d6db36d2a010cfe41b02c1b1578f93b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:         0001-fix-range-dependencies.patch

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/io-safety) = %{version}

%description
Source code for takopackized Rust crate "async-std"

%package     -n %{name}+alloc
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(futures-core-0.3/alloc) >= 0.3.4
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-attributes
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "async-attributes" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-attributes-1/default) >= 1.1.2
Provides:       crate(%{pkgname}/async-attributes) = %{version}
Provides:       crate(%{pkgname}/attributes) = %{version}

%description -n %{name}+async-attributes
This metapackage enables feature "async-attributes" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "attributes" feature.

%package     -n %{name}+async-channel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "async-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-channel-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/async-channel) = %{version}

%description -n %{name}+async-channel
This metapackage enables feature "async-channel" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-global-executor
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "async-global-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-global-executor-2/async-io) >= 2.4.0
Requires:       crate(async-global-executor-2/default) >= 2.4.0
Provides:       crate(%{pkgname}/async-global-executor) = %{version}

%description -n %{name}+async-global-executor
This metapackage enables feature "async-global-executor" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-io
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "async-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-io-2/default) >= 2.2.0
Provides:       crate(%{pkgname}/async-io) = %{version}

%description -n %{name}+async-io
This metapackage enables feature "async-io" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-lock
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "async-lock"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-lock-3/default) >= 3.1.0
Provides:       crate(%{pkgname}/async-lock) = %{version}

%description -n %{name}+async-lock
This metapackage enables feature "async-lock" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-process
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "async-process"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-process-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/async-process) = %{version}

%description -n %{name}+async-process
This metapackage enables feature "async-process" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossbeam-utils
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "crossbeam-utils"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/crossbeam-utils) = %{version}

%description -n %{name}+crossbeam-utils
This metapackage enables feature "crossbeam-utils" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-global-executor) = %{version}
Requires:       crate(%{pkgname}/async-io) = %{version}
Requires:       crate(%{pkgname}/futures-lite) = %{version}
Requires:       crate(%{pkgname}/gloo-timers) = %{version}
Requires:       crate(%{pkgname}/kv-log-macro) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+docs
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "docs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(%{pkgname}/default) = %{version}
Requires:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/docs) = %{version}

%description -n %{name}+docs
This metapackage enables feature "docs" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-channel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "futures-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-channel-0.3/default) >= 0.3.4
Provides:       crate(%{pkgname}/futures-channel) = %{version}

%description -n %{name}+futures-channel
This metapackage enables feature "futures-channel" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "futures-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.4
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-io
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/default) >= 0.3.4
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-lite
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "futures-lite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-lite-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/futures-lite) = %{version}

%description -n %{name}+futures-lite
This metapackage enables feature "futures-lite" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gloo-timers
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "gloo-timers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gloo-timers-0.3/default) >= 0.3.0
Requires:       crate(gloo-timers-0.3/futures) >= 0.3.0
Provides:       crate(%{pkgname}/gloo-timers) = %{version}

%description -n %{name}+gloo-timers
This metapackage enables feature "gloo-timers" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv-log-macro
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "kv-log-macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(kv-log-macro-1/default) >= 1.0.6
Provides:       crate(%{pkgname}/kv-log-macro) = %{version}

%description -n %{name}+kv-log-macro
This metapackage enables feature "kv-log-macro" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.8
Requires:       crate(log-0.4/kv-unstable) >= 0.4.8
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memchr
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "memchr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/default) >= 2.3.3
Provides:       crate(%{pkgname}/memchr) = %{version}

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.3.1
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pin-project-lite
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "pin-project-lite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/pin-project-lite) = %{version}

%description -n %{name}+pin-project-lite
This metapackage enables feature "pin-project-lite" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pin-utils
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "pin-utils"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-utils-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/pin-utils) = %{version}

%description -n %{name}+pin-utils
This metapackage enables feature "pin-utils" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+slab
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "slab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(slab-0.4/default) >= 0.4.2
Provides:       crate(%{pkgname}/slab) = %{version}

%description -n %{name}+slab
This metapackage enables feature "slab" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/async-channel) = %{version}
Requires:       crate(%{pkgname}/async-lock) = %{version}
Requires:       crate(%{pkgname}/crossbeam-utils) = %{version}
Requires:       crate(%{pkgname}/futures-channel) = %{version}
Requires:       crate(%{pkgname}/futures-io) = %{version}
Requires:       crate(%{pkgname}/memchr) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Requires:       crate(%{pkgname}/pin-utils) = %{version}
Requires:       crate(%{pkgname}/slab) = %{version}
Requires:       crate(%{pkgname}/wasm-bindgen-futures) = %{version}
Requires:       crate(futures-core-0.3/std) >= 0.3.4
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+surf
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "surf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(surf-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/surf) = %{version}

%description -n %{name}+surf
This metapackage enables feature "surf" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio02
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "tokio02"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-global-executor-2/async-io) >= 2.4.0
Requires:       crate(async-global-executor-2/tokio02) >= 2.4.0
Provides:       crate(%{pkgname}/tokio02) = %{version}

%description -n %{name}+tokio02
This metapackage enables feature "tokio02" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio03
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "tokio03"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-global-executor-2/async-io) >= 2.4.0
Requires:       crate(async-global-executor-2/tokio03) >= 2.4.0
Provides:       crate(%{pkgname}/tokio03) = %{version}

%description -n %{name}+tokio03
This metapackage enables feature "tokio03" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio1
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "tokio1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-global-executor-2/async-io) >= 2.4.0
Requires:       crate(async-global-executor-2/tokio) >= 2.4.0
Provides:       crate(%{pkgname}/tokio1) = %{version}

%description -n %{name}+tokio1
This metapackage enables feature "tokio1" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-io) = %{version}
Requires:       crate(%{pkgname}/async-process) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen-futures
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard library - feature "wasm-bindgen-futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.10
Provides:       crate(%{pkgname}/wasm-bindgen-futures) = %{version}

%description -n %{name}+wasm-bindgen-futures
This metapackage enables feature "wasm-bindgen-futures" for the Rust async-std crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
