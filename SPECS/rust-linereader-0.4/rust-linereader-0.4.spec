# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linereader
%global full_version 0.4.0
%global pkgname linereader-0.4

Name:           rust-linereader-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "linereader"
License:        MIT
URL:            https://github.com/Freaky/rust-linereader
#!RemoteAsset:  sha256:d921fea6860357575519aca014c6e22470585accdd543b370c404a8a72d0dd1d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "linereader"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
