# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wayland-protocols-plasma
%global full_version 0.3.12
%global pkgname wayland-protocols-plasma-0.3

Name:           rust-wayland-protocols-plasma-0.3
Version:        0.3.12
Release:        %autorelease
Summary:        Rust crate "wayland-protocols-plasma"
License:        MIT
URL:            https://github.com/smithay/wayland-rs
#!RemoteAsset:  sha256:2b6d8cf1eb2c1c31ed1f5643c88a6e53538129d4af80030c8cabd1f9fa884d91
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(wayland-backend-0.3/default) >= 0.3.15
Requires:       crate(wayland-protocols-0.32/default) >= 0.32.12
Requires:       crate(wayland-scanner-0.31/default) >= 0.31.10
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wayland-protocols-plasma"

%package     -n %{name}+client
Summary:        Generated API for the Plasma wayland protocol extensions - feature "client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/wayland-client) = %{version}
Requires:       crate(wayland-protocols-0.32/client) >= 0.32.12
Provides:       crate(%{pkgname}/client) = %{version}

%description -n %{name}+client
This metapackage enables feature "client" for the Rust wayland-protocols-plasma crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+server
Summary:        Generated API for the Plasma wayland protocol extensions - feature "server"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/wayland-server) = %{version}
Requires:       crate(wayland-protocols-0.32/server) >= 0.32.12
Provides:       crate(%{pkgname}/server) = %{version}

%description -n %{name}+server
This metapackage enables feature "server" for the Rust wayland-protocols-plasma crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-client
Summary:        Generated API for the Plasma wayland protocol extensions - feature "wayland-client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-client-0.31/default) >= 0.31.14
Provides:       crate(%{pkgname}/wayland-client) = %{version}

%description -n %{name}+wayland-client
This metapackage enables feature "wayland-client" for the Rust wayland-protocols-plasma crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-server
Summary:        Generated API for the Plasma wayland protocol extensions - feature "wayland-server"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-server-0.31/default) >= 0.31.13
Provides:       crate(%{pkgname}/wayland-server) = %{version}

%description -n %{name}+wayland-server
This metapackage enables feature "wayland-server" for the Rust wayland-protocols-plasma crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
