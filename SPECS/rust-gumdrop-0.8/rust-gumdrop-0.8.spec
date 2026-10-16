# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gumdrop
%global full_version 0.8.1
%global pkgname gumdrop-0.8

Name:           rust-gumdrop-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "gumdrop"
License:        MIT OR Apache-2.0
URL:            https://github.com/murarth/gumdrop
#!RemoteAsset:  sha256:5bc700f989d2f6f0248546222d9b4258f5b02a171a431f8285a81c08142629e3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gumdrop-derive-0.8/default) >= 0.8.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gumdrop"

%package     -n %{name}+default-expr
Summary:        Option parser with custom derive support - feature "default_expr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gumdrop-derive-0.8/default-expr) >= 0.8.1
Provides:       crate(%{pkgname}/default-expr) = %{version}

%description -n %{name}+default-expr
This metapackage enables feature "default_expr" for the Rust gumdrop crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
