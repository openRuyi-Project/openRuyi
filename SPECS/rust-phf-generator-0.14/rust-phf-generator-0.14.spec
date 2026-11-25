# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf_generator
%global full_version 0.14.0
%global pkgname phf-generator-0.14

Name:           rust-phf-generator-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "phf_generator"
License:        MIT
URL:            https://github.com/rust-phf/rust-phf
#!RemoteAsset:  sha256:aeb62e0959d5a1bebc965f4d15d9e2b7cea002b6b0f5ba8cde6cc26738467100
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fastrand-2) >= 2.1.0
Requires:       crate(phf-shared-0.14) >= 0.14.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "phf_generator"

%package     -n %{name}+ptrhash
Summary:        PHF generation logic - feature "ptrhash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-shared-0.14/ptrhash) >= 0.14.0
Provides:       crate(%{pkgname}/ptrhash) = %{version}

%description -n %{name}+ptrhash
This metapackage enables feature "ptrhash" for the Rust phf_generator crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
