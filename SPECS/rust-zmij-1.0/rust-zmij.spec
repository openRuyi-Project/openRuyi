# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zmij
%global full_version 1.0.21
%global pkgname zmij-1.0

Name:           rust-zmij-1.0
Version:        1.0.21
Release:        %autorelease
Summary:        Rust crate "zmij"
License:        MIT
URL:            https://github.com/dtolnay/zmij
#!RemoteAsset:  sha256:b8848ee67ecc8aedbaf3e4122217aff892639231befc6a1b58d29fff4c2cabaa
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "zmij"

%package     -n %{name}+no-panic
Summary:        Double-to-string conversion algorithm based on Schubfach and yy - feature "no-panic"
Requires:       crate(%{pkgname})
Requires:       crate(no-panic-0.1/default) >= 0.1.36
Provides:       crate(%{pkgname}/no-panic)

%description -n %{name}+no-panic
This metapackage enables feature "no-panic" for the Rust zmij crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
