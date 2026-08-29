# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atomic-polyfill
%global full_version 1.0.3
%global pkgname atomic-polyfill-1

Name:           rust-atomic-polyfill-1
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "atomic-polyfill"
License:        MIT OR Apache-2.0
URL:            https://github.com/embassy-rs/atomic-polyfill
#!RemoteAsset:  sha256:8cf2bce30dfe09ef0bfaef228b9d414faaf7e563035494d7fe092dba54b300f4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(critical-section-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "atomic-polyfill"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
