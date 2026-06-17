# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-numerics
%global full_version 0.3.1
%global pkgname windows-numerics-0.3

Name:           rust-windows-numerics-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "windows-numerics"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:6e2e40844ac143cdb44aead537bbf727de9b044e107a0f1220392177d15b0f26
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-core-0.62) >= 0.62.2
Requires:       crate(windows-link-0.2) >= 0.2.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "windows-numerics"

%package     -n %{name}+std
Summary:        Windows numeric types - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-core-0.62/std) >= 0.62.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust windows-numerics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
