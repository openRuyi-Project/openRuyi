# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cairo-rs
%global full_version 0.21.5
%global pkgname cairo-rs-0.21

Name:           rust-cairo-rs-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "cairo-rs"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:b01fe135c0bd16afe262b6dea349bd5ea30e6de50708cec639aae7c5c14cc7e4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.9.0
Requires:       crate(cairo-sys-rs-0.21/default) >= 0.21.1
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "cairo-rs"

%package     -n %{name}+freetype
Summary:        Rust bindings for the Cairo library - feature "freetype"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/freetype-rs) = %{version}
Requires:       crate(cairo-sys-rs-0.21/freetype) >= 0.21.1
Provides:       crate(%{pkgname}/freetype) = %{version}

%description -n %{name}+freetype
This metapackage enables feature "freetype" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+freetype-rs
Summary:        Rust bindings for the Cairo library - feature "freetype-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(freetype-rs-0.38/default) >= 0.38.0
Provides:       crate(%{pkgname}/freetype-rs) = %{version}

%description -n %{name}+freetype-rs
This metapackage enables feature "freetype-rs" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+glib
Summary:        Rust bindings for the Cairo library - feature "glib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glib-0.21/default) >= 0.21.0
Provides:       crate(%{pkgname}/glib) = %{version}

%description -n %{name}+glib
This metapackage enables feature "glib" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pdf
Summary:        Rust bindings for the Cairo library - feature "pdf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cairo-sys-rs-0.21/pdf) >= 0.21.1
Provides:       crate(%{pkgname}/pdf) = %{version}

%description -n %{name}+pdf
This metapackage enables feature "pdf" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+png
Summary:        Rust bindings for the Cairo library - feature "png"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cairo-sys-rs-0.21/png) >= 0.21.1
Provides:       crate(%{pkgname}/png) = %{version}

%description -n %{name}+png
This metapackage enables feature "png" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ps
Summary:        Rust bindings for the Cairo library - feature "ps"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cairo-sys-rs-0.21/ps) >= 0.21.1
Provides:       crate(%{pkgname}/ps) = %{version}

%description -n %{name}+ps
This metapackage enables feature "ps" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quartz-surface
Summary:        Rust bindings for the Cairo library - feature "quartz-surface"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cairo-sys-rs-0.21/quartz-surface) >= 0.21.1
Provides:       crate(%{pkgname}/quartz-surface) = %{version}

%description -n %{name}+quartz-surface
This metapackage enables feature "quartz-surface" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+script
Summary:        Rust bindings for the Cairo library - feature "script"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cairo-sys-rs-0.21/script) >= 0.21.1
Provides:       crate(%{pkgname}/script) = %{version}

%description -n %{name}+script
This metapackage enables feature "script" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+svg
Summary:        Rust bindings for the Cairo library - feature "svg"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cairo-sys-rs-0.21/svg) >= 0.21.1
Provides:       crate(%{pkgname}/svg) = %{version}

%description -n %{name}+svg
This metapackage enables feature "svg" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-glib
Summary:        Rust bindings for the Cairo library - feature "use_glib" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/glib) = %{version}
Requires:       crate(cairo-sys-rs-0.21/use-glib) >= 0.21.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-glib) = %{version}

%description -n %{name}+use-glib
This metapackage enables feature "use_glib" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+v1-16
Summary:        Rust bindings for the Cairo library - feature "v1_16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cairo-sys-rs-0.21/v1-16) >= 0.21.1
Provides:       crate(%{pkgname}/v1-16) = %{version}

%description -n %{name}+v1-16
This metapackage enables feature "v1_16" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-18
Summary:        Rust bindings for the Cairo library - feature "v1_18"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-16) = %{version}
Requires:       crate(cairo-sys-rs-0.21/v1-18) >= 0.21.1
Provides:       crate(%{pkgname}/v1-18) = %{version}

%description -n %{name}+v1-18
This metapackage enables feature "v1_18" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+win32-surface
Summary:        Rust bindings for the Cairo library - feature "win32-surface"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cairo-sys-rs-0.21/win32-surface) >= 0.21.1
Provides:       crate(%{pkgname}/win32-surface) = %{version}

%description -n %{name}+win32-surface
This metapackage enables feature "win32-surface" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xcb
Summary:        Rust bindings for the Cairo library - feature "xcb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cairo-sys-rs-0.21/xcb) >= 0.21.1
Provides:       crate(%{pkgname}/xcb) = %{version}

%description -n %{name}+xcb
This metapackage enables feature "xcb" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xlib
Summary:        Rust bindings for the Cairo library - feature "xlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cairo-sys-rs-0.21/xlib) >= 0.21.1
Provides:       crate(%{pkgname}/xlib) = %{version}

%description -n %{name}+xlib
This metapackage enables feature "xlib" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
