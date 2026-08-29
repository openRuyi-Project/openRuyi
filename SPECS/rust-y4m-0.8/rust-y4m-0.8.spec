# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name y4m
%global full_version 0.8.0
%global pkgname y4m-0.8

Name:           rust-y4m-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "y4m"
License:        MIT
URL:            https://github.com/image-rs/y4m
#!RemoteAsset:  sha256:7a5a4b21e1a62b67a2970e6831bc091d7b87e119e7f9791aef9702e3bef04448
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "y4m"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
