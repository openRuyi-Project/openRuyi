# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xkbcommon
%global full_version 0.8.0
%global pkgname xkbcommon-0.8

Name:           rust-xkbcommon-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "xkbcommon"
License:        MIT
URL:            https://github.com/rust-x-bindings/xkbcommon-rs
#!RemoteAsset:  sha256:8d66ca9352cbd4eecbbc40871d8a11b4ac8107cfc528a6e14d7c19c69d0e1ac9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.148
Requires:       crate(xkeysym-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "xkbcommon"

%package     -n %{name}+as-raw-xcb-connection
Summary:        Rust bindings and wrappers for libxkbcommon - feature "as-raw-xcb-connection" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(as-raw-xcb-connection-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/as-raw-xcb-connection) = %{version}
Provides:       crate(%{pkgname}/x11) = %{version}

%description -n %{name}+as-raw-xcb-connection
This metapackage enables feature "as-raw-xcb-connection" for the Rust xkbcommon crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "x11" feature.

%package     -n %{name}+memmap2
Summary:        Rust bindings and wrappers for libxkbcommon - feature "memmap2" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memmap2-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/memmap2) = %{version}
Provides:       crate(%{pkgname}/wayland) = %{version}

%description -n %{name}+memmap2
This metapackage enables feature "memmap2" for the Rust xkbcommon crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "wayland" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
