# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parking_lot_core
%global full_version 0.6.3
%global pkgname parking-lot-core-0.6

Name:           rust-parking-lot-core-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "parking_lot_core"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/parking_lot
#!RemoteAsset:  sha256:bda66b810a62be75176a80873726630147a5ca780cd33921e0b5709033e66b0a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-0.1/default) >= 0.1.5
Requires:       crate(cloudabi-0.0.3/default) >= 0.0.3
Requires:       crate(libc-0.2/default) >= 0.2.55
Requires:       crate(redox-syscall-0.1/default) >= 0.1.0
Requires:       crate(rustc-version-0.2) >= 0.2.0
Requires:       crate(smallvec-0.6/default) >= 0.6.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/errhandlingapi) >= 0.3.0
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/minwindef) >= 0.3.0
Requires:       crate(winapi-0.3/ntstatus) >= 0.3.0
Requires:       crate(winapi-0.3/winbase) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0
Requires:       crate(winapi-0.3/winnt) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "parking_lot_core"

%package     -n %{name}+backtrace
Summary:        Advanced API for creating custom synchronization primitives - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.2
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This metapackage enables feature "backtrace" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deadlock-detection
Summary:        Advanced API for creating custom synchronization primitives - feature "deadlock_detection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backtrace) = %{version}
Requires:       crate(%{pkgname}/petgraph) = %{version}
Requires:       crate(%{pkgname}/thread-id) = %{version}
Provides:       crate(%{pkgname}/deadlock-detection) = %{version}

%description -n %{name}+deadlock-detection
This metapackage enables feature "deadlock_detection" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+petgraph
Summary:        Advanced API for creating custom synchronization primitives - feature "petgraph"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(petgraph-0.4/default) >= 0.4.5
Provides:       crate(%{pkgname}/petgraph) = %{version}

%description -n %{name}+petgraph
This metapackage enables feature "petgraph" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thread-id
Summary:        Advanced API for creating custom synchronization primitives - feature "thread-id"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(thread-id-3/default) >= 3.2.0
Provides:       crate(%{pkgname}/thread-id) = %{version}

%description -n %{name}+thread-id
This metapackage enables feature "thread-id" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
