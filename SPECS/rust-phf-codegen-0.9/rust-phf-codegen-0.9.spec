# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf_codegen
%global full_version 0.9.0
%global pkgname phf-codegen-0.9

Name:           rust-phf-codegen-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "phf_codegen"
License:        MIT
URL:            https://github.com/sfackler/rust-phf
#!RemoteAsset:  sha256:963adb11cf22ee65dfd401cf75577c1aa0eca58c0b97f9337d2da61d3e640503
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-generator-0.9/default) >= 0.9.0
Requires:       crate(phf-shared-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "phf_codegen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
