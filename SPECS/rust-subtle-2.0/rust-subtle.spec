# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name subtle
%global full_version 2.6.1
%global pkgname subtle-2.0

Name:           rust-subtle-2.0
Version:        2.6.1
Release:        %autorelease
Summary:        Rust crate "subtle"
License:        BSD-3-Clause
URL:            https://dalek.rs/
#!RemoteAsset:  sha256:13c2bddecc57b384dee18652358fb23172facb8a2c51ccc10d74c157bdea3292
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/const-generics)
Provides:       crate(%{pkgname}/core-hint-black-box)
Provides:       crate(%{pkgname}/i128)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "subtle"

%package     -n %{name}+default
Summary:        Pure-Rust traits and utilities for constant-time cryptographic implementations - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/i128)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust subtle crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
