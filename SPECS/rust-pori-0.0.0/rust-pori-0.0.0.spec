# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pori
%global full_version 0.0.0
%global pkgname pori-0.0.0

Name:           rust-pori-0.0.0
Version:        0.0.0
Release:        %autorelease
Summary:        Rust crate "pori"
License:        MIT
URL:            https://github.com/olson-sean-k/pori
#!RemoteAsset:  sha256:a4a63d338dec139f56dacc692ca63ad35a6be6a797442479b55acd611d79e906
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(nom-7/default) >= 7.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pori"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
