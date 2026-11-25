# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrayvec
%global full_version 0.7.8
%global pkgname arrayvec-0.7

Name:           rust-arrayvec-0.7
Version:        0.7.8
Release:        %autorelease
Summary:        Rust crate "arrayvec"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/arrayvec
#!RemoteAsset:  sha256:d3fb67a6e08acf24fdeccbac2cb6ac4305825bd1f117462e0e6f2f193345ad56
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Implements fixed capacity ArrayVec and ArrayString.
Source code for takopackized Rust crate "arrayvec"

%package     -n %{name}+borsh
Summary:        Vector with fixed capacity, backed by an array (it can be stored on the stack too) - feature "borsh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(borsh-1) >= 1.2.0
Provides:       crate(%{pkgname}/borsh) = %{version}

%description -n %{name}+borsh
Implements fixed capacity ArrayVec and ArrayString.
This metapackage enables feature "borsh" for the Rust arrayvec crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Vector with fixed capacity, backed by an array (it can be stored on the stack too) - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Implements fixed capacity ArrayVec and ArrayString.
This metapackage enables feature "serde" for the Rust arrayvec crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Vector with fixed capacity, backed by an array (it can be stored on the stack too) - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.4.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
Implements fixed capacity ArrayVec and ArrayString.
This metapackage enables feature "zeroize" for the Rust arrayvec crate, by
pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
