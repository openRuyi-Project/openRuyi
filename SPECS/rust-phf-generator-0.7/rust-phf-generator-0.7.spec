# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf_generator
%global full_version 0.7.24
%global pkgname phf-generator-0.7

Name:           rust-phf-generator-0.7
Version:        0.7.24
Release:        %autorelease
Summary:        Rust crate "phf_generator"
License:        MIT
URL:            https://github.com/sfackler/rust-phf
#!RemoteAsset:  sha256:09364cc93c159b8b06b1f4dd8a4398984503483891b0c26b867cf431fb132662
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-shared-0.7/default) >= 0.7.24
Requires:       crate(rand-0.6/default) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "phf_generator"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
