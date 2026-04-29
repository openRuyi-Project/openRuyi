# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name snapbox-macros
%global full_version 0.4.0
%global pkgname snapbox-macros-0.4

Name:           rust-snapbox-macros-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "snapbox-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/snapbox/
#!RemoteAsset:  sha256:3b750c344002d7cc69afb9da00ebd9b5c0f8ac2eb7d115d9d45d5b5f47718d74
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/debug)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "snapbox-macros"

%package     -n %{name}+color
Summary:        Snapshot testing toolbox - feature "color"
Requires:       crate(%{pkgname})
Requires:       crate(anstream-0.6/default) >= 0.6.21
Provides:       crate(%{pkgname}/color)

%description -n %{name}+color
This metapackage enables feature "color" for the Rust snapbox-macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
