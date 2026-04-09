# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tinyvec
%global full_version 1.11.0
%global pkgname tinyvec-1.0

Name:           rust-tinyvec-1.0
Version:        1.11.0
Release:        %autorelease
Summary:        Rust crate "tinyvec"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/Lokathor/tinyvec
#!RemoteAsset:  sha256:3e61e67053d25a4e82c844e8424039d9745781b3fc4f32b8d55ed50f5f667ef3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/debugger-visualizer)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/experimental-write-impl)
Provides:       crate(%{pkgname}/grab-spare-slice)
Provides:       crate(%{pkgname}/latest-stable-rust)
Provides:       crate(%{pkgname}/nightly-slice-partition-dedup)
Provides:       crate(%{pkgname}/real-blackbox)
Provides:       crate(%{pkgname}/rustc-1-40)
Provides:       crate(%{pkgname}/rustc-1-55)
Provides:       crate(%{pkgname}/rustc-1-57)
Provides:       crate(%{pkgname}/rustc-1-61)

%description
Source code for takopackized Rust crate "tinyvec"

%package     -n %{name}+arbitrary
Summary:        `tinyvec` provides 100% safe vec-like data structures - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust tinyvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+borsh
Summary:        `tinyvec` provides 100% safe vec-like data structures - feature "borsh"
Requires:       crate(%{pkgname})
Requires:       crate(borsh-1.0) >= 1.2.0
Provides:       crate(%{pkgname}/borsh)

%description -n %{name}+borsh
This metapackage enables feature "borsh" for the Rust tinyvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+defmt
Summary:        `tinyvec` provides 100% safe vec-like data structures - feature "defmt"
Requires:       crate(%{pkgname})
Requires:       crate(defmt-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/defmt)

%description -n %{name}+defmt
This metapackage enables feature "defmt" for the Rust tinyvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generic-array
Summary:        `tinyvec` provides 100% safe vec-like data structures - feature "generic-array"
Requires:       crate(%{pkgname})
Requires:       crate(generic-array-1.0) >= 1.1.1
Provides:       crate(%{pkgname}/generic-array)

%description -n %{name}+generic-array
This metapackage enables feature "generic-array" for the Rust tinyvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        `tinyvec` provides 100% safe vec-like data structures - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust tinyvec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tinyvec-macros
Summary:        `tinyvec` provides 100% safe vec-like data structures - feature "tinyvec_macros" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(tinyvec-macros-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/tinyvec-macros)

%description -n %{name}+tinyvec-macros
This metapackage enables feature "tinyvec_macros" for the Rust tinyvec crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "alloc", and "std" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
