# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name encoding_index_tests
%global full_version 0.1.4
%global pkgname encoding-index-tests-0.1

Name:           rust-encoding-index-tests-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "encoding_index_tests"
License:        CC0-1.0
URL:            https://github.com/lifthrasiir/rust-encoding
#!RemoteAsset:  sha256:a246d82be1c9d791c5dfde9a2bd045fc3cbba3fa2b11ad558f27d01712f00569
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "encoding_index_tests"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
