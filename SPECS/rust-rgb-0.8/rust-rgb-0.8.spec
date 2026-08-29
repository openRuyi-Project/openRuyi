# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rgb
%global full_version 0.8.53
%global pkgname rgb-0.8

Name:           rust-rgb-0.8
Version:        0.8.53
Release:        %autorelease
Summary:        Rust crate "rgb"
License:        MIT
URL:            https://lib.rs/crates/rgb
#!RemoteAsset:  sha256:47b34b781b31e5d73e9fbc8689c70551fd1ade9a19e3e28cfec8580a79290cc4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/argb) = %{version}
Provides:       crate(%{pkgname}/checked-fns) = %{version}
Provides:       crate(%{pkgname}/grb) = %{version}
Provides:       crate(%{pkgname}/unstable-experimental) = %{version}

%description
Allows no-copy high-level interoperability. Also adds common convenience methods and implements standard Rust traits to make `RGB`/`RGBA` pixels and slices first-class Rust objects.
Source code for takopackized Rust crate "rgb"

%package     -n %{name}+bytemuck
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenience methods for color manipulation - feature "bytemuck" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.16.0
Provides:       crate(%{pkgname}/as-bytes) = %{version}
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
Allows no-copy high-level interoperability. Also adds common convenience methods and implements standard Rust traits to make `RGB`/`RGBA` pixels and slices first-class Rust objects.
This metapackage enables feature "bytemuck" for the Rust rgb crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "as-bytes" feature.

%package     -n %{name}+default
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenience methods for color manipulation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/argb) = %{version}
Requires:       crate(%{pkgname}/as-bytes) = %{version}
Requires:       crate(%{pkgname}/grb) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Allows no-copy high-level interoperability. Also adds common convenience methods and implements standard Rust traits to make `RGB`/`RGBA` pixels and slices first-class Rust objects.
This metapackage enables feature "default" for the Rust rgb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+defmt-03
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenience methods for color manipulation - feature "defmt-03"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-0.3/default) >= 0.3.8
Provides:       crate(%{pkgname}/defmt-03) = %{version}

%description -n %{name}+defmt-03
Allows no-copy high-level interoperability. Also adds common convenience methods and implements standard Rust traits to make `RGB`/`RGBA` pixels and slices first-class Rust objects.
This metapackage enables feature "defmt-03" for the Rust rgb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenience methods for color manipulation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.200
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Allows no-copy high-level interoperability. Also adds common convenience methods and implements standard Rust traits to make `RGB`/`RGBA` pixels and slices first-class Rust objects.
This metapackage enables feature "serde" for the Rust rgb crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
