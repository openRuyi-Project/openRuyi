# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ar_archive_writer
%global full_version 0.5.2
%global pkgname ar-archive-writer-0.5

Name:           rust-ar-archive-writer-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "ar_archive_writer"
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/rust-lang/ar_archive_writer
#!RemoteAsset:  sha256:4087686b4b0a3427190bae57a1d9a478dbb2d40c5dc1bd6e2b6d797913bdd348
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(object-0.37/read) >= 0.37.1
Requires:       crate(object-0.37/std) >= 0.37.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ar_archive_writer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
