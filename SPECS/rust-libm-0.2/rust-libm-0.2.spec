# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libm
%global full_version 0.2.16
%global pkgname libm-0.2

Name:           rust-libm-0.2
Version:        0.2.16
Release:        %autorelease
Summary:        Rust crate "libm"
License:        MIT
URL:            https://github.com/rust-lang/compiler-builtins
#!RemoteAsset:  sha256:b6d2cec3eae94f9f509c767b45932f1ada8350c4bdb85af2fcab4a3c14807981
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/arch) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/force-soft-floats) = %{version}
Provides:       crate(%{pkgname}/unstable-float) = %{version}
Provides:       crate(%{pkgname}/unstable-intrinsics) = %{version}
Provides:       crate(%{pkgname}/unstable-public-internals) = %{version}

%description
Source code for takopackized Rust crate "libm"

%package     -n %{name}+unstable
Summary:        Libm in pure Rust - feature "unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/unstable-float) = %{version}
Requires:       crate(%{pkgname}/unstable-intrinsics) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust libm crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
