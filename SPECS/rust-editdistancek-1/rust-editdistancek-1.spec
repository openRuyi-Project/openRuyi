# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name editdistancek
%global full_version 1.0.2
%global pkgname editdistancek-1

Name:           rust-editdistancek-1
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "editdistancek"
License:        MIT
URL:            https://github.com/nkkarpov/editdistancek
#!RemoteAsset:  sha256:3e02df23d5b1c6f9e69fa603b890378123b93073df998a21e6e33b9db0a32613
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "editdistancek"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
