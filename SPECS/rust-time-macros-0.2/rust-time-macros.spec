# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name time-macros
%global full_version 0.2.27
%global pkgname time-macros-0.2

Name:           rust-time-macros-0.2
Version:        0.2.27
Release:        %autorelease
Summary:        Rust crate "time-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/time-rs/time
#!RemoteAsset:  sha256:2e70e4c5a0e0a8a4823ad65dfe1a6930e4f4d756dcd9dd7939022b5e8c501215
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-conv-0.2/default) >= 0.2.1
Requires:       crate(time-core-0.1/default) >= 0.1.8
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/formatting)
Provides:       crate(%{pkgname}/large-dates)
Provides:       crate(%{pkgname}/parsing)
Provides:       crate(%{pkgname}/serde)

%description
This crate is an implementation detail and should not be relied upon directly.
Source code for takopackized Rust crate "time-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
