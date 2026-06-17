# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ansi-to-tui
%global full_version 8.0.1
%global pkgname ansi-to-tui-8

Name:           rust-ansi-to-tui-8
Version:        8.0.1
Release:        %autorelease
Summary:        Rust crate "ansi-to-tui"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:e42366bb9d958f042bf58f0a85e1b2d091997c1257ca49bddd7e4827aadc65fd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(nom-8/default) >= 8.0.0
Requires:       crate(ratatui-core-0.1) >= 0.1.0
Requires:       crate(smallvec-1/const-generics) >= 1.0.0
Requires:       crate(smallvec-1/default) >= 1.0.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/zero-copy) = %{version}

%description
Source code for takopackized Rust crate "ansi-to-tui"

%package     -n %{name}+default
Summary:        Convert ANSI color and style codes into Ratatui Text - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/simd) = %{version}
Requires:       crate(%{pkgname}/zero-copy) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ansi-to-tui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simd
Summary:        Convert ANSI color and style codes into Ratatui Text - feature "simd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simdutf8-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/simd) = %{version}

%description -n %{name}+simd
This metapackage enables feature "simd" for the Rust ansi-to-tui crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
