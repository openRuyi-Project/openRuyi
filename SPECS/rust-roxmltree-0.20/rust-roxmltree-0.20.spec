# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name roxmltree
%global full_version 0.20.0
%global pkgname roxmltree-0.20

Name:           rust-roxmltree-0.20
Version:        0.20.0
Release:        %autorelease
Summary:        Rust crate "roxmltree"
License:        MIT OR Apache-2.0
URL:            https://github.com/RazrFalcon/roxmltree
#!RemoteAsset:  sha256:6c20b6793b5c2fa6553b250154b78d6d0db37e72700ae35fad9387a46f487c97
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/positions) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "roxmltree"

%package     -n %{name}+default
Summary:        Represent an XML as a read-only tree - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/positions) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust roxmltree crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
