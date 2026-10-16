# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-registry
%global full_version 0.5.3
%global pkgname windows-registry-0.5

Name:           rust-windows-registry-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "windows-registry"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:5b8a9ed28765efc97bbc954883f4e6796c33a06546ebafacbabee9696967499e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-link-0.1) >= 0.1.3
Requires:       crate(windows-result-0.3) >= 0.3.4
Requires:       crate(windows-strings-0.4) >= 0.4.2

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "windows-registry"

%package     -n %{name}+std
Summary:        Windows registry - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-result-0.3/std) >= 0.3.4
Requires:       crate(windows-strings-0.4/std) >= 0.4.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust windows-registry crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
