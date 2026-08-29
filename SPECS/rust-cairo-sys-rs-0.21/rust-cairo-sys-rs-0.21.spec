# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cairo-sys-rs
%global full_version 0.21.5
%global pkgname cairo-sys-rs-0.21

Name:           rust-cairo-sys-rs-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "cairo-sys-rs"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:06c28280c6b12055b5e39e4554271ae4e6630b27c0da9148c4cf6485fc6d245c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/freetype) = %{version}
Provides:       crate(%{pkgname}/pdf) = %{version}
Provides:       crate(%{pkgname}/png) = %{version}
Provides:       crate(%{pkgname}/ps) = %{version}
Provides:       crate(%{pkgname}/quartz-surface) = %{version}
Provides:       crate(%{pkgname}/script) = %{version}
Provides:       crate(%{pkgname}/svg) = %{version}
Provides:       crate(%{pkgname}/v1-16) = %{version}
Provides:       crate(%{pkgname}/v1-18) = %{version}
Provides:       crate(%{pkgname}/xcb) = %{version}

%description
Source code for takopackized Rust crate "cairo-sys-rs"

%package     -n %{name}+glib-sys
Summary:        FFI bindings to libcairo - feature "glib-sys" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glib-sys-0.21/default) >= 0.21.0
Provides:       crate(%{pkgname}/glib-sys) = %{version}
Provides:       crate(%{pkgname}/use-glib) = %{version}

%description -n %{name}+glib-sys
This metapackage enables feature "glib-sys" for the Rust cairo-sys-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use_glib" feature.

%package     -n %{name}+windows-sys
Summary:        FFI bindings to libcairo - feature "windows-sys" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-graphics-gdi) >= 0.52.0
Provides:       crate(%{pkgname}/win32-surface) = %{version}
Provides:       crate(%{pkgname}/windows-sys) = %{version}

%description -n %{name}+windows-sys
This metapackage enables feature "windows-sys" for the Rust cairo-sys-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "win32-surface" feature.

%package     -n %{name}+x11
Summary:        FFI bindings to libcairo - feature "x11" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11-2/default) >= 2.16.0
Requires:       crate(x11-2/xlib) >= 2.16.0
Provides:       crate(%{pkgname}/x11) = %{version}
Provides:       crate(%{pkgname}/xlib) = %{version}

%description -n %{name}+x11
This metapackage enables feature "x11" for the Rust cairo-sys-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "xlib" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
