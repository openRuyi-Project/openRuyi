# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-collections
%global full_version 0.3.2
%global pkgname windows-collections-0.3

Name:           rust-windows-collections-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "windows-collections"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:23b2d95af1a8a14a3c7367e1ed4fc9c20e0a26e79551b1454d72583c97cc6610
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-core-0.62) >= 0.62.2
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "windows-collections"

%package     -n %{name}+std
Summary:        Windows collection types - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-core-0.62/std) >= 0.62.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust windows-collections crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
