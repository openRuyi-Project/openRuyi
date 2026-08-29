# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name core-graphics-types
%global full_version 0.1.3
%global pkgname core-graphics-types-0.1

Name:           rust-core-graphics-types-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "core-graphics-types"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/core-foundation-rs
#!RemoteAsset:  sha256:45390e6114f68f718cc7a830514a96f903cccd70d02a8f6d9f643ac4ba45afaf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.0
Requires:       crate(core-foundation-0.9) >= 0.9.4
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "core-graphics-types"

%package     -n %{name}+link
Summary:        Bindings for some fundamental Core Graphics types - feature "link" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-foundation-0.9/link) >= 0.9.4
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/link) = %{version}

%description -n %{name}+link
This metapackage enables feature "link" for the Rust core-graphics-types crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
