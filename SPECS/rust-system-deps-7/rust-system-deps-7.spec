# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name system-deps
%global full_version 7.0.8
%global pkgname system-deps-7

Name:           rust-system-deps-7
Version:        7.0.8
Release:        %autorelease
Summary:        Rust crate "system-deps"
License:        MIT OR Apache-2.0
URL:            https://github.com/gdesmott/system-deps
#!RemoteAsset:  sha256:396a35feb67335377e0251fcbc1092fc85c484bd4e3a7a54319399da127796e7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:         0001-fix-range-dependencies.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-expr-0.20/default) >= 0.20.8
Requires:       crate(cfg-expr-0.20/targets) >= 0.20.8
Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(pkg-config-0.3/default) >= 0.3.25
Requires:       crate(toml-1/parse) >= 1.0.0
Requires:       crate(toml-1/std) >= 1.0.0
Requires:       crate(version-compare-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "system-deps"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
