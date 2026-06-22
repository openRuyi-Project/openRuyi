# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cgmath
%global full_version 0.18.0
%global pkgname cgmath-0.18

Name:           rust-cgmath-0.18
Version:        0.18.0
Release:        %autorelease
Summary:        Rust crate "cgmath"
License:        Apache-2.0
URL:            https://github.com/rustgd/cgmath
#!RemoteAsset:  sha256:1a98d30140e3296250832bbaaff83b27dcd6fa3cc70fb6f1f3e5c9c0023b5317
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(approx-0.4/default) >= 0.4.0
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/swizzle) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "cgmath"

%package     -n %{name}+mint
Summary:        Linear algebra and mathematics library for computer graphics - feature "mint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mint-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/mint) = %{version}

%description -n %{name}+mint
This metapackage enables feature "mint" for the Rust cgmath crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Linear algebra and mathematics library for computer graphics - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8/default) >= 0.8.0
Requires:       crate(rand-0.8/small-rng) >= 0.8.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust cgmath crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Linear algebra and mathematics library for computer graphics - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/serde-derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust cgmath crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
