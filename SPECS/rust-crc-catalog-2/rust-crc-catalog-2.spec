# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crc-catalog
%global full_version 2.5.0
%global pkgname crc-catalog-2

Name:           rust-crc-catalog-2
Version:        2.5.0
Release:        %autorelease
Summary:        Rust crate "crc-catalog"
License:        MIT OR Apache-2.0
URL:            https://github.com/akhilles/crc-catalog.git
#!RemoteAsset:  sha256:217698eaf96b4a3f0bc4f3662aaa55bdf913cd54d7204591faa790070c6d0853
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "crc-catalog"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
