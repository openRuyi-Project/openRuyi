# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf_generator
%global full_version 0.9.0
%global pkgname phf-generator-0.9

Name:           rust-phf-generator-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "phf_generator"
License:        MIT
URL:            https://github.com/sfackler/rust-phf
#!RemoteAsset:  sha256:0fc1437ada0f3a97d538f0bb608137bf53c53969028cab74c89893e1e9a12f0e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-shared-0.9) >= 0.9.0
Requires:       crate(rand-0.8/default) >= 0.8.0
Requires:       crate(rand-0.8/small-rng) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "phf_generator"

%package     -n %{name}+criterion
Summary:        PHF generation logic - feature "criterion"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(criterion-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/criterion) = %{version}

%description -n %{name}+criterion
This metapackage enables feature "criterion" for the Rust phf_generator crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
