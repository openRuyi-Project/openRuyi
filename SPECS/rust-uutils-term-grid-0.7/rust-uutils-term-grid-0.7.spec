# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uutils_term_grid
%global full_version 0.7.0
%global pkgname uutils-term-grid-0.7

Name:           rust-uutils-term-grid-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "uutils_term_grid"
License:        MIT
URL:            https://github.com/uutils/uutils-term-grid
#!RemoteAsset:  sha256:fcba141ce511bad08e80b43f02976571072e1ff4286f7d628943efbd277c6361
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ansi-width-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Fork of term_grid.
Source code for takopackized Rust crate "uutils_term_grid"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
