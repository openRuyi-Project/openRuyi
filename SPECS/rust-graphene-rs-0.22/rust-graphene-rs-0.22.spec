# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name graphene-rs
%global full_version 0.22.0
%global pkgname graphene-rs-0.22

Name:           rust-graphene-rs-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "graphene-rs"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:c7d1b7881f96869f49808b6adfe906a93a57a34204952253444d68c3208d71f1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glib-0.22) >= 0.22.0
Requires:       crate(graphene-sys-0.22/default) >= 0.22.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "graphene-rs"

%package     -n %{name}+v1-12
Summary:        Rust bindings for the Graphene library - feature "v1_12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(graphene-sys-0.22/v1-12) >= 0.22.0
Provides:       crate(%{pkgname}/v1-12) = %{version}

%description -n %{name}+v1-12
This metapackage enables feature "v1_12" for the Rust graphene-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
