# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name x11rb
%global full_version 0.13.2
%global pkgname x11rb-0.13

Name:           rust-x11rb-0.13
Version:        0.13.2
Release:        %autorelease
Summary:        Rust crate "x11rb"
License:        MIT OR Apache-2.0
URL:            https://github.com/psychon/x11rb
#!RemoteAsset:  sha256:9993aa5be5a26815fe2c3eacfc1fde061fc1a1f094bf1ad2a18bf9c495dd7414
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gethostname-1/default) >= 1.0.0
Requires:       crate(rustix-1/event) >= 1.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0
Requires:       crate(rustix-1/net) >= 1.0.0
Requires:       crate(rustix-1/std) >= 1.0.0
Requires:       crate(rustix-1/system) >= 1.0.0
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/image) = %{version}

%description
Source code for takopackized Rust crate "x11rb"

%package     -n %{name}+all-extensions
Summary:        Rust bindings to X11 - feature "all-extensions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/composite) = %{version}
Requires:       crate(%{pkgname}/damage) = %{version}
Requires:       crate(%{pkgname}/dbe) = %{version}
Requires:       crate(%{pkgname}/dpms) = %{version}
Requires:       crate(%{pkgname}/dri2) = %{version}
Requires:       crate(%{pkgname}/dri3) = %{version}
Requires:       crate(%{pkgname}/glx) = %{version}
Requires:       crate(%{pkgname}/present) = %{version}
Requires:       crate(%{pkgname}/randr) = %{version}
Requires:       crate(%{pkgname}/record) = %{version}
Requires:       crate(%{pkgname}/render) = %{version}
Requires:       crate(%{pkgname}/res) = %{version}
Requires:       crate(%{pkgname}/screensaver) = %{version}
Requires:       crate(%{pkgname}/shape) = %{version}
Requires:       crate(%{pkgname}/shm) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Requires:       crate(%{pkgname}/xevie) = %{version}
Requires:       crate(%{pkgname}/xf86dri) = %{version}
Requires:       crate(%{pkgname}/xf86vidmode) = %{version}
Requires:       crate(%{pkgname}/xfixes) = %{version}
Requires:       crate(%{pkgname}/xinerama) = %{version}
Requires:       crate(%{pkgname}/xinput) = %{version}
Requires:       crate(%{pkgname}/xkb) = %{version}
Requires:       crate(%{pkgname}/xprint) = %{version}
Requires:       crate(%{pkgname}/xselinux) = %{version}
Requires:       crate(%{pkgname}/xtest) = %{version}
Requires:       crate(%{pkgname}/xv) = %{version}
Requires:       crate(%{pkgname}/xvmc) = %{version}
Requires:       crate(x11rb-protocol-0.13/all-extensions) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/all-extensions) = %{version}

%description -n %{name}+all-extensions
This metapackage enables feature "all-extensions" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+allow-unsafe-code
Summary:        Rust bindings to X11 - feature "allow-unsafe-code"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/as-raw-xcb-connection) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Provides:       crate(%{pkgname}/allow-unsafe-code) = %{version}

%description -n %{name}+allow-unsafe-code
This metapackage enables feature "allow-unsafe-code" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+as-raw-xcb-connection
Summary:        Rust bindings to X11 - feature "as-raw-xcb-connection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(as-raw-xcb-connection-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/as-raw-xcb-connection) = %{version}

%description -n %{name}+as-raw-xcb-connection
This metapackage enables feature "as-raw-xcb-connection" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+composite
Summary:        Rust bindings to X11 - feature "composite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/xfixes) = %{version}
Requires:       crate(x11rb-protocol-0.13/composite) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/composite) = %{version}

%description -n %{name}+composite
This metapackage enables feature "composite" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cursor
Summary:        Rust bindings to X11 - feature "cursor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/render) = %{version}
Requires:       crate(%{pkgname}/resource-manager) = %{version}
Requires:       crate(%{pkgname}/xcursor) = %{version}
Provides:       crate(%{pkgname}/cursor) = %{version}

%description -n %{name}+cursor
This metapackage enables feature "cursor" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+damage
Summary:        Rust bindings to X11 - feature "damage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/xfixes) = %{version}
Requires:       crate(x11rb-protocol-0.13/damage) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/damage) = %{version}

%description -n %{name}+damage
This metapackage enables feature "damage" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dbe
Summary:        Rust bindings to X11 - feature "dbe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/dbe) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/dbe) = %{version}

%description -n %{name}+dbe
This metapackage enables feature "dbe" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dl-libxcb
Summary:        Rust bindings to X11 - feature "dl-libxcb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/allow-unsafe-code) = %{version}
Requires:       crate(%{pkgname}/libloading) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Provides:       crate(%{pkgname}/dl-libxcb) = %{version}

%description -n %{name}+dl-libxcb
This metapackage enables feature "dl-libxcb" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dpms
Summary:        Rust bindings to X11 - feature "dpms"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/dpms) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/dpms) = %{version}

%description -n %{name}+dpms
This metapackage enables feature "dpms" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dri2
Summary:        Rust bindings to X11 - feature "dri2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/dri2) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/dri2) = %{version}

%description -n %{name}+dri2
This metapackage enables feature "dri2" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dri3
Summary:        Rust bindings to X11 - feature "dri3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/dri3) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/dri3) = %{version}

%description -n %{name}+dri3
This metapackage enables feature "dri3" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extra-traits
Summary:        Rust bindings to X11 - feature "extra-traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/extra-traits) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/extra-traits) = %{version}

%description -n %{name}+extra-traits
This metapackage enables feature "extra-traits" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+glx
Summary:        Rust bindings to X11 - feature "glx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/glx) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/glx) = %{version}

%description -n %{name}+glx
This metapackage enables feature "glx" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Rust bindings to X11 - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libloading
Summary:        Rust bindings to X11 - feature "libloading"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libloading-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/libloading) = %{version}

%description -n %{name}+libloading
This metapackage enables feature "libloading" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Rust bindings to X11 - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.19.0
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+present
Summary:        Rust bindings to X11 - feature "present"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/randr) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Requires:       crate(%{pkgname}/xfixes) = %{version}
Requires:       crate(x11rb-protocol-0.13/present) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/present) = %{version}

%description -n %{name}+present
This metapackage enables feature "present" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+randr
Summary:        Rust bindings to X11 - feature "randr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/render) = %{version}
Requires:       crate(x11rb-protocol-0.13/randr) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/randr) = %{version}

%description -n %{name}+randr
This metapackage enables feature "randr" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+raw-window-handle
Summary:        Rust bindings to X11 - feature "raw-window-handle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(raw-window-handle-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/raw-window-handle) = %{version}

%description -n %{name}+raw-window-handle
This metapackage enables feature "raw-window-handle" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+record
Summary:        Rust bindings to X11 - feature "record"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/record) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/record) = %{version}

%description -n %{name}+record
This metapackage enables feature "record" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+render
Summary:        Rust bindings to X11 - feature "render"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/render) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/render) = %{version}

%description -n %{name}+render
This metapackage enables feature "render" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+request-parsing
Summary:        Rust bindings to X11 - feature "request-parsing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/request-parsing) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/request-parsing) = %{version}

%description -n %{name}+request-parsing
This metapackage enables feature "request-parsing" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+res
Summary:        Rust bindings to X11 - feature "res"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/res) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/res) = %{version}

%description -n %{name}+res
This metapackage enables feature "res" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+resource-manager
Summary:        Rust bindings to X11 - feature "resource_manager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/resource-manager) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/resource-manager) = %{version}

%description -n %{name}+resource-manager
This metapackage enables feature "resource_manager" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+screensaver
Summary:        Rust bindings to X11 - feature "screensaver"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/screensaver) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/screensaver) = %{version}

%description -n %{name}+screensaver
This metapackage enables feature "screensaver" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+shape
Summary:        Rust bindings to X11 - feature "shape"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/shape) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/shape) = %{version}

%description -n %{name}+shape
This metapackage enables feature "shape" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+shm
Summary:        Rust bindings to X11 - feature "shm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/shm) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Provides:       crate(%{pkgname}/shm) = %{version}

%description -n %{name}+shm
This metapackage enables feature "shm" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sync
Summary:        Rust bindings to X11 - feature "sync"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/sync) >= 0.13.2
Provides:       crate(%{pkgname}/sync) = %{version}

%description -n %{name}+sync
This metapackage enables feature "sync" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Rust bindings to X11 - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xcursor
Summary:        Rust bindings to X11 - feature "xcursor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(xcursor-0.3/default) >= 0.3.7
Provides:       crate(%{pkgname}/xcursor) = %{version}

%description -n %{name}+xcursor
This metapackage enables feature "xcursor" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xevie
Summary:        Rust bindings to X11 - feature "xevie"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xevie) >= 0.13.2
Provides:       crate(%{pkgname}/xevie) = %{version}

%description -n %{name}+xevie
This metapackage enables feature "xevie" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xf86dri
Summary:        Rust bindings to X11 - feature "xf86dri"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xf86dri) >= 0.13.2
Provides:       crate(%{pkgname}/xf86dri) = %{version}

%description -n %{name}+xf86dri
This metapackage enables feature "xf86dri" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xf86vidmode
Summary:        Rust bindings to X11 - feature "xf86vidmode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xf86vidmode) >= 0.13.2
Provides:       crate(%{pkgname}/xf86vidmode) = %{version}

%description -n %{name}+xf86vidmode
This metapackage enables feature "xf86vidmode" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xfixes
Summary:        Rust bindings to X11 - feature "xfixes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/render) = %{version}
Requires:       crate(%{pkgname}/shape) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xfixes) >= 0.13.2
Provides:       crate(%{pkgname}/xfixes) = %{version}

%description -n %{name}+xfixes
This metapackage enables feature "xfixes" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xinerama
Summary:        Rust bindings to X11 - feature "xinerama"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xinerama) >= 0.13.2
Provides:       crate(%{pkgname}/xinerama) = %{version}

%description -n %{name}+xinerama
This metapackage enables feature "xinerama" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xinput
Summary:        Rust bindings to X11 - feature "xinput"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/xfixes) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xinput) >= 0.13.2
Provides:       crate(%{pkgname}/xinput) = %{version}

%description -n %{name}+xinput
This metapackage enables feature "xinput" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xkb
Summary:        Rust bindings to X11 - feature "xkb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xkb) >= 0.13.2
Provides:       crate(%{pkgname}/xkb) = %{version}

%description -n %{name}+xkb
This metapackage enables feature "xkb" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xprint
Summary:        Rust bindings to X11 - feature "xprint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xprint) >= 0.13.2
Provides:       crate(%{pkgname}/xprint) = %{version}

%description -n %{name}+xprint
This metapackage enables feature "xprint" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xselinux
Summary:        Rust bindings to X11 - feature "xselinux"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xselinux) >= 0.13.2
Provides:       crate(%{pkgname}/xselinux) = %{version}

%description -n %{name}+xselinux
This metapackage enables feature "xselinux" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xtest
Summary:        Rust bindings to X11 - feature "xtest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xtest) >= 0.13.2
Provides:       crate(%{pkgname}/xtest) = %{version}

%description -n %{name}+xtest
This metapackage enables feature "xtest" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xv
Summary:        Rust bindings to X11 - feature "xv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/shm) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xv) >= 0.13.2
Provides:       crate(%{pkgname}/xv) = %{version}

%description -n %{name}+xv
This metapackage enables feature "xv" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xvmc
Summary:        Rust bindings to X11 - feature "xvmc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/xv) = %{version}
Requires:       crate(x11rb-protocol-0.13/std) >= 0.13.2
Requires:       crate(x11rb-protocol-0.13/xvmc) >= 0.13.2
Provides:       crate(%{pkgname}/xvmc) = %{version}

%description -n %{name}+xvmc
This metapackage enables feature "xvmc" for the Rust x11rb crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
