# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name itoa
%global full_version 1.0.18
%global pkgname itoa-1.0

Name:           rust-itoa-1.0
Version:        1.0.18
Release:        %autorelease
Summary:        Rust crate "itoa"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/itoa
#!RemoteAsset:  sha256:8f42a60cbdf9a97f5d2305f08a87dc4e09308d1276d28c869c684d7777685682
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "itoa"

%package     -n %{name}+no-panic
Summary:        Fast integer primitive to string conversion - feature "no-panic"
Requires:       crate(%{pkgname})
Requires:       crate(no-panic-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/no-panic)

%description -n %{name}+no-panic
This metapackage enables feature "no-panic" for the Rust itoa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
