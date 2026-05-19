# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libtest-mimic
%global full_version 0.8.1
%global pkgname libtest-mimic-0.8

Name:           rust-libtest-mimic-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "libtest-mimic"
License:        MIT/Apache-2.0
URL:            https://github.com/LukasKalbertodt/libtest-mimic
#!RemoteAsset:  sha256:5297962ef19edda4ce33aaa484386e0a5b3d7f2f4e037cbeee00503ef6b29d33
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstream-0.6/default) >= 0.6.21
Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(clap-4.0/default) >= 4.6.1
Requires:       crate(clap-4.0/derive) >= 4.6.1
Requires:       crate(escape8259-0.5/default) >= 0.5.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "libtest-mimic"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
