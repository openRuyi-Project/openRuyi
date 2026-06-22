# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wayland-backend
%global full_version 0.3.15
%global pkgname wayland-backend-0.3

Name:           rust-wayland-backend-0.3
Version:        0.3.15
Release:        %autorelease
Summary:        Rust crate "wayland-backend"
License:        MIT
URL:            https://github.com/smithay/wayland-rs
#!RemoteAsset:  sha256:2857dd20b54e916ec7253b3d6b4d5c4d7d4ca2c33c2e11c6c76a99bd8744755d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(downcast-rs-1/default) >= 1.2.0
Requires:       crate(rustix-1/default) >= 1.0.2
Requires:       crate(rustix-1/event) >= 1.0.2
Requires:       crate(rustix-1/fs) >= 1.0.2
Requires:       crate(rustix-1/net) >= 1.0.2
Requires:       crate(rustix-1/process) >= 1.0.2
Requires:       crate(smallvec-1/const-generics) >= 1.9.0
Requires:       crate(smallvec-1/const-new) >= 1.9.0
Requires:       crate(smallvec-1/default) >= 1.9.0
Requires:       crate(smallvec-1/union) >= 1.9.0
Requires:       crate(wayland-sys-0.31/default) >= 0.31.11
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wayland-backend"

%package     -n %{name}+client-system
Summary:        Low-level bindings to the Wayland protocol - feature "client_system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(scoped-tls-1/default) >= 1.0.0
Requires:       crate(wayland-sys-0.31/client) >= 0.31.11
Provides:       crate(%{pkgname}/client-system) = %{version}

%description -n %{name}+client-system
This metapackage enables feature "client_system" for the Rust wayland-backend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dlopen
Summary:        Low-level bindings to the Wayland protocol - feature "dlopen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-sys-0.31/dlopen) >= 0.31.11
Provides:       crate(%{pkgname}/dlopen) = %{version}

%description -n %{name}+dlopen
This metapackage enables feature "dlopen" for the Rust wayland-backend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libwayland-client-1-23
Summary:        Low-level bindings to the Wayland protocol - feature "libwayland_client_1_23"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-sys-0.31/libwayland-client-1-23) >= 0.31.11
Provides:       crate(%{pkgname}/libwayland-client-1-23) = %{version}

%description -n %{name}+libwayland-client-1-23
This metapackage enables feature "libwayland_client_1_23" for the Rust wayland-backend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libwayland-server-1-22
Summary:        Low-level bindings to the Wayland protocol - feature "libwayland_server_1_22"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-sys-0.31/libwayland-server-1-22) >= 0.31.11
Provides:       crate(%{pkgname}/libwayland-server-1-22) = %{version}

%description -n %{name}+libwayland-server-1-22
This metapackage enables feature "libwayland_server_1_22" for the Rust wayland-backend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libwayland-server-1-23
Summary:        Low-level bindings to the Wayland protocol - feature "libwayland_server_1_23"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libwayland-server-1-22) = %{version}
Requires:       crate(wayland-sys-0.31/libwayland-server-1-23) >= 0.31.11
Provides:       crate(%{pkgname}/libwayland-server-1-23) = %{version}

%description -n %{name}+libwayland-server-1-23
This metapackage enables feature "libwayland_server_1_23" for the Rust wayland-backend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Low-level bindings to the Wayland protocol - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust wayland-backend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+raw-window-handle
Summary:        Low-level bindings to the Wayland protocol - feature "raw-window-handle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(raw-window-handle-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/raw-window-handle) = %{version}

%description -n %{name}+raw-window-handle
This metapackage enables feature "raw-window-handle" for the Rust wayland-backend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rwh-06
Summary:        Low-level bindings to the Wayland protocol - feature "rwh_06"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(raw-window-handle-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/rwh-06) = %{version}

%description -n %{name}+rwh-06
This metapackage enables feature "rwh_06" for the Rust wayland-backend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+server-system
Summary:        Low-level bindings to the Wayland protocol - feature "server_system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(scoped-tls-1/default) >= 1.0.0
Requires:       crate(wayland-sys-0.31/server) >= 0.31.11
Provides:       crate(%{pkgname}/server-system) = %{version}

%description -n %{name}+server-system
This metapackage enables feature "server_system" for the Rust wayland-backend crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
