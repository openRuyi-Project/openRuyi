# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wayland-sys
%global full_version 0.31.11
%global pkgname wayland-sys-0.31

Name:           rust-wayland-sys-0.31
Version:        0.31.11
Release:        %autorelease
Summary:        Rust crate "wayland-sys"
License:        MIT
URL:            https://github.com/smithay/wayland-rs
#!RemoteAsset:  sha256:d8eab23fefc9e41f8e841df4a9c707e8a8c4ed26e944ef69297184de2785e3be
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pkg-config-0.3) >= 0.3.7
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/libwayland-client-1-23) = %{version}
Provides:       crate(%{pkgname}/libwayland-server-1-22) = %{version}
Provides:       crate(%{pkgname}/libwayland-server-1-23) = %{version}

%description
You should only need this crate if you are working on custom wayland protocol extensions. Look at the crate wayland-client for usable bindings.
Source code for takopackized Rust crate "wayland-sys"

%package     -n %{name}+client
Summary:        FFI bindings to the various libwayland-*.so libraries - feature "client" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dlib-0.5/default) >= 0.5.3
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/client) = %{version}
Provides:       crate(%{pkgname}/cursor) = %{version}
Provides:       crate(%{pkgname}/egl) = %{version}

%description -n %{name}+client
You should only need this crate if you are working on custom wayland protocol extensions. Look at the crate wayland-client for usable bindings.
This metapackage enables feature "client" for the Rust wayland-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cursor", and "egl" features.

%package     -n %{name}+libc
Summary:        FFI bindings to the various libwayland-*.so libraries - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
You should only need this crate if you are working on custom wayland protocol extensions. Look at the crate wayland-client for usable bindings.
This metapackage enables feature "libc" for the Rust wayland-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memoffset
Summary:        FFI bindings to the various libwayland-*.so libraries - feature "memoffset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memoffset-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/memoffset) = %{version}

%description -n %{name}+memoffset
You should only need this crate if you are working on custom wayland protocol extensions. Look at the crate wayland-client for usable bindings.
This metapackage enables feature "memoffset" for the Rust wayland-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        FFI bindings to the various libwayland-*.so libraries - feature "once_cell" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/dlopen) = %{version}
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
You should only need this crate if you are working on custom wayland protocol extensions. Look at the crate wayland-client for usable bindings.
This metapackage enables feature "once_cell" for the Rust wayland-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dlopen" feature.

%package     -n %{name}+server
Summary:        FFI bindings to the various libwayland-*.so libraries - feature "server"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/memoffset) = %{version}
Requires:       crate(dlib-0.5/default) >= 0.5.3
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/server) = %{version}

%description -n %{name}+server
You should only need this crate if you are working on custom wayland protocol extensions. Look at the crate wayland-client for usable bindings.
This metapackage enables feature "server" for the Rust wayland-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
