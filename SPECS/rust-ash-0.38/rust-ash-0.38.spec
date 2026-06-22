# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ash
%global full_version 0.38.0+1.3.281
%global pkgname ash-0.38

Name:           rust-ash-0.38
Version:        0.38.0
Release:        %autorelease
Summary:        Rust crate "ash"
License:        MIT OR Apache-2.0
URL:            https://github.com/ash-rs/ash
#!RemoteAsset:  sha256:0bb44936d800fea8f016d7f2311c6a4f97aebd5dc86f09906139ec848cf3a46f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/linked) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ash"

%package     -n %{name}+default
Summary:        Vulkan bindings for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/debug) = %{version}
Requires:       crate(%{pkgname}/loaded) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libloading
Summary:        Vulkan bindings for Rust - feature "libloading"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libloading-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/libloading) = %{version}

%description -n %{name}+libloading
This metapackage enables feature "libloading" for the Rust ash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loaded
Summary:        Vulkan bindings for Rust - feature "loaded"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libloading) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/loaded) = %{version}

%description -n %{name}+loaded
This metapackage enables feature "loaded" for the Rust ash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
