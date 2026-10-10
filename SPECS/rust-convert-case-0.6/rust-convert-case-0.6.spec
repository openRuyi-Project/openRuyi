# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name convert_case
%global full_version 0.6.0
%global pkgname convert-case-0.6

Name:           rust-convert-case-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "convert_case"
License:        MIT
URL:            https://github.com/rutrum/convert-case
#!RemoteAsset:  sha256:ec182b0ca2f35d8fc196cf3404988fd8b8c739a4d270ff118a398feb0cbec1ca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-segmentation-1/default) >= 1.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "convert_case"

%package     -n %{name}+rand
Summary:        Convert strings into any case - feature "rand" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/random) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust convert_case crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "random" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
