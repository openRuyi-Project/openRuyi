# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name minicov
%global full_version 0.3.7
%global pkgname minicov-0.3

Name:           rust-minicov-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "minicov"
License:        Apache-2.0/MIT
URL:            https://github.com/Amanieu/minicov
#!RemoteAsset:  sha256:f27fe9f1cc3c22e1687f9446c2083c4c5fc7f0bcf1c7a86bdbded14985895b4b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.38
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "minicov"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
