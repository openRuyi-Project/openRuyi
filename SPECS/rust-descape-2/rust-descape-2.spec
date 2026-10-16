# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name descape
%global full_version 2.0.3
%global pkgname descape-2

Name:           rust-descape-2
Version:        2.0.3
Release:        %autorelease
Summary:        Rust crate "descape"
License:        Apache-2.0 OR MIT
URL:            https://github.com/balt-dev/descape
#!RemoteAsset:  sha256:7c1113b908df80c963b107424498e37fba986b424b605729d1492dfbe4b2a630
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core-error) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "descape"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
