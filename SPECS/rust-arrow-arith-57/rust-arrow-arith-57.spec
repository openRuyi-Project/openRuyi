# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-arith
%global full_version 57.3.1
%global pkgname arrow-arith-57

Name:           rust-arrow-arith-57
Version:        57.3.1
Release:        %autorelease
Summary:        Rust crate "arrow-arith"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:7c7bbd679c5418b8639b92be01f361d60013c4906574b578b77b63c78356594c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-57/default) >= 57.3.1
Requires:       crate(arrow-buffer-57/default) >= 57.3.1
Requires:       crate(arrow-data-57/default) >= 57.3.1
Requires:       crate(arrow-schema-57/default) >= 57.3.1
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(num-traits-0.2/std) >= 0.2.19

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-arith"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
