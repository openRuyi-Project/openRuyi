# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name relative-path
%global full_version 1.9.3
%global pkgname relative-path-1.0

Name:           rust-relative-path-1.0
Version:        1.9.3
Release:        %autorelease
Summary:        Rust crate "relative-path"
License:        MIT OR Apache-2.0
URL:            https://github.com/udoprog/relative-path
#!RemoteAsset:  sha256:ba39f3699c378cd8970968dcbff9c43159ea4cfbd88d43c00b22f2ef10a435d2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "relative-path"

%package     -n %{name}+serde
Summary:        Portable, relative paths for Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.160
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust relative-path crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
