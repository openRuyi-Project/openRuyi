# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gbm
%global full_version 0.18.0
%global pkgname gbm-0.18

Name:           rust-gbm-0.18
Version:        0.18.0
Release:        %autorelease
Summary:        Rust crate "gbm"
License:        MIT
URL:            https://github.com/Smithay/gbm.rs
#!RemoteAsset:  sha256:ce852e998d3ca5e4a97014fb31c940dc5ef344ec7d364984525fd11e8a547e6a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(drm-fourcc-2/default) >= 2.2.0
Requires:       crate(gbm-sys-0.4/default) >= 0.4.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/import-egl) = %{version}

%description
Source code for takopackized Rust crate "gbm"

%package     -n %{name}+default
Summary:        Libgbm bindings for rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/drm-support) = %{version}
Requires:       crate(%{pkgname}/import-egl) = %{version}
Requires:       crate(%{pkgname}/import-wayland) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gbm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+drm
Summary:        Libgbm bindings for rust - feature "drm" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(drm-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/drm) = %{version}
Provides:       crate(%{pkgname}/drm-support) = %{version}

%description -n %{name}+drm
This metapackage enables feature "drm" for the Rust gbm crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "drm-support" feature.

%package     -n %{name}+import-wayland
Summary:        Libgbm bindings for rust - feature "import-wayland"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/wayland-backend) = %{version}
Requires:       crate(%{pkgname}/wayland-server) = %{version}
Provides:       crate(%{pkgname}/import-wayland) = %{version}

%description -n %{name}+import-wayland
This metapackage enables feature "import-wayland" for the Rust gbm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Libgbm bindings for rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/serde) >= 2.0.0
Requires:       crate(serde-1/default) >= 1.0.103
Requires:       crate(serde-1/derive) >= 1.0.103
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gbm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-bindgen
Summary:        Libgbm bindings for rust - feature "use_bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gbm-sys-0.4/use-bindgen) >= 0.4.0
Provides:       crate(%{pkgname}/use-bindgen) = %{version}

%description -n %{name}+use-bindgen
This metapackage enables feature "use_bindgen" for the Rust gbm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-backend
Summary:        Libgbm bindings for rust - feature "wayland-backend"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-backend-0.3/default) >= 0.3.0
Requires:       crate(wayland-backend-0.3/server-system) >= 0.3.0
Provides:       crate(%{pkgname}/wayland-backend) = %{version}

%description -n %{name}+wayland-backend
This metapackage enables feature "wayland-backend" for the Rust gbm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-server
Summary:        Libgbm bindings for rust - feature "wayland-server"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-server-0.31/default) >= 0.31.0
Provides:       crate(%{pkgname}/wayland-server) = %{version}

%description -n %{name}+wayland-server
This metapackage enables feature "wayland-server" for the Rust gbm crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
