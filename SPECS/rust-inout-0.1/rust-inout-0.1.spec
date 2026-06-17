# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name inout
%global full_version 0.1.4
%global pkgname inout-0.1

Name:           rust-inout-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "inout"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/utils
#!RemoteAsset:  sha256:879f10e63c20629ecabbb64a8010319738c66a5cd0c29b02d63d272b03751d01
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(generic-array-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "inout"

%package     -n %{name}+block-padding
Summary:        Custom reference types for code generic over in-place and buffer-to-buffer modes of operation - feature "block-padding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block-padding-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/block-padding) = %{version}

%description -n %{name}+block-padding
This metapackage enables feature "block-padding" for the Rust inout crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Custom reference types for code generic over in-place and buffer-to-buffer modes of operation - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block-padding-0.3/std) >= 0.3.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust inout crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
