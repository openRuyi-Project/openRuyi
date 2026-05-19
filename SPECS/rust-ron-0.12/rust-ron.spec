# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ron
%global full_version 0.12.0
%global pkgname ron-0.12

Name:           rust-ron-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "ron"
License:        MIT OR Apache-2.0
URL:            https://github.com/ron-rs/ron
#!RemoteAsset:  sha256:fd490c5b18261893f14449cbd28cb9c0b637aebf161cd77900bfdedaff21ec32
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/serde) >= 2.11.1
Requires:       crate(once-cell-1.0/alloc) >= 1.21.3
Requires:       crate(once-cell-1.0/race) >= 1.21.3
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Requires:       crate(serde-derive-1.0) >= 1.0.228
Requires:       crate(typeid-1.0) >= 1.0.3
Requires:       crate(unicode-ident-1.0) >= 1.0.24
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/integer128)

%description
Source code for takopackized Rust crate "ron"

%package     -n %{name}+indexmap
Summary:        Rusty Object Notation - feature "indexmap"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(indexmap-2.0/serde) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap)

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust ron crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Rusty Object Notation - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Requires:       crate(serde-1.0/std) >= 1.0.228
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ron crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+unicode-segmentation
Summary:        Rusty Object Notation - feature "unicode-segmentation" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(unicode-segmentation-1.0) >= 1.12.0
Provides:       crate(%{pkgname}/internal-span-substring-test)
Provides:       crate(%{pkgname}/unicode-segmentation)

%description -n %{name}+unicode-segmentation
This metapackage enables feature "unicode-segmentation" for the Rust ron crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "internal-span-substring-test" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
