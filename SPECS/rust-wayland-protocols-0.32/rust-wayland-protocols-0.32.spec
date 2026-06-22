# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wayland-protocols
%global full_version 0.32.12
%global pkgname wayland-protocols-0.32

Name:           rust-wayland-protocols-0.32
Version:        0.32.12
Release:        %autorelease
Summary:        Rust crate "wayland-protocols"
License:        MIT
URL:            https://github.com/smithay/wayland-rs
#!RemoteAsset:  sha256:563a85523cade2429938e790815fd7319062103b9f4a2dc806e9b53b95982d8f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(wayland-backend-0.3/default) >= 0.3.15
Requires:       crate(wayland-scanner-0.31/default) >= 0.31.10
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/staging) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "wayland-protocols"

%package     -n %{name}+wayland-client
Summary:        Generated API for the officials wayland protocol extensions - feature "wayland-client" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-client-0.31/default) >= 0.31.14
Provides:       crate(%{pkgname}/client) = %{version}
Provides:       crate(%{pkgname}/wayland-client) = %{version}

%description -n %{name}+wayland-client
This metapackage enables feature "wayland-client" for the Rust wayland-protocols crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "client" feature.

%package     -n %{name}+wayland-server
Summary:        Generated API for the officials wayland protocol extensions - feature "wayland-server" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-server-0.31/default) >= 0.31.13
Provides:       crate(%{pkgname}/server) = %{version}
Provides:       crate(%{pkgname}/wayland-server) = %{version}

%description -n %{name}+wayland-server
This metapackage enables feature "wayland-server" for the Rust wayland-protocols crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "server" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
