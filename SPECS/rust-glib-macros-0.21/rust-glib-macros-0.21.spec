# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glib-macros
%global full_version 0.21.5
%global pkgname glib-macros-0.21

Name:           rust-glib-macros-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "glib-macros"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:cf59b675301228a696fe01c3073974643365080a76cc3ed5bc2cbc466ad87f17
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro-crate-3/default) >= 3.3.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.104
Requires:       crate(syn-2/full) >= 2.0.104
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "glib-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
