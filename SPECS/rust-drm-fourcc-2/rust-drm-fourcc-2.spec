# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name drm-fourcc
%global full_version 2.2.0
%global pkgname drm-fourcc-2

Name:           rust-drm-fourcc-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "drm-fourcc"
License:        MIT
URL:            https://github.com/danielzfranklin/drm-fourcc-rs
#!RemoteAsset:  sha256:0aafbcdb8afc29c1a7ee5fbe53b5d62f4565b35a042a662ca9fecd0b54dae6f4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "drm-fourcc"

%package     -n %{name}+bindgen
Summary:        Provides an enum with every valid Direct Rendering Manager (DRM) format fourcc - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.57/default) >= 0.57.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust drm-fourcc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+build-bindings
Summary:        Provides an enum with every valid Direct Rendering Manager (DRM) format fourcc - feature "build_bindings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bindgen) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Provides:       crate(%{pkgname}/build-bindings) = %{version}

%description -n %{name}+build-bindings
This metapackage enables feature "build_bindings" for the Rust drm-fourcc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Provides an enum with every valid Direct Rendering Manager (DRM) format fourcc - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.4.3
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust drm-fourcc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Provides an enum with every valid Direct Rendering Manager (DRM) format fourcc - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.125
Requires:       crate(serde-1/derive) >= 1.0.125
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust drm-fourcc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
