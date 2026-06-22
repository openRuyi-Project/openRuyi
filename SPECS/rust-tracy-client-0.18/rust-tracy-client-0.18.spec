# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracy-client
%global full_version 0.18.4
%global pkgname tracy-client-0.18

Name:           rust-tracy-client-0.18
Version:        0.18.4
Release:        %autorelease
Summary:        Rust crate "tracy-client"
License:        MIT OR Apache-2.0
URL:            https://github.com/nagisa/rust_tracy_client
#!RemoteAsset:  sha256:a4f6fc3baeac5d86ab90c772e9e30620fc653bf1864295029921a15ef478e6a5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:         0001-fix-range-dependencies.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(loom-0.7/default) >= 0.7.0
Requires:       crate(once-cell-1/default) >= 1.19.0
Requires:       crate(tracy-client-sys-0.28) >= 0.28.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tracy-client"

%package     -n %{name}+broadcast
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "broadcast"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/broadcast) >= 0.28.0
Provides:       crate(%{pkgname}/broadcast) = %{version}

%description -n %{name}+broadcast
This metapackage enables feature "broadcast" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+callstack-inlines
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "callstack-inlines"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/callstack-inlines) >= 0.28.0
Provides:       crate(%{pkgname}/callstack-inlines) = %{version}

%description -n %{name}+callstack-inlines
This metapackage enables feature "callstack-inlines" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+code-transfer
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "code-transfer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/code-transfer) >= 0.28.0
Provides:       crate(%{pkgname}/code-transfer) = %{version}

%description -n %{name}+code-transfer
This metapackage enables feature "code-transfer" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+context-switch-tracing
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "context-switch-tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/context-switch-tracing) >= 0.28.0
Provides:       crate(%{pkgname}/context-switch-tracing) = %{version}

%description -n %{name}+context-switch-tracing
This metapackage enables feature "context-switch-tracing" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crash-handler
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "crash-handler"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/crash-handler) >= 0.28.0
Provides:       crate(%{pkgname}/crash-handler) = %{version}

%description -n %{name}+crash-handler
This metapackage enables feature "crash-handler" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debuginfod
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "debuginfod"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/debuginfod) >= 0.28.0
Provides:       crate(%{pkgname}/debuginfod) = %{version}

%description -n %{name}+debuginfod
This metapackage enables feature "debuginfod" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/broadcast) = %{version}
Requires:       crate(%{pkgname}/callstack-inlines) = %{version}
Requires:       crate(%{pkgname}/code-transfer) = %{version}
Requires:       crate(%{pkgname}/context-switch-tracing) = %{version}
Requires:       crate(%{pkgname}/crash-handler) = %{version}
Requires:       crate(%{pkgname}/enable) = %{version}
Requires:       crate(%{pkgname}/sampling) = %{version}
Requires:       crate(%{pkgname}/system-tracing) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+delayed-init
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "delayed-init"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/delayed-init) >= 0.28.0
Provides:       crate(%{pkgname}/delayed-init) = %{version}

%description -n %{name}+delayed-init
This metapackage enables feature "delayed-init" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+demangle
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "demangle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-demangle-0.1/default) >= 0.1.0
Requires:       crate(tracy-client-sys-0.28/demangle) >= 0.28.0
Provides:       crate(%{pkgname}/demangle) = %{version}

%description -n %{name}+demangle
This metapackage enables feature "demangle" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+enable
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "enable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/enable) >= 0.28.0
Provides:       crate(%{pkgname}/enable) = %{version}

%description -n %{name}+enable
This metapackage enables feature "enable" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fibers
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "fibers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/fibers) >= 0.28.0
Provides:       crate(%{pkgname}/fibers) = %{version}

%description -n %{name}+fibers
This metapackage enables feature "fibers" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flush-on-exit
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "flush-on-exit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/flush-on-exit) >= 0.28.0
Provides:       crate(%{pkgname}/flush-on-exit) = %{version}

%description -n %{name}+flush-on-exit
This metapackage enables feature "flush-on-exit" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+manual-lifetime
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "manual-lifetime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/manual-lifetime) >= 0.28.0
Provides:       crate(%{pkgname}/manual-lifetime) = %{version}

%description -n %{name}+manual-lifetime
This metapackage enables feature "manual-lifetime" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ondemand
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "ondemand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/ondemand) >= 0.28.0
Provides:       crate(%{pkgname}/ondemand) = %{version}

%description -n %{name}+ondemand
This metapackage enables feature "ondemand" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+only-ipv4
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "only-ipv4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/only-ipv4) >= 0.28.0
Provides:       crate(%{pkgname}/only-ipv4) = %{version}

%description -n %{name}+only-ipv4
This metapackage enables feature "only-ipv4" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+only-localhost
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "only-localhost"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/only-localhost) >= 0.28.0
Provides:       crate(%{pkgname}/only-localhost) = %{version}

%description -n %{name}+only-localhost
This metapackage enables feature "only-localhost" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sampling
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "sampling"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/sampling) >= 0.28.0
Provides:       crate(%{pkgname}/sampling) = %{version}

%description -n %{name}+sampling
This metapackage enables feature "sampling" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system-tracing
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "system-tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/system-tracing) >= 0.28.0
Provides:       crate(%{pkgname}/system-tracing) = %{version}

%description -n %{name}+system-tracing
This metapackage enables feature "system-tracing" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+timer-fallback
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "timer-fallback"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/timer-fallback) >= 0.28.0
Provides:       crate(%{pkgname}/timer-fallback) = %{version}

%description -n %{name}+timer-fallback
This metapackage enables feature "timer-fallback" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+verify
Summary:        High level bindings to the client libraries for the Tracy profiler - feature "verify"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracy-client-sys-0.28/verify) >= 0.28.0
Provides:       crate(%{pkgname}/verify) = %{version}

%description -n %{name}+verify
This metapackage enables feature "verify" for the Rust tracy-client crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
