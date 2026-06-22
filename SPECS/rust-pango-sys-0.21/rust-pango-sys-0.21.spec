# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pango-sys
%global full_version 0.21.5
%global pkgname pango-sys-0.21

Name:           rust-pango-sys-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "pango-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:b4f06627d36ed5ff303d2df65211fc2e52ba5b17bf18dd80ff3d9628d6e06cfd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glib-sys-0.21/default) >= 0.21.0
Requires:       crate(gobject-sys-0.21/default) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v1-42) = %{version}
Provides:       crate(%{pkgname}/v1-44) = %{version}
Provides:       crate(%{pkgname}/v1-46) = %{version}
Provides:       crate(%{pkgname}/v1-48) = %{version}
Provides:       crate(%{pkgname}/v1-50) = %{version}
Provides:       crate(%{pkgname}/v1-52) = %{version}
Provides:       crate(%{pkgname}/v1-54) = %{version}
Provides:       crate(%{pkgname}/v1-56) = %{version}
Provides:       crate(%{pkgname}/v1-57) = %{version}

%description
Source code for takopackized Rust crate "pango-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
