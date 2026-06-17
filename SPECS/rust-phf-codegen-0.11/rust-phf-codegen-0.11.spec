# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf_codegen
%global full_version 0.11.3
%global pkgname phf-codegen-0.11

Name:           rust-phf-codegen-0.11
Version:        0.11.3
Release:        %autorelease
Summary:        Rust crate "phf_codegen"
License:        MIT
URL:            https://github.com/rust-phf/rust-phf
#!RemoteAsset:  sha256:aef8048c789fa5e851558d709946d6d79a8ff88c0440c587967f8e94bfb1216a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-generator-0.11/default) >= 0.11.0
Requires:       crate(phf-shared-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "phf_codegen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
