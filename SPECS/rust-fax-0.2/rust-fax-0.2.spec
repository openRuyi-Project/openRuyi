# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fax
%global full_version 0.2.7
%global pkgname fax-0.2

Name:           rust-fax-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "fax"
License:        MIT
URL:            https://github.com/pdf-rs/fax
#!RemoteAsset:  sha256:caf1079563223d5d59d83c85886a56e586cfd5c1a26292e971a0fa266531ac5a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fax"

%package     -n %{name}+generate-bitmaps
Summary:        Decoder and Encoder for CCITT Group 3 and 4 bi-level image encodings used by fax machines TIFF and PDF - feature "generate_bitmaps"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fax-derive-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/generate-bitmaps) = %{version}

%description -n %{name}+generate-bitmaps
This metapackage enables feature "generate_bitmaps" for the Rust fax crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
