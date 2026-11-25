# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mac-addr
%global full_version 0.3.0
%global pkgname mac-addr-0.3

Name:           rust-mac-addr-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "mac-addr"
License:        MIT
URL:            https://github.com/shellrow/mac-addr
#!RemoteAsset:  sha256:d3d25b0e0b648a86960ac23b7ad4abb9717601dec6f66c165f5b037f3f03065f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "mac-addr"

%package     -n %{name}+serde
Summary:        Lightweight, no_std compatible MAC address library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust mac-addr crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
