# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name snapbox-macros
%global full_version 1.1.0
%global pkgname snapbox-macros-1

Name:           rust-snapbox-macros-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "snapbox-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/snapbox/
#!RemoteAsset:  sha256:ed4a172e483585ebbc7c7f7d1705ca7e3f94f606ed78caa14805673189fd5455
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "snapbox-macros"

%package     -n %{name}+color
Summary:        Snapshot testing toolbox - feature "color"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstream-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/color) = %{version}

%description -n %{name}+color
This metapackage enables feature "color" for the Rust snapbox-macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
