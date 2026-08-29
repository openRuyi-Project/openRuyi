# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name acpi_tables
%global full_version 0.2.0
%global pkgname acpi-tables-0.2

Name:           rust-acpi-tables-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "acpi_tables"
License:        Apache-2.0
URL:            https://github.com/rust-vmm/acpi_tables
#!RemoteAsset:  sha256:5ad581b2b0fa02638f3df6ff3f852ebc30dc7cfe531e9745d1ca4c0f283a6dbe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zerocopy-0.8/default) >= 0.8.23
Requires:       crate(zerocopy-0.8/derive) >= 0.8.23
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "acpi_tables"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
