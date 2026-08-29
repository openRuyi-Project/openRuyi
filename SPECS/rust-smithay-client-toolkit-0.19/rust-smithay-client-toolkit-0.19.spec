# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smithay-client-toolkit
%global full_version 0.19.2
%global pkgname smithay-client-toolkit-0.19

Name:           rust-smithay-client-toolkit-0.19
Version:        0.19.2
Release:        %autorelease
Summary:        Rust crate "smithay-client-toolkit"
License:        MIT
URL:            https://github.com/smithay/client-toolkit
#!RemoteAsset:  sha256:3457dea1f0eb631b4034d61d4d8c32074caa6cd1ab2d59f2327bd8461e2c0016
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.0
Requires:       crate(cursor-icon-1/default) >= 1.1.0
Requires:       crate(libc-0.2/default) >= 0.2.148
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(memmap2-0.9/default) >= 0.9.0
Requires:       crate(rustix-0.38/default) >= 0.38.15
Requires:       crate(rustix-0.38/fs) >= 0.38.15
Requires:       crate(rustix-0.38/pipe) >= 0.38.15
Requires:       crate(rustix-0.38/shm) >= 0.38.15
Requires:       crate(thiserror-1/default) >= 1.0.30
Requires:       crate(wayland-backend-0.3/default) >= 0.3.0
Requires:       crate(wayland-client-0.31/default) >= 0.31.1
Requires:       crate(wayland-csd-frame-0.3/default) >= 0.3.0
Requires:       crate(wayland-cursor-0.31/default) >= 0.31.0
Requires:       crate(wayland-protocols-0.32/client) >= 0.32.1
Requires:       crate(wayland-protocols-0.32/default) >= 0.32.1
Requires:       crate(wayland-protocols-0.32/staging) >= 0.32.1
Requires:       crate(wayland-protocols-0.32/unstable) >= 0.32.1
Requires:       crate(wayland-protocols-wlr-0.3/client) >= 0.3.1
Requires:       crate(wayland-protocols-wlr-0.3/default) >= 0.3.1
Requires:       crate(wayland-scanner-0.31/default) >= 0.31.0
Requires:       crate(xkeysym-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "smithay-client-toolkit"

%package     -n %{name}+bytemuck
Summary:        Toolkit for making client wayland applications - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.13.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust smithay-client-toolkit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+calloop
Summary:        Toolkit for making client wayland applications - feature "calloop"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/calloop-wayland-source) = %{version}
Requires:       crate(calloop-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/calloop) = %{version}

%description -n %{name}+calloop
This metapackage enables feature "calloop" for the Rust smithay-client-toolkit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+calloop-wayland-source
Summary:        Toolkit for making client wayland applications - feature "calloop-wayland-source"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(calloop-wayland-source-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/calloop-wayland-source) = %{version}

%description -n %{name}+calloop-wayland-source
This metapackage enables feature "calloop-wayland-source" for the Rust smithay-client-toolkit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Toolkit for making client wayland applications - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/calloop) = %{version}
Requires:       crate(%{pkgname}/xkbcommon) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust smithay-client-toolkit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkg-config
Summary:        Toolkit for making client wayland applications - feature "pkg-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkg-config-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/pkg-config) = %{version}

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust smithay-client-toolkit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xkbcommon
Summary:        Toolkit for making client wayland applications - feature "xkbcommon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytemuck) = %{version}
Requires:       crate(%{pkgname}/pkg-config) = %{version}
Requires:       crate(xkbcommon-0.7/default) >= 0.7.0
Requires:       crate(xkbcommon-0.7/wayland) >= 0.7.0
Requires:       crate(xkeysym-0.2/bytemuck) >= 0.2.0
Provides:       crate(%{pkgname}/xkbcommon) = %{version}

%description -n %{name}+xkbcommon
This metapackage enables feature "xkbcommon" for the Rust smithay-client-toolkit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
