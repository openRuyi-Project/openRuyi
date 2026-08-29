# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-worktree
%global full_version 0.42.0
%global pkgname gix-worktree-0.42

Name:           rust-gix-worktree-0.42
Version:        0.42.0
Release:        %autorelease
Summary:        Rust crate "gix-worktree"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:55f625ac9126c19bef06dbc6d2703cdd7987e21e35b497bb265ac37d383877b1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1) >= 1.12.0
Requires:       crate(gix-features-0.43/default) >= 0.43.0
Requires:       crate(gix-fs-0.16/default) >= 0.16.0
Requires:       crate(gix-glob-0.21/default) >= 0.21.0
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-ignore-0.16/default) >= 0.16.0
Requires:       crate(gix-index-0.41/default) >= 0.41.0
Requires:       crate(gix-object-0.50/default) >= 0.50.0
Requires:       crate(gix-path-0.10/default) >= 0.10.19
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "gix-worktree"

%package     -n %{name}+attributes
Summary:        The gitoxide project for shared worktree related types and utilities - feature "attributes" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-attributes-0.27/default) >= 0.27.0
Requires:       crate(gix-validate-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/attributes) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+attributes
This metapackage enables feature "attributes" for the Rust gix-worktree crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+document-features
Summary:        The gitoxide project for shared worktree related types and utilities - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-worktree crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project for shared worktree related types and utilities - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/serde) >= 1.12.0
Requires:       crate(gix-attributes-0.27/serde) >= 0.27.0
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(gix-ignore-0.16/serde) >= 0.16.0
Requires:       crate(gix-index-0.41/serde) >= 0.41.0
Requires:       crate(gix-object-0.50/serde) >= 0.50.0
Requires:       crate(serde-1/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-worktree crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
