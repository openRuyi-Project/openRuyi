# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-future
%global full_version 0.3.2
%global pkgname windows-future-0.3

Name:           rust-windows-future-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "windows-future"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:e1d6f90251fe18a279739e78025bd6ddc52a7e22f921070ccdc67dde84c605cb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-core-0.62) >= 0.62.2
Requires:       crate(windows-link-0.2) >= 0.2.1
Requires:       crate(windows-threading-0.2) >= 0.2.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "windows-future"

%package     -n %{name}+std
Summary:        Windows async types - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-core-0.62/std) >= 0.62.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust windows-future crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
