# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf_generator
%global full_version 0.11.3
%global pkgname phf-generator-0.11

Name:           rust-phf-generator-0.11
Version:        0.11.3
Release:        %autorelease
Summary:        Rust crate "phf_generator"
License:        MIT
URL:            https://github.com/rust-phf/rust-phf
#!RemoteAsset:  sha256:3c80231409c20246a13fddb31776fb942c38553c51e871f8cbd687a4cfb5843d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-shared-0.11) >= 0.11.2
Requires:       crate(rand-0.8/small-rng) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "phf_generator"

%package     -n %{name}+criterion
Summary:        PHF generation logic - feature "criterion"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(criterion-0.3/default) >= 0.3.6
Provides:       crate(%{pkgname}/criterion) = %{version}

%description -n %{name}+criterion
This metapackage enables feature "criterion" for the Rust phf_generator crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
