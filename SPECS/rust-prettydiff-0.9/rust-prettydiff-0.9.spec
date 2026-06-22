# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prettydiff
%global full_version 0.9.0
%global pkgname prettydiff-0.9

Name:           rust-prettydiff-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "prettydiff"
License:        MIT
URL:            https://github.com/romankoblov/prettydiff
#!RemoteAsset:  sha256:ac17546d82912e64874e3d5b40681ce32eac4e5834344f51efcf689ff1550a65
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(owo-colors-4/default) >= 4.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "prettydiff"

%package     -n %{name}+prettytable-rs
Summary:        Side-by-side diff for two files - feature "prettytable-rs" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prettytable-rs-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/cli) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/prettytable-rs) = %{version}

%description -n %{name}+prettytable-rs
This metapackage enables feature "prettytable-rs" for the Rust prettydiff crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cli", and "default" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
