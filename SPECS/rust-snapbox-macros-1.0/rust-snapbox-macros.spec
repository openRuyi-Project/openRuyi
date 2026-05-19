# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name snapbox-macros
%global full_version 1.0.0
%global pkgname snapbox-macros-1.0

Name:           rust-snapbox-macros-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "snapbox-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/snapbox/
#!RemoteAsset:  sha256:d248cef42e1456ab2f7149c0376985351b7d849ea9ad2a957bf15ddfebf1fdf9
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
Requires:       crate(anstream-0.6/default) >= 0.6.20
Provides:       crate(%{pkgname}/color)

%description -n %{name}+color
This metapackage enables feature "color" for the Rust snapbox-macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
