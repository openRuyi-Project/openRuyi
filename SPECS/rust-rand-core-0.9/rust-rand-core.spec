# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_core
%global full_version 0.9.5
%global pkgname rand-core-0.9

Name:           rust-rand-core-0.9
Version:        0.9.5
Release:        %autorelease
Summary:        Rust crate "rand_core"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:76afc826de14238e6e8c374ddcc1fa19e374fd8dd986b0d2af0d02377261d83c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "rand_core"

%package     -n %{name}+os-rng
Summary:        Core random number generator traits and tools for implementation - feature "os_rng"
Requires:       crate(%{pkgname})
Requires:       crate(getrandom-0.3/default) >= 0.3.4
Provides:       crate(%{pkgname}/os-rng)

%description -n %{name}+os-rng
This metapackage enables feature "os_rng" for the Rust rand_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Core random number generator traits and tools for implementation - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Core random number generator traits and tools for implementation - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(getrandom-0.3/std) >= 0.3.4
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand_core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
