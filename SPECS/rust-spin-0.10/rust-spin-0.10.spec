# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name spin
%global full_version 0.10.0
%global pkgname spin-0.10

Name:           rust-spin-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "spin"
License:        MIT
URL:            https://github.com/mvdnes/spin-rs.git
#!RemoteAsset:  sha256:d5fe4ccb98d9c292d56fec89a5e07da7fc4cf0dc11e156b41793132775d3e591
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/barrier) = %{version}
Provides:       crate(%{pkgname}/fair-mutex) = %{version}
Provides:       crate(%{pkgname}/lazy) = %{version}
Provides:       crate(%{pkgname}/mutex) = %{version}
Provides:       crate(%{pkgname}/once) = %{version}
Provides:       crate(%{pkgname}/rwlock) = %{version}
Provides:       crate(%{pkgname}/spin-mutex) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/ticket-mutex) = %{version}

%description
Source code for takopackized Rust crate "spin"

%package     -n %{name}+default
Summary:        Spin-based synchronization primitives - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/barrier) = %{version}
Requires:       crate(%{pkgname}/lazy) = %{version}
Requires:       crate(%{pkgname}/lock-api) = %{version}
Requires:       crate(%{pkgname}/mutex) = %{version}
Requires:       crate(%{pkgname}/once) = %{version}
Requires:       crate(%{pkgname}/rwlock) = %{version}
Requires:       crate(%{pkgname}/spin-mutex) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust spin crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lock-api
Summary:        Spin-based synchronization primitives - feature "lock_api"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lock-api-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/lock-api) = %{version}

%description -n %{name}+lock-api
This metapackage enables feature "lock_api" for the Rust spin crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Spin-based synchronization primitives - feature "portable_atomic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-1/require-cas) >= 1.3.0
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
This metapackage enables feature "portable_atomic" for the Rust spin crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-ticket-mutex
Summary:        Spin-based synchronization primitives - feature "use_ticket_mutex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mutex) = %{version}
Requires:       crate(%{pkgname}/ticket-mutex) = %{version}
Provides:       crate(%{pkgname}/use-ticket-mutex) = %{version}

%description -n %{name}+use-ticket-mutex
This metapackage enables feature "use_ticket_mutex" for the Rust spin crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
