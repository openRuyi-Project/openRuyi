# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-log
%global full_version 0.2.0
%global pkgname tracing-log-0.2

Name:           rust-tracing-log-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "tracing-log"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:ee855f1f400bd0e5c02d150ae5de3840039a3f54b025156404e34c23c03f47c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(once-cell-1/default) >= 1.13.0
Requires:       crate(tracing-core-0.1/default) >= 0.1.28
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/log-tracer) = %{version}

%description
Source code for takopackized Rust crate "tracing-log"

%package     -n %{name}+ahash
Summary:        Provides compatibility between `tracing` and the `log` crate - feature "ahash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ahash-0.7/default) >= 0.7.6
Provides:       crate(%{pkgname}/ahash) = %{version}

%description -n %{name}+ahash
This metapackage enables feature "ahash" for the Rust tracing-log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Provides compatibility between `tracing` and the `log` crate - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/log-tracer) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tracing-log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+interest-cache
Summary:        Provides compatibility between `tracing` and the `log` crate - feature "interest-cache"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ahash) = %{version}
Requires:       crate(%{pkgname}/lru) = %{version}
Provides:       crate(%{pkgname}/interest-cache) = %{version}

%description -n %{name}+interest-cache
This metapackage enables feature "interest-cache" for the Rust tracing-log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lru
Summary:        Provides compatibility between `tracing` and the `log` crate - feature "lru"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lru-0.7/default) >= 0.7.7
Provides:       crate(%{pkgname}/lru) = %{version}

%description -n %{name}+lru
This metapackage enables feature "lru" for the Rust tracing-log crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Provides compatibility between `tracing` and the `log` crate - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/std) >= 0.4.17
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust tracing-log crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
