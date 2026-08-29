# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name colored
%global full_version 2.2.0
%global pkgname colored-2

Name:           rust-colored-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "colored"
License:        MPL-2.0
URL:            https://github.com/mackwic/colored
#!RemoteAsset:  sha256:117725a109d387c937a1533ce01b450cbde6b88abceea8473c4d7a85853cda3c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-color) = %{version}

%description
Source code for takopackized Rust crate "colored"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
