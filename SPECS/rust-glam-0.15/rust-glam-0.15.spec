# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glam
%global full_version 0.15.2
%global pkgname glam-0.15

Name:           rust-glam-0.15
Version:        0.15.2
Release:        %autorelease
Summary:        Rust crate "glam"
License:        MIT OR Apache-2.0
URL:            https://github.com/bitshifter/glam-rs
#!RemoteAsset:  sha256:3abb554f8ee44336b72d522e0a7fe86a29e09f839a36022fa869a7dfe941a54b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug-glam-assert) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/glam-assert) = %{version}
Provides:       crate(%{pkgname}/scalar-math) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/transform-types) = %{version}

%description
Source code for takopackized Rust crate "glam"

%package     -n %{name}+bytemuck
Summary:        Simple and fast 3D math library for games and graphics - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1) >= 1.5.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Simple and fast 3D math library for games and graphics - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/libm) >= 0.2.14
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mint
Summary:        Simple and fast 3D math library for games and graphics - feature "mint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mint-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/mint) = %{version}

%description -n %{name}+mint
This metapackage enables feature "mint" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-traits
Summary:        Simple and fast 3D math library for games and graphics - feature "num-traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2) >= 0.2.14
Provides:       crate(%{pkgname}/num-traits) = %{version}

%description -n %{name}+num-traits
This metapackage enables feature "num-traits" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Simple and fast 3D math library for games and graphics - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Simple and fast 3D math library for games and graphics - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spirv-std
Summary:        Simple and fast 3D math library for games and graphics - feature "spirv-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(spirv-std-0.4.0-alpha.7/default) >= 0.4.0-alpha.7
Provides:       crate(%{pkgname}/spirv-std) = %{version}

%description -n %{name}+spirv-std
This metapackage enables feature "spirv-std" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
