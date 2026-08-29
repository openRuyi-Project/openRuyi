# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pangocairo
%global full_version 0.22.0
%global pkgname pangocairo-0.22

Name:           rust-pangocairo-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "pangocairo"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:d9f15369c787b1cc59a5b86eff6afffd5a9716c5beb4969d20b307cebfe7e407
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cairo-rs-0.22/default) >= 0.22.0
Requires:       crate(glib-0.22) >= 0.22.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-0.22/default) >= 0.22.0
Requires:       crate(pangocairo-sys-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pangocairo"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
