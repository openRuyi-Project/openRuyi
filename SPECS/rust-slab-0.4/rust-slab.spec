# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name slab
%global full_version 0.4.12
%global pkgname slab-0.4

Name:           rust-slab-0.4
Version:        0.4.12
Release:        %autorelease
Summary:        Rust crate "slab"
License:        MIT
URL:            https://github.com/tokio-rs/slab
#!RemoteAsset:  sha256:0c790de23124f9ab44544d7ac05d60440adc586479ce501c1d6d7da3cd8c9cf5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "slab"

%package     -n %{name}+serde
Summary:        Pre-allocated storage for a uniform data type - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/alloc) >= 1.0.95
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust slab crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
