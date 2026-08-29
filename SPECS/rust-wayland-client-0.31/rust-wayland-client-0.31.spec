# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wayland-client
%global full_version 0.31.14
%global pkgname wayland-client-0.31

Name:           rust-wayland-client-0.31
Version:        0.31.14
Release:        %autorelease
Summary:        Rust crate "wayland-client"
License:        MIT
URL:            https://github.com/smithay/wayland-rs
#!RemoteAsset:  sha256:645c7c96bb74690c3189b5c9cb4ca1627062bb23693a4fad9d8c3de958260144
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(rustix-1/default) >= 1.0.2
Requires:       crate(rustix-1/event) >= 1.0.2
Requires:       crate(wayland-backend-0.3/default) >= 0.3.15
Requires:       crate(wayland-scanner-0.31/default) >= 0.31.10
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wayland-client"

%package     -n %{name}+dlopen
Summary:        Bindings to the standard C implementation of the wayland protocol, client side - feature "dlopen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-backend-0.3/dlopen) >= 0.3.15
Provides:       crate(%{pkgname}/dlopen) = %{version}

%description -n %{name}+dlopen
This metapackage enables feature "dlopen" for the Rust wayland-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libwayland-1-23
Summary:        Bindings to the standard C implementation of the wayland protocol, client side - feature "libwayland_1_23"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-backend-0.3/libwayland-client-1-23) >= 0.3.15
Provides:       crate(%{pkgname}/libwayland-1-23) = %{version}

%description -n %{name}+libwayland-1-23
This metapackage enables feature "libwayland_1_23" for the Rust wayland-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Bindings to the standard C implementation of the wayland protocol, client side - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust wayland-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system
Summary:        Bindings to the standard C implementation of the wayland protocol, client side - feature "system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-backend-0.3/client-system) >= 0.3.15
Provides:       crate(%{pkgname}/system) = %{version}

%description -n %{name}+system
This metapackage enables feature "system" for the Rust wayland-client crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
