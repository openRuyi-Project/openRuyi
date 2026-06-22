# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name graphene-rs
%global full_version 0.21.5
%global pkgname graphene-rs-0.21

Name:           rust-graphene-rs-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "graphene-rs"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:2730030ac9db663fd8bfe1e7093742c1cafb92db9c315c9417c29032341fe2f9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glib-0.21/default) >= 0.21.0
Requires:       crate(graphene-sys-0.21/default) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "graphene-rs"

%package     -n %{name}+v1-12
Summary:        Rust bindings for the Graphene library - feature "v1_12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(graphene-sys-0.21/v1-12) >= 0.21.0
Provides:       crate(%{pkgname}/v1-12) = %{version}

%description -n %{name}+v1-12
This metapackage enables feature "v1_12" for the Rust graphene-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
