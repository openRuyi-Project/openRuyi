# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-status
%global full_version 0.20.0
%global pkgname gix-status-0.20

Name:           rust-gix-status-0.20
Version:        0.20.0
Release:        %autorelease
Summary:        Rust crate "gix-status"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:2a4afff9b34eeececa8bdc32b42fb318434b6b1391d9f8d45fe455af08dc2d35
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0) >= 1.12.1
Requires:       crate(filetime-0.2/default) >= 0.2.27
Requires:       crate(gix-features-0.43/default) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Requires:       crate(gix-filter-0.20/default) >= 0.20.0
Requires:       crate(gix-fs-0.16/default) >= 0.16.1
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-index-0.41/default) >= 0.41.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-pathspec-0.12/default) >= 0.12.0
Requires:       crate(gix-worktree-0.42/attributes) >= 0.42.0
Requires:       crate(portable-atomic-1.0/default) >= 1.13.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-status"

%package     -n %{name}+document-features
Summary:        The gitoxide project dealing with 'git status'-like functionality - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-status crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+worktree-rewrites
Summary:        The gitoxide project dealing with 'git status'-like functionality - feature "worktree-rewrites"
Requires:       crate(%{pkgname})
Requires:       crate(gix-diff-0.53/blob) >= 0.53.0
Requires:       crate(gix-dir-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/worktree-rewrites)

%description -n %{name}+worktree-rewrites
This metapackage enables feature "worktree-rewrites" for the Rust gix-status crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
