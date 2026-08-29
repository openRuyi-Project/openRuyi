# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name drm-ffi
%global full_version 0.9.1
%global pkgname drm-ffi-0.9

Name:           rust-drm-ffi-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "drm-ffi"
License:        MIT
URL:            https://github.com/Smithay/drm-rs
#!RemoteAsset:  sha256:51a91c9b32ac4e8105dec255e849e0d66e27d7c34d184364fb93e469db08f690
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(drm-sys-0.8/default) >= 0.8.0
Requires:       crate(rustix-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "drm-ffi"

%package     -n %{name}+use-bindgen
Summary:        Safe, low-level bindings to the Direct Rendering Manager API - feature "use_bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(drm-sys-0.8/use-bindgen) >= 0.8.0
Provides:       crate(%{pkgname}/use-bindgen) = %{version}

%description -n %{name}+use-bindgen
This metapackage enables feature "use_bindgen" for the Rust drm-ffi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
