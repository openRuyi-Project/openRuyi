# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name btree-slab
%global full_version 0.6.1
%global pkgname btree-slab-0.6

Name:           rust-btree-slab-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "btree-slab"
License:        MIT OR Apache-2.0
URL:            https://github.com/timothee-haudebourg/btree-slab
#!RemoteAsset:  sha256:7a2b56d3029f075c4fa892428a098425b86cef5c89ae54073137ece416aef13c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-traits-2/default) >= 2.0.0
Requires:       crate(smallvec-1/default) >= 1.8.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "btree-slab"

%package     -n %{name}+std-slab
Summary:        Memory compact Slab-based B-tree implementation - feature "std-slab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-traits-2/slab) >= 2.0.0
Requires:       crate(slab-0.4/default) >= 0.4.5

Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std-slab) = %{version}

%description -n %{name}+std-slab
This metapackage enables feature "std-slab" for the Rust btree-slab crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
