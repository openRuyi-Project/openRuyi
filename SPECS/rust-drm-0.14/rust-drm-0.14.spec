# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name drm
%global full_version 0.14.1
%global pkgname drm-0.14

Name:           rust-drm-0.14
Version:        0.14.1
Release:        %autorelease
Summary:        Rust crate "drm"
License:        MIT
URL:            https://github.com/Smithay/drm-rs
#!RemoteAsset:  sha256:80bc8c5c6c2941f70a55c15f8d9f00f9710ebda3ffda98075f996a0e6c92756f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(bytemuck-1/default) >= 1.12.0
Requires:       crate(bytemuck-1/derive) >= 1.12.0
Requires:       crate(bytemuck-1/extern-crate-alloc) >= 1.12.0
Requires:       crate(drm-ffi-0.9/default) >= 0.9.0
Requires:       crate(drm-fourcc-2/default) >= 2.2.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(rustix-0.38/default) >= 0.38.22
Requires:       crate(rustix-0.38/fs) >= 0.38.22
Requires:       crate(rustix-0.38/mm) >= 0.38.22
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "drm"

%package     -n %{name}+use-bindgen
Summary:        Safe, low-level bindings to the Direct Rendering Manager API - feature "use_bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(drm-ffi-0.9/use-bindgen) >= 0.9.0
Provides:       crate(%{pkgname}/use-bindgen) = %{version}

%description -n %{name}+use-bindgen
This metapackage enables feature "use_bindgen" for the Rust drm crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
