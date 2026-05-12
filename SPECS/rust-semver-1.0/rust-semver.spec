# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name semver
%global full_version 1.0.27
%global pkgname semver-1.0

Name:           rust-semver-1.0
Version:        1.0.27
Release:        %autorelease
Summary:        Rust crate "semver"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/semver
#!RemoteAsset:  sha256:d767eb0aabc880b29956c35734170f26ed551a859dbd361d140cdbeca61ab1e2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "semver"

%package     -n %{name}+serde
Summary:        Parser and evaluator for Cargo's flavor of Semantic Versioning - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.220
Requires:       crate(serde-core-1.0) >= 1.0.220
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust semver crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
