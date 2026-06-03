# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-timer
%global full_version 3.0.3
%global pkgname futures-timer-3.0

Name:           rust-futures-timer-3.0
Version:        3.0.3
Release:        %autorelease
Summary:        Rust crate "futures-timer"
License:        MIT OR Apache-2.0
URL:            https://github.com/async-rs/futures-timer
#!RemoteAsset:  sha256:f288b0a4f20f9a56b5d1da57e2227c661b7b16168e2f72365f57b63326e29b24
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "futures-timer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
