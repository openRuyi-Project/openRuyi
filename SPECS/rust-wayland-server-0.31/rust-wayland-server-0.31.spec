# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wayland-server
%global full_version 0.31.13
%global pkgname wayland-server-0.31

Name:           rust-wayland-server-0.31
Version:        0.31.13
Release:        %autorelease
Summary:        Rust crate "wayland-server"
License:        MIT
URL:            https://github.com/smithay/wayland-rs
#!RemoteAsset:  sha256:cc1846eb04c49182e04f4a099e2a830a2b745610bbc1d61246e206f29c7000a0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(downcast-rs-1/default) >= 1.2.0
Requires:       crate(rustix-1/default) >= 1.0.2
Requires:       crate(rustix-1/fs) >= 1.0.2
Requires:       crate(wayland-backend-0.3/default) >= 0.3.15
Requires:       crate(wayland-scanner-0.31/default) >= 0.31.10
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wayland-server"

%package     -n %{name}+dlopen
Summary:        Bindings to the standard C implementation of the wayland protocol, server side - feature "dlopen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-backend-0.3/dlopen) >= 0.3.15
Provides:       crate(%{pkgname}/dlopen) = %{version}

%description -n %{name}+dlopen
This metapackage enables feature "dlopen" for the Rust wayland-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libwayland-1-22
Summary:        Bindings to the standard C implementation of the wayland protocol, server side - feature "libwayland_1_22"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-backend-0.3/libwayland-server-1-22) >= 0.3.15
Provides:       crate(%{pkgname}/libwayland-1-22) = %{version}

%description -n %{name}+libwayland-1-22
This metapackage enables feature "libwayland_1_22" for the Rust wayland-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libwayland-1-23
Summary:        Bindings to the standard C implementation of the wayland protocol, server side - feature "libwayland_1_23"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libwayland-1-22) = %{version}
Requires:       crate(wayland-backend-0.3/libwayland-server-1-23) >= 0.3.15
Provides:       crate(%{pkgname}/libwayland-1-23) = %{version}

%description -n %{name}+libwayland-1-23
This metapackage enables feature "libwayland_1_23" for the Rust wayland-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Bindings to the standard C implementation of the wayland protocol, server side - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust wayland-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system
Summary:        Bindings to the standard C implementation of the wayland protocol, server side - feature "system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-backend-0.3/server-system) >= 0.3.15
Provides:       crate(%{pkgname}/system) = %{version}

%description -n %{name}+system
This metapackage enables feature "system" for the Rust wayland-server crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
