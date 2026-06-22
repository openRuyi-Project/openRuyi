# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smithay
%global full_version 0.7.0
%global pkgname smithay-0.7

Name:           rust-smithay-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "smithay"
License:        MIT
URL:            https://smithay.github.io/
#!RemoteAsset:  sha256:740cea6927892bc182d5bf70c8f79806c8bc9f68f2fb96e55a30be171b63af98
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(appendlist-1/default) >= 1.4.0
Requires:       crate(atomic-float-1/default) >= 1.1.0
Requires:       crate(bitflags-2/default) >= 2.2.1
Requires:       crate(calloop-0.14/default) >= 0.14.0
Requires:       crate(cgmath-0.18/default) >= 0.18.0
Requires:       crate(cursor-icon-1/default) >= 1.2.0
Requires:       crate(downcast-rs-1/default) >= 1.2.0
Requires:       crate(drm-fourcc-2/default) >= 2.2.0
Requires:       crate(errno-0.3/default) >= 0.3.5
Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(libc-0.2/default) >= 0.2.103
Requires:       crate(profiling-1/default) >= 1.0.13
Requires:       crate(rand-0.9/default) >= 0.9.0
Requires:       crate(rustix-1/default) >= 1.0.7
Requires:       crate(rustix-1/event) >= 1.0.7
Requires:       crate(rustix-1/fs) >= 1.0.7
Requires:       crate(rustix-1/mm) >= 1.0.7
Requires:       crate(rustix-1/net) >= 1.0.7
Requires:       crate(rustix-1/pipe) >= 1.0.7
Requires:       crate(rustix-1/process) >= 1.0.7
Requires:       crate(rustix-1/shm) >= 1.0.7
Requires:       crate(rustix-1/time) >= 1.0.7
Requires:       crate(sha2-0.10/default) >= 0.10.9
Requires:       crate(smallvec-1/default) >= 1.11.0
Requires:       crate(thiserror-2/default) >= 2.0.12
Requires:       crate(tracing-0.1/default) >= 0.1.37
Requires:       crate(xkbcommon-0.8/default) >= 0.8.0
Requires:       crate(xkbcommon-0.8/wayland) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/backend-gbm-has-create-with-modifiers2) = %{version}
Provides:       crate(%{pkgname}/backend-gbm-has-fd-for-plane) = %{version}
Provides:       crate(%{pkgname}/backend-session) = %{version}
Provides:       crate(%{pkgname}/desktop) = %{version}
Provides:       crate(%{pkgname}/renderer-test) = %{version}

%description
Source code for takopackized Rust crate "smithay"

%package     -n %{name}+aliasable
Summary:        Writing wayland compositors - feature "aliasable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aliasable-0.1/default) >= 0.1.3
Provides:       crate(%{pkgname}/aliasable) = %{version}

%description -n %{name}+aliasable
This metapackage enables feature "aliasable" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ash
Summary:        Writing wayland compositors - feature "ash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ash-0.38/default) >= 0.38.0
Provides:       crate(%{pkgname}/ash) = %{version}

%description -n %{name}+ash
This metapackage enables feature "ash" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backend-drm
Summary:        Writing wayland compositors - feature "backend_drm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/drm) = %{version}
Requires:       crate(%{pkgname}/drm-ffi) = %{version}
Provides:       crate(%{pkgname}/backend-drm) = %{version}

%description -n %{name}+backend-drm
This metapackage enables feature "backend_drm" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backend-egl
Summary:        Writing wayland compositors - feature "backend_egl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gl-generator) = %{version}
Requires:       crate(%{pkgname}/libloading) = %{version}
Provides:       crate(%{pkgname}/backend-egl) = %{version}

%description -n %{name}+backend-egl
This metapackage enables feature "backend_egl" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backend-gbm
Summary:        Writing wayland compositors - feature "backend_gbm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backend-drm) = %{version}
Requires:       crate(%{pkgname}/cc) = %{version}
Requires:       crate(%{pkgname}/gbm) = %{version}
Requires:       crate(%{pkgname}/pkg-config) = %{version}
Provides:       crate(%{pkgname}/backend-gbm) = %{version}

%description -n %{name}+backend-gbm
This metapackage enables feature "backend_gbm" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backend-session-libseat
Summary:        Writing wayland compositors - feature "backend_session_libseat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backend-session) = %{version}
Requires:       crate(%{pkgname}/libseat) = %{version}
Provides:       crate(%{pkgname}/backend-session-libseat) = %{version}

%description -n %{name}+backend-session-libseat
This metapackage enables feature "backend_session_libseat" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backend-udev
Summary:        Writing wayland compositors - feature "backend_udev"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/udev) = %{version}
Requires:       crate(input-0.9/libinput-1-19) >= 0.9.0
Requires:       crate(input-0.9/udev) >= 0.9.0
Provides:       crate(%{pkgname}/backend-udev) = %{version}

%description -n %{name}+backend-udev
This metapackage enables feature "backend_udev" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backend-vulkan
Summary:        Writing wayland compositors - feature "backend_vulkan"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ash) = %{version}
Requires:       crate(%{pkgname}/scopeguard) = %{version}
Provides:       crate(%{pkgname}/backend-vulkan) = %{version}

%description -n %{name}+backend-vulkan
This metapackage enables feature "backend_vulkan" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backend-winit
Summary:        Writing wayland compositors - feature "backend_winit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backend-egl) = %{version}
Requires:       crate(%{pkgname}/renderer-gl) = %{version}
Requires:       crate(%{pkgname}/wayland-client) = %{version}
Requires:       crate(%{pkgname}/wayland-cursor) = %{version}
Requires:       crate(%{pkgname}/wayland-egl) = %{version}
Requires:       crate(%{pkgname}/winit) = %{version}
Provides:       crate(%{pkgname}/backend-winit) = %{version}

%description -n %{name}+backend-winit
This metapackage enables feature "backend_winit" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backend-x11
Summary:        Writing wayland compositors - feature "backend_x11"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backend-drm) = %{version}
Requires:       crate(%{pkgname}/backend-egl) = %{version}
Requires:       crate(%{pkgname}/backend-gbm) = %{version}
Requires:       crate(%{pkgname}/x11rb) = %{version}
Requires:       crate(%{pkgname}/x11rb-event-source) = %{version}
Requires:       crate(x11rb-0.13/dri3) >= 0.13.0
Requires:       crate(x11rb-0.13/present) >= 0.13.0
Requires:       crate(x11rb-0.13/res) >= 0.13.0
Requires:       crate(x11rb-0.13/xfixes) >= 0.13.0
Requires:       crate(x11rb-0.13/xinput) >= 0.13.0
Provides:       crate(%{pkgname}/backend-x11) = %{version}

%description -n %{name}+backend-x11
This metapackage enables feature "backend_x11" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cc
Summary:        Writing wayland compositors - feature "cc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-1/default) >= 1.0.79
Provides:       crate(%{pkgname}/cc) = %{version}

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Writing wayland compositors - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backend-drm) = %{version}
Requires:       crate(%{pkgname}/backend-gbm) = %{version}
Requires:       crate(%{pkgname}/backend-libinput) = %{version}
Requires:       crate(%{pkgname}/backend-session-libseat) = %{version}
Requires:       crate(%{pkgname}/backend-udev) = %{version}
Requires:       crate(%{pkgname}/backend-vulkan) = %{version}
Requires:       crate(%{pkgname}/backend-winit) = %{version}
Requires:       crate(%{pkgname}/backend-x11) = %{version}
Requires:       crate(%{pkgname}/desktop) = %{version}
Requires:       crate(%{pkgname}/renderer-gl) = %{version}
Requires:       crate(%{pkgname}/renderer-multi) = %{version}
Requires:       crate(%{pkgname}/renderer-pixman) = %{version}
Requires:       crate(%{pkgname}/wayland-frontend) = %{version}
Requires:       crate(%{pkgname}/xwayland) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+drm
Summary:        Writing wayland compositors - feature "drm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(drm-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/drm) = %{version}

%description -n %{name}+drm
This metapackage enables feature "drm" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+drm-ffi
Summary:        Writing wayland compositors - feature "drm-ffi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(drm-ffi-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/drm-ffi) = %{version}

%description -n %{name}+drm-ffi
This metapackage enables feature "drm-ffi" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encoding-rs
Summary:        Writing wayland compositors - feature "encoding_rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encoding-rs-0.8/default) >= 0.8.33
Provides:       crate(%{pkgname}/encoding-rs) = %{version}

%description -n %{name}+encoding-rs
This metapackage enables feature "encoding_rs" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gbm
Summary:        Writing wayland compositors - feature "gbm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gbm-0.18/drm-support) >= 0.18.0
Provides:       crate(%{pkgname}/gbm) = %{version}

%description -n %{name}+gbm
This metapackage enables feature "gbm" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gl-generator
Summary:        Writing wayland compositors - feature "gl_generator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gl-generator-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/gl-generator) = %{version}

%description -n %{name}+gl-generator
This metapackage enables feature "gl_generator" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+glow
Summary:        Writing wayland compositors - feature "glow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glow-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}/glow) = %{version}

%description -n %{name}+glow
This metapackage enables feature "glow" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+input
Summary:        Writing wayland compositors - feature "input" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(input-0.9/libinput-1-19) >= 0.9.0
Provides:       crate(%{pkgname}/backend-libinput) = %{version}
Provides:       crate(%{pkgname}/input) = %{version}

%description -n %{name}+input
This metapackage enables feature "input" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "backend_libinput" feature.

%package     -n %{name}+libloading
Summary:        Writing wayland compositors - feature "libloading"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libloading-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/libloading) = %{version}

%description -n %{name}+libloading
This metapackage enables feature "libloading" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libseat
Summary:        Writing wayland compositors - feature "libseat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libseat-0.2) >= 0.2.3
Provides:       crate(%{pkgname}/libseat) = %{version}

%description -n %{name}+libseat
This metapackage enables feature "libseat" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pixman
Summary:        Writing wayland compositors - feature "pixman" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pixman-0.2/default) >= 0.2.1
Requires:       crate(pixman-0.2/drm-fourcc) >= 0.2.1
Requires:       crate(pixman-0.2/sync) >= 0.2.1
Provides:       crate(%{pkgname}/pixman) = %{version}
Provides:       crate(%{pkgname}/renderer-pixman) = %{version}

%description -n %{name}+pixman
This metapackage enables feature "pixman" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "renderer_pixman" feature.

%package     -n %{name}+pkg-config
Summary:        Writing wayland compositors - feature "pkg-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkg-config-0.3/default) >= 0.3.17
Provides:       crate(%{pkgname}/pkg-config) = %{version}

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+renderer-gl
Summary:        Writing wayland compositors - feature "renderer_gl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backend-egl) = %{version}
Requires:       crate(%{pkgname}/gl-generator) = %{version}
Provides:       crate(%{pkgname}/renderer-gl) = %{version}

%description -n %{name}+renderer-gl
This metapackage enables feature "renderer_gl" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+renderer-glow
Summary:        Writing wayland compositors - feature "renderer_glow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/glow) = %{version}
Requires:       crate(%{pkgname}/renderer-gl) = %{version}
Provides:       crate(%{pkgname}/renderer-glow) = %{version}

%description -n %{name}+renderer-glow
This metapackage enables feature "renderer_glow" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+renderer-multi
Summary:        Writing wayland compositors - feature "renderer_multi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aliasable) = %{version}
Requires:       crate(%{pkgname}/backend-drm) = %{version}
Provides:       crate(%{pkgname}/renderer-multi) = %{version}

%description -n %{name}+renderer-multi
This metapackage enables feature "renderer_multi" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scopeguard
Summary:        Writing wayland compositors - feature "scopeguard"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(scopeguard-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/scopeguard) = %{version}

%description -n %{name}+scopeguard
This metapackage enables feature "scopeguard" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tempfile
Summary:        Writing wayland compositors - feature "tempfile"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tempfile-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/tempfile) = %{version}

%description -n %{name}+tempfile
This metapackage enables feature "tempfile" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-all-features
Summary:        Writing wayland compositors - feature "test_all_features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/default) = %{version}
Requires:       crate(%{pkgname}/renderer-glow) = %{version}
Requires:       crate(%{pkgname}/renderer-test) = %{version}
Requires:       crate(%{pkgname}/use-system-lib) = %{version}
Provides:       crate(%{pkgname}/test-all-features) = %{version}

%description -n %{name}+test-all-features
This metapackage enables feature "test_all_features" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+udev
Summary:        Writing wayland compositors - feature "udev"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(udev-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/udev) = %{version}

%description -n %{name}+udev
This metapackage enables feature "udev" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-bindgen
Summary:        Writing wayland compositors - feature "use_bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(drm-ffi-0.9/use-bindgen) >= 0.9.0
Requires:       crate(gbm-0.18/drm-support) >= 0.18.0
Requires:       crate(gbm-0.18/use-bindgen) >= 0.18.0
Requires:       crate(input-0.9/libinput-1-19) >= 0.9.0
Requires:       crate(input-0.9/use-bindgen) >= 0.9.0
Provides:       crate(%{pkgname}/use-bindgen) = %{version}

%description -n %{name}+use-bindgen
This metapackage enables feature "use_bindgen" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-system-lib
Summary:        Writing wayland compositors - feature "use_system_lib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/wayland-frontend) = %{version}
Requires:       crate(%{pkgname}/wayland-sys) = %{version}
Requires:       crate(gbm-0.18/drm-support) >= 0.18.0
Requires:       crate(gbm-0.18/import-wayland) >= 0.18.0
Requires:       crate(wayland-backend-0.3/server-system) >= 0.3.10
Provides:       crate(%{pkgname}/use-system-lib) = %{version}

%description -n %{name}+use-system-lib
This metapackage enables feature "use_system_lib" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-backend
Summary:        Writing wayland compositors - feature "wayland-backend"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-backend-0.3/default) >= 0.3.10
Provides:       crate(%{pkgname}/wayland-backend) = %{version}

%description -n %{name}+wayland-backend
This metapackage enables feature "wayland-backend" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-client
Summary:        Writing wayland compositors - feature "wayland-client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-client-0.31/default) >= 0.31.10
Provides:       crate(%{pkgname}/wayland-client) = %{version}

%description -n %{name}+wayland-client
This metapackage enables feature "wayland-client" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-cursor
Summary:        Writing wayland compositors - feature "wayland-cursor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-cursor-0.31/default) >= 0.31.10
Provides:       crate(%{pkgname}/wayland-cursor) = %{version}

%description -n %{name}+wayland-cursor
This metapackage enables feature "wayland-cursor" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-egl
Summary:        Writing wayland compositors - feature "wayland-egl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-egl-0.32/default) >= 0.32.7
Provides:       crate(%{pkgname}/wayland-egl) = %{version}

%description -n %{name}+wayland-egl
This metapackage enables feature "wayland-egl" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-protocols
Summary:        Writing wayland compositors - feature "wayland-protocols"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-protocols-0.32/default) >= 0.32.8
Requires:       crate(wayland-protocols-0.32/server) >= 0.32.8
Requires:       crate(wayland-protocols-0.32/staging) >= 0.32.8
Requires:       crate(wayland-protocols-0.32/unstable) >= 0.32.8
Provides:       crate(%{pkgname}/wayland-protocols) = %{version}

%description -n %{name}+wayland-protocols
This metapackage enables feature "wayland-protocols" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-protocols-misc
Summary:        Writing wayland compositors - feature "wayland-protocols-misc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-protocols-misc-0.3/default) >= 0.3.8
Requires:       crate(wayland-protocols-misc-0.3/server) >= 0.3.8
Provides:       crate(%{pkgname}/wayland-protocols-misc) = %{version}

%description -n %{name}+wayland-protocols-misc
This metapackage enables feature "wayland-protocols-misc" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-protocols-wlr
Summary:        Writing wayland compositors - feature "wayland-protocols-wlr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-protocols-wlr-0.3/default) >= 0.3.8
Requires:       crate(wayland-protocols-wlr-0.3/server) >= 0.3.8
Provides:       crate(%{pkgname}/wayland-protocols-wlr) = %{version}

%description -n %{name}+wayland-protocols-wlr
This metapackage enables feature "wayland-protocols-wlr" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-server
Summary:        Writing wayland compositors - feature "wayland-server"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-server-0.31/default) >= 0.31.9
Provides:       crate(%{pkgname}/wayland-server) = %{version}

%description -n %{name}+wayland-server
This metapackage enables feature "wayland-server" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-sys
Summary:        Writing wayland compositors - feature "wayland-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-sys-0.31/default) >= 0.31.6
Provides:       crate(%{pkgname}/wayland-sys) = %{version}

%description -n %{name}+wayland-sys
This metapackage enables feature "wayland-sys" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-frontend
Summary:        Writing wayland compositors - feature "wayland_frontend"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tempfile) = %{version}
Requires:       crate(%{pkgname}/wayland-protocols) = %{version}
Requires:       crate(%{pkgname}/wayland-protocols-misc) = %{version}
Requires:       crate(%{pkgname}/wayland-protocols-wlr) = %{version}
Requires:       crate(%{pkgname}/wayland-server) = %{version}
Provides:       crate(%{pkgname}/wayland-frontend) = %{version}

%description -n %{name}+wayland-frontend
This metapackage enables feature "wayland_frontend" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+winit
Summary:        Writing wayland compositors - feature "winit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(winit-0.30/rwh-06) >= 0.30.0
Requires:       crate(winit-0.30/wayland) >= 0.30.0
Requires:       crate(winit-0.30/wayland-dlopen) >= 0.30.0
Requires:       crate(winit-0.30/x11) >= 0.30.0
Provides:       crate(%{pkgname}/winit) = %{version}

%description -n %{name}+winit
This metapackage enables feature "winit" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+x11rb
Summary:        Writing wayland compositors - feature "x11rb" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-0.13/default) >= 0.13.0
Requires:       crate(x11rb-0.13/res) >= 0.13.0
Provides:       crate(%{pkgname}/x11rb) = %{version}
Provides:       crate(%{pkgname}/x11rb-event-source) = %{version}

%description -n %{name}+x11rb
This metapackage enables feature "x11rb" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "x11rb_event_source" feature.

%package     -n %{name}+xwayland
Summary:        Writing wayland compositors - feature "xwayland"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/encoding-rs) = %{version}
Requires:       crate(%{pkgname}/scopeguard) = %{version}
Requires:       crate(%{pkgname}/wayland-frontend) = %{version}
Requires:       crate(%{pkgname}/x11rb-event-source) = %{version}
Requires:       crate(x11rb-0.13/composite) >= 0.13.0
Requires:       crate(x11rb-0.13/randr) >= 0.13.0
Requires:       crate(x11rb-0.13/res) >= 0.13.0
Requires:       crate(x11rb-0.13/xfixes) >= 0.13.0
Provides:       crate(%{pkgname}/xwayland) = %{version}

%description -n %{name}+xwayland
This metapackage enables feature "xwayland" for the Rust smithay crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
