# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam-utils
%global full_version 0.8.21
%global pkgname crossbeam-utils-0.8

Name:           rust-crossbeam-utils-0.8
Version:        0.8.21
Release:        %autorelease
Summary:        Rust crate "crossbeam-utils"
License:        MIT OR Apache-2.0
URL:            https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-utils
#!RemoteAsset:  sha256:d0a5c400df2834b80a4c3327b3aad3a4c4cd4de0629063962b03235697506a28
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "crossbeam-utils"

%package     -n %{name}+loom
Summary:        Utilities for concurrent programming - feature "loom"
Requires:       crate(%{pkgname})
Requires:       crate(loom-0.7/default) >= 0.7.1
Provides:       crate(%{pkgname}/loom)

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust crossbeam-utils crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
