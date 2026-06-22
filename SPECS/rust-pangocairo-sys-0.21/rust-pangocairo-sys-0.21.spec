# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pangocairo-sys
%global full_version 0.21.5
%global pkgname pangocairo-sys-0.21

Name:           rust-pangocairo-sys-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "pangocairo-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:eadbb01ad38be76e0d37e329d40ba0f3f9ef261d7b84b05201d7a0f14f819406
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cairo-sys-rs-0.21/default) >= 0.21.1
Requires:       crate(glib-sys-0.21/default) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-sys-0.21/default) >= 0.21.0
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pangocairo-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
