# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cloudabi
%global full_version 0.0.3
%global pkgname cloudabi-0.0.3

Name:           rust-cloudabi-0.0.3
Version:        0.0.3
Release:        %autorelease
Summary:        Rust crate "cloudabi"
License:        BSD-2-Clause
URL:            https://nuxi.nl/cloudabi/
#!RemoteAsset:  sha256:ddfc5b9aa5d4507acaf872de71051dfd0e309860e88966e1051e462a077aac4f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Contains all syscalls and related types.
Source code for takopackized Rust crate "cloudabi"

%package     -n %{name}+bitflags
Summary:        Low level interface to CloudABI - feature "bitflags" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bitflags) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+bitflags
Contains all syscalls and related types.
This metapackage enables feature "bitflags" for the Rust cloudabi crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
