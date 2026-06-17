# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pangocairo-sys
%global full_version 0.22.0
%global pkgname pangocairo-sys-0.22

Name:           rust-pangocairo-sys-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "pangocairo-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:d95cb73468373b9e568abb1afbaf5b42fe6ab9128fc41b5f2adbf69451c3c77f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cairo-sys-rs-0.22/default) >= 0.22.0
Requires:       crate(glib-sys-0.22/default) >= 0.22.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-sys-0.22/default) >= 0.22.0
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pangocairo-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
