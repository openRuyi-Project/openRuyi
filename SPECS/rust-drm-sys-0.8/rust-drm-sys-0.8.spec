# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name drm-sys
%global full_version 0.8.1
%global pkgname drm-sys-0.8

Name:           rust-drm-sys-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "drm-sys"
License:        MIT
URL:            https://github.com/Smithay/drm-rs
#!RemoteAsset:  sha256:ecc8e1361066d91f5ffccff060a3c3be9c3ecde15be2959c1937595f7a82a9f8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(linux-raw-sys-0.9/general) >= 0.9.0
Requires:       crate(linux-raw-sys-0.9/no-std) >= 0.9.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "drm-sys"

%package     -n %{name}+bindgen
Summary:        Bindings to the Direct Rendering Manager API - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.70/default) >= 0.70.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust drm-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkg-config
Summary:        Bindings to the Direct Rendering Manager API - feature "pkg-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkg-config-0.3/default) >= 0.3.19
Provides:       crate(%{pkgname}/pkg-config) = %{version}

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust drm-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-bindgen
Summary:        Bindings to the Direct Rendering Manager API - feature "use_bindgen" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bindgen) = %{version}
Requires:       crate(%{pkgname}/pkg-config) = %{version}
Provides:       crate(%{pkgname}/update-bindings) = %{version}
Provides:       crate(%{pkgname}/use-bindgen) = %{version}

%description -n %{name}+use-bindgen
This metapackage enables feature "use_bindgen" for the Rust drm-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "update_bindings" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
