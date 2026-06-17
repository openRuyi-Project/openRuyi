# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-lock
%global full_version 3.4.2
%global pkgname async-lock-3

Name:           rust-async-lock-3
Version:        3.4.2
Release:        %autorelease
Summary:        Rust crate "async-lock"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-lock
#!RemoteAsset:  sha256:290f7f2596bd5b78a9fec8088ccd89180d7f9f55b94b0576823bbbdc72ee8311
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(event-listener-5) >= 5.0.0
Requires:       crate(event-listener-strategy-0.5) >= 0.5.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.11
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "async-lock"

%package     -n %{name}+loom
Summary:        Async synchronization primitives - feature "loom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(event-listener-5/loom) >= 5.0.0
Requires:       crate(loom-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/loom) = %{version}

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust async-lock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Async synchronization primitives - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(event-listener-5/std) >= 5.0.0
Requires:       crate(event-listener-strategy-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust async-lock crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
