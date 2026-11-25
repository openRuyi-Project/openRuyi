# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wg
%global full_version 1.1.0
%global pkgname wg-1

Name:           rust-wg-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "wg"
License:        MIT OR Apache-2.0
URL:            https://github.com/al8n/wg
#!RemoteAsset:  sha256:6845af35d0efb945bf9f1ad34c09e55489c82b40fbc67eabe16d26ddcceed7b5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "wg"

%package     -n %{name}+default
Summary:        Golang like WaitGroup implementation for sync/async Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/parking-lot) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/triomphe) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+event-listener
Summary:        Golang like WaitGroup implementation for sync/async Rust - feature "event-listener"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(event-listener-5/portable-atomic) >= 5.0.0
Provides:       crate(%{pkgname}/event-listener) = %{version}

%description -n %{name}+event-listener
This metapackage enables feature "event-listener" for the Rust wg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+future
Summary:        Golang like WaitGroup implementation for sync/async Rust - feature "future"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/event-listener) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Provides:       crate(%{pkgname}/future) = %{version}

%description -n %{name}+future
This metapackage enables feature "future" for the Rust wg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking-lot
Summary:        Golang like WaitGroup implementation for sync/async Rust - feature "parking_lot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/parking-lot) = %{version}

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust wg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pin-project-lite
Summary:        Golang like WaitGroup implementation for sync/async Rust - feature "pin-project-lite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/pin-project-lite) = %{version}

%description -n %{name}+pin-project-lite
This metapackage enables feature "pin-project-lite" for the Rust wg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Golang like WaitGroup implementation for sync/async Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(event-listener-5/default) >= 5.0.0
Requires:       crate(event-listener-5/portable-atomic) >= 5.0.0
Requires:       crate(triomphe-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust wg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+triomphe
Summary:        Golang like WaitGroup implementation for sync/async Rust - feature "triomphe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(triomphe-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/triomphe) = %{version}

%description -n %{name}+triomphe
This metapackage enables feature "triomphe" for the Rust wg crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
