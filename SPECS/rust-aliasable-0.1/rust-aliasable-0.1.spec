# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aliasable
%global full_version 0.1.3
%global pkgname aliasable-0.1

Name:           rust-aliasable-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "aliasable"
License:        MIT
URL:            https://github.com/avitex/rust-aliasable
#!RemoteAsset:  sha256:250f629c0161ad8107cf89319e990051fae62832fd343083bea452d93e2205fd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "aliasable"

%package     -n %{name}+aliasable-deref-trait
Summary:        Basic aliasable (non unique pointer) types - feature "aliasable_deref_trait"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aliasable-deref-trait-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/aliasable-deref-trait) = %{version}

%description -n %{name}+aliasable-deref-trait
This metapackage enables feature "aliasable_deref_trait" for the Rust aliasable crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stable-deref-trait
Summary:        Basic aliasable (non unique pointer) types - feature "stable_deref_trait"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(stable-deref-trait-1/default) >= 1.2.0
Provides:       crate(%{pkgname}/stable-deref-trait) = %{version}

%description -n %{name}+stable-deref-trait
This metapackage enables feature "stable_deref_trait" for the Rust aliasable crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+traits
Summary:        Basic aliasable (non unique pointer) types - feature "traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aliasable-deref-trait) = %{version}
Requires:       crate(%{pkgname}/stable-deref-trait) = %{version}
Provides:       crate(%{pkgname}/traits) = %{version}

%description -n %{name}+traits
This metapackage enables feature "traits" for the Rust aliasable crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
