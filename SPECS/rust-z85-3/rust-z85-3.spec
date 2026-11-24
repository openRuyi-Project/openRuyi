# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name z85
%global full_version 3.0.5
%global pkgname z85-3

Name:           rust-z85-3
Version:        3.0.5
Release:        %autorelease
Summary:        Rust crate "z85"
License:        MIT OR Apache-2.0
URL:            https://github.com/decafbad/z85
#!RemoteAsset:  sha256:2a599daf1b507819c1121f0bf87fa37eb19daac6aff3aefefd4e6e2e0f2020fc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "z85"

%prep -a
# Cargo ships the original manifest as a backup.
rm -f Cargo.toml.orig .gitignore

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
