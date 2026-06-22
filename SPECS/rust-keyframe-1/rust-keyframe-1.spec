# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name keyframe
%global full_version 1.1.1
%global pkgname keyframe-1

Name:           rust-keyframe-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "keyframe"
License:        MIT
URL:            https://github.com/HannesMann/keyframe
#!RemoteAsset:  sha256:60708bf7981518d09095d6f5673ce5cf6a64f1e0d9708b554f670e6d9d2bd9a9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/libm) >= 0.2.15
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "keyframe"

%package     -n %{name}+default
Summary:        Simple library for animation in Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/mint-types) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust keyframe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mint
Summary:        Simple library for animation in Rust - feature "mint" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mint-0.5/default) >= 0.5.9
Provides:       crate(%{pkgname}/mint) = %{version}
Provides:       crate(%{pkgname}/mint-types) = %{version}

%description -n %{name}+mint
This metapackage enables feature "mint" for the Rust keyframe crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "mint_types" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
