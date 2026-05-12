# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name id-arena
%global full_version 2.3.0
%global pkgname id-arena-2.0

Name:           rust-id-arena-2.0
Version:        2.3.0
Release:        %autorelease
Summary:        Rust crate "id-arena"
License:        MIT/Apache-2.0
URL:            https://github.com/fitzgen/id-arena
#!RemoteAsset:  sha256:3d3067d79b975e8844ca9eb072e16b31c3c1c36928edf9c6789548c524d0d954
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "id-arena"

%package     -n %{name}+rayon
Summary:        Simple, id-based arena - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.0.3
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust id-arena crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
