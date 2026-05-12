# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cfg-if
%global full_version 1.0.4
%global pkgname cfg-if-1.0

Name:           rust-cfg-if-1.0
Version:        1.0.4
Release:        %autorelease
Summary:        Rust crate "cfg-if"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cfg-if
#!RemoteAsset:  sha256:9330f8b2ff13f34540b44e946ef35111825727b38d33286ef986142615121801
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Structured like an if-else chain, the first matching branch is the item that gets emitted.
Source code for takopackized Rust crate "cfg-if"

%package     -n %{name}+core
Summary:        Macro to ergonomically define an item depending on a large number of #[cfg] parameters - feature "core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+core
Structured like an if-else chain, the first matching branch is the item that gets emitted.
This metapackage enables feature "core" for the Rust cfg-if crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustc-dep-of-std" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
