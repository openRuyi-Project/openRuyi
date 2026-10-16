# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pikchr
%global full_version 0.1.4
%global pkgname pikchr-0.1

Name:           rust-pikchr-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "pikchr"
License:        MIT OR Apache-2.0
URL:            https://github.com/kinnison/pikchr
#!RemoteAsset:  sha256:13680336a9060974d823f15053decc0ae5380eebf6f82abf17608523a7d71826
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.2.0
Requires:       crate(libc-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pikchr"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
