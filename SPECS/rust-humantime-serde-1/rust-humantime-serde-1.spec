# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name humantime-serde
%global full_version 1.1.1
%global pkgname humantime-serde-1

Name:           rust-humantime-serde-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "humantime-serde"
License:        MIT OR Apache-2.0
URL:            https://github.com/jean-airoldie/humantime-serde
#!RemoteAsset:  sha256:57a3db5ea5923d99402c94e9feb261dc5ee9b4efa158b0315f788cf549cc200c
Source:         https://static.crates.io/crates/humantime-serde/1.1.1/download#/rust-humantime-serde-1-1.1.1.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(humantime-2/default) >= 2.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "humantime-serde"

%package     -n %{name}+default
Summary:        Serde support for the `humantime` crate - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust humantime-serde crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
