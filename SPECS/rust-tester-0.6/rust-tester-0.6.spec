# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tester
%global full_version 0.6.0
%global pkgname tester-0.6

Name:           rust-tester-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "tester"
License:        MIT OR Apache-2.0
URL:            https://github.com/messense/rustc-test
#!RemoteAsset:  sha256:7647e6d732eb84375d8e7abda37818f81861ddbfc7235e33f4983cb254b71e4f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getopts-0.2/default) >= 0.2.0
Requires:       crate(libc-0.2) >= 0.2.0
Requires:       crate(term-0.6/default) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/asm-black-box) = %{version}
Provides:       crate(%{pkgname}/capture) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tester"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
