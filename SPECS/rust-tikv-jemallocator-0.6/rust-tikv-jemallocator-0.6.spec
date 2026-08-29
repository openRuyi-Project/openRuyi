# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tikv-jemallocator
%global full_version 0.6.1
%global pkgname tikv-jemallocator-0.6

Name:           rust-tikv-jemallocator-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "tikv-jemallocator"
License:        MIT OR Apache-2.0
URL:            https://github.com/tikv/jemallocator
#!RemoteAsset:  sha256:0359b4327f954e0567e69fb191cf1436617748813819c94b8cd4a431422d053a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2) >= 0.2.8
Requires:       crate(tikv-jemalloc-sys-0.6) >= 0.6.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc-trait) = %{version}

%description
Source code for takopackized Rust crate "tikv-jemallocator"

%package     -n %{name}+background-threads
Summary:        Rust allocator backed by jemalloc - feature "background_threads"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tikv-jemalloc-sys-0.6/background-threads) >= 0.6.1
Provides:       crate(%{pkgname}/background-threads) = %{version}

%description -n %{name}+background-threads
This metapackage enables feature "background_threads" for the Rust tikv-jemallocator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+background-threads-runtime-support
Summary:        Rust allocator backed by jemalloc - feature "background_threads_runtime_support" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tikv-jemalloc-sys-0.6/background-threads-runtime-support) >= 0.6.1
Provides:       crate(%{pkgname}/background-threads-runtime-support) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+background-threads-runtime-support
This metapackage enables feature "background_threads_runtime_support" for the Rust tikv-jemallocator crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+debug
Summary:        Rust allocator backed by jemalloc - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tikv-jemalloc-sys-0.6/debug) >= 0.6.1
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust tikv-jemallocator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+disable-cache-oblivious
Summary:        Rust allocator backed by jemalloc - feature "disable_cache_oblivious"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tikv-jemalloc-sys-0.6/disable-cache-oblivious) >= 0.6.1
Provides:       crate(%{pkgname}/disable-cache-oblivious) = %{version}

%description -n %{name}+disable-cache-oblivious
This metapackage enables feature "disable_cache_oblivious" for the Rust tikv-jemallocator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+disable-initial-exec-tls
Summary:        Rust allocator backed by jemalloc - feature "disable_initial_exec_tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tikv-jemalloc-sys-0.6/disable-initial-exec-tls) >= 0.6.1
Provides:       crate(%{pkgname}/disable-initial-exec-tls) = %{version}

%description -n %{name}+disable-initial-exec-tls
This metapackage enables feature "disable_initial_exec_tls" for the Rust tikv-jemallocator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+override-allocator-on-supported-platforms
Summary:        Rust allocator backed by jemalloc - feature "override_allocator_on_supported_platforms"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/unprefixed-malloc-on-supported-platforms) = %{version}
Requires:       crate(tikv-jemalloc-sys-0.6/override-allocator-on-supported-platforms) >= 0.6.1
Provides:       crate(%{pkgname}/override-allocator-on-supported-platforms) = %{version}

%description -n %{name}+override-allocator-on-supported-platforms
This metapackage enables feature "override_allocator_on_supported_platforms" for the Rust tikv-jemallocator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+profiling
Summary:        Rust allocator backed by jemalloc - feature "profiling"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tikv-jemalloc-sys-0.6/profiling) >= 0.6.1
Provides:       crate(%{pkgname}/profiling) = %{version}

%description -n %{name}+profiling
This metapackage enables feature "profiling" for the Rust tikv-jemallocator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stats
Summary:        Rust allocator backed by jemalloc - feature "stats"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tikv-jemalloc-sys-0.6/stats) >= 0.6.1
Provides:       crate(%{pkgname}/stats) = %{version}

%description -n %{name}+stats
This metapackage enables feature "stats" for the Rust tikv-jemallocator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unprefixed-malloc-on-supported-platforms
Summary:        Rust allocator backed by jemalloc - feature "unprefixed_malloc_on_supported_platforms"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tikv-jemalloc-sys-0.6/unprefixed-malloc-on-supported-platforms) >= 0.6.1
Provides:       crate(%{pkgname}/unprefixed-malloc-on-supported-platforms) = %{version}

%description -n %{name}+unprefixed-malloc-on-supported-platforms
This metapackage enables feature "unprefixed_malloc_on_supported_platforms" for the Rust tikv-jemallocator crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
