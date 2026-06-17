# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-core
%global full_version 0.62.2
%global pkgname windows-core-0.62

Name:           rust-windows-core-0.62
Version:        0.62.2
Release:        %autorelease
Summary:        Rust crate "windows-core"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:b8e83a14d34d0623b51dce9581199302a221863196a1dde71a7663a4c2be9deb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-implement-0.60) >= 0.60.2
Requires:       crate(windows-interface-0.59) >= 0.59.3
Requires:       crate(windows-link-0.2) >= 0.2.1
Requires:       crate(windows-result-0.4) >= 0.4.1
Requires:       crate(windows-strings-0.5) >= 0.5.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "windows-core"

%package     -n %{name}+std
Summary:        Core type support for COM and Windows - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-result-0.4/std) >= 0.4.1
Requires:       crate(windows-strings-0.5/std) >= 0.5.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust windows-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
