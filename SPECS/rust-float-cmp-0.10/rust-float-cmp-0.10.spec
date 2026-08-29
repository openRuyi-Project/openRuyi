# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name float-cmp
%global full_version 0.10.0
%global pkgname float-cmp-0.10

Name:           rust-float-cmp-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "float-cmp"
License:        MIT
URL:            https://github.com/mikedilger/float-cmp
#!RemoteAsset:  sha256:b09cf3155332e944990140d967ff5eceb70df778b34f77d8075db46e4704e6d8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "float-cmp"

%package     -n %{name}+num-traits
Summary:        Floating point approximate comparison traits - feature "num-traits" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2) >= 0.2.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/num-traits) = %{version}
Provides:       crate(%{pkgname}/ratio) = %{version}

%description -n %{name}+num-traits
This metapackage enables feature "num-traits" for the Rust float-cmp crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "ratio" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
