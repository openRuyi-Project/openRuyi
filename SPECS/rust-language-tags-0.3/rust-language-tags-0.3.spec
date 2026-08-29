# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name language-tags
%global full_version 0.3.2
%global pkgname language-tags-0.3

Name:           rust-language-tags-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "language-tags"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyfisch/rust-language-tags
#!RemoteAsset:  sha256:d4345964bb142484797b161f473a503a434de77149dd8c7427788c6e13379388
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "language-tags"

%package     -n %{name}+serde
Summary:        Language tags for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust language-tags crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
