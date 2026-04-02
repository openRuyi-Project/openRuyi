# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sharded-slab
%global full_version 0.1.7
%global pkgname sharded-slab-0.1

Name:           rust-sharded-slab-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "sharded-slab"
License:        MIT
URL:            https://github.com/hawkw/sharded-slab
#!RemoteAsset:  sha256:f40ca3c46823713e0d4209592e8d6e826aa57e928f09752619fc696c499637f6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1.0/default) >= 1.5.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "sharded-slab"

%package     -n %{name}+loom
Summary:        Lock-free concurrent slab - feature "loom"
Requires:       crate(%{pkgname})
Requires:       crate(loom-0.5/checkpoint) >= 0.5.0
Requires:       crate(loom-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/loom)

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust sharded-slab crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
