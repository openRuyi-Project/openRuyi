# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name intrusive-collections
%global full_version 0.9.7
%global pkgname intrusive-collections-0.9

Name:           rust-intrusive-collections-0.9
Version:        0.9.7
Release:        %autorelease
Summary:        Rust crate "intrusive-collections"
License:        Apache-2.0/MIT
URL:            https://github.com/Amanieu/intrusive-rs
#!RemoteAsset:  sha256:189d0897e4cbe8c75efedf3502c18c887b05046e59d28404d4d8e46cbc4d1e86
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memoffset-0.9/default) >= 0.9.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)

%description
Source code for takopackized Rust crate "intrusive-collections"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
