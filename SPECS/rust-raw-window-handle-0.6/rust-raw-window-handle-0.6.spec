# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name raw-window-handle
%global full_version 0.6.2
%global pkgname raw-window-handle-0.6

Name:           rust-raw-window-handle-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "raw-window-handle"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/rust-windowing/raw-window-handle
#!RemoteAsset:  sha256:20675572f6f24e9e76ef639bc5552774ed45f1c30e2951e1e99c59888861c539
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "raw-window-handle"

%package     -n %{name}+wasm-bindgen
Summary:        Interoperability library for Rust Windowing applications - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-bindgen-0.2/std) >= 0.2.87
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust raw-window-handle crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen-0-2
Summary:        Interoperability library for Rust Windowing applications - feature "wasm-bindgen-0-2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/wasm-bindgen) = %{version}
Provides:       crate(%{pkgname}/wasm-bindgen-0-2) = %{version}

%description -n %{name}+wasm-bindgen-0-2
This metapackage enables feature "wasm-bindgen-0-2" for the Rust raw-window-handle crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
