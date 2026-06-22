# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name graphene-sys
%global full_version 0.22.0
%global pkgname graphene-sys-0.22

Name:           rust-graphene-sys-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "graphene-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:517f062f3fd6b7fd3e57a3f038a74b3c23ca32f51199ff028aa704609943f79c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glib-sys-0.22/default) >= 0.22.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pkg-config-0.3) >= 0.3.31
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v1-12) = %{version}

%description
Source code for takopackized Rust crate "graphene-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
