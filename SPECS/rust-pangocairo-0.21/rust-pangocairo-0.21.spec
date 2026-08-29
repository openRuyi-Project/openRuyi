# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pangocairo
%global full_version 0.21.5
%global pkgname pangocairo-0.21

Name:           rust-pangocairo-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "pangocairo"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:b36c5c84304072939d860595d9bda2a797d3bd6f7215e20b8ccd0e72d84da8c8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cairo-rs-0.21/default) >= 0.21.0
Requires:       crate(glib-0.21/default) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-0.21/default) >= 0.21.0
Requires:       crate(pangocairo-sys-0.21/default) >= 0.21.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pangocairo"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
