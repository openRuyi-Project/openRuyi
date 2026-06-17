# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name enumflags2
%global full_version 0.7.12
%global pkgname enumflags2-0.7

Name:           rust-enumflags2-0.7
Version:        0.7.12
Release:        %autorelease
Summary:        Rust crate "enumflags2"
License:        MIT OR Apache-2.0
URL:            https://github.com/meithecatte/enumflags2
#!RemoteAsset:  sha256:1027f7680c853e056ebcec683615fb6fbbc07dbaa13b4d5d9442b146ded4ecef
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(enumflags2-derive-0.7/default) >= 0.7.12
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "enumflags2"

%package     -n %{name}+serde
Summary:        Enum-based bit flags - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust enumflags2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
