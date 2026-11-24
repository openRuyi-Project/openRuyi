# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name data-encoding-macro
%global full_version 0.1.19
%global pkgname data-encoding-macro-0.1

Name:           rust-data-encoding-macro-0.1
Version:        0.1.19
Release:        %autorelease
Summary:        Rust crate "data-encoding-macro"
License:        MIT
URL:            https://github.com/ia0/data-encoding
#!RemoteAsset:  sha256:8142a83c17aa9461d637e649271eae18bf2edd00e91f2e105df36c3c16355bdb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(data-encoding-2) >= 2.10.0
Requires:       crate(data-encoding-macro-internal-0.1/default) >= 0.1.17

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "data-encoding-macro"

%prep -a
# Cargo ships the original manifest as a backup.
rm -f Cargo.toml.orig

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
