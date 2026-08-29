# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name imagesize
%global full_version 0.13.0
%global pkgname imagesize-0.13

Name:           rust-imagesize-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "imagesize"
License:        MIT
URL:            https://github.com/Roughsketch/imagesize
#!RemoteAsset:  sha256:edcd27d72f2f071c64249075f42e205ff93c9a4c5f6c6da53e79ed9f9832c285
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "imagesize"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
