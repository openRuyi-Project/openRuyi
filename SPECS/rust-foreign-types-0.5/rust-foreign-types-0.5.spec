# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name foreign-types
%global full_version 0.5.0
%global pkgname foreign-types-0.5

Name:           rust-foreign-types-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "foreign-types"
License:        MIT OR Apache-2.0
URL:            https://github.com/sfackler/foreign-types
#!RemoteAsset:  sha256:d737d9aa519fb7b749cbc3b962edcf310a8dd1f4b67c91c4f83975dbdd17d965
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(foreign-types-macros-0.2/default) >= 0.2.0
Requires:       crate(foreign-types-shared-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "foreign-types"

%package     -n %{name}+std
Summary:        Framework for Rust wrappers over C APIs - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(foreign-types-macros-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust foreign-types crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
