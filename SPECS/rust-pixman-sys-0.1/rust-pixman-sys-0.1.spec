# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pixman-sys
%global full_version 0.1.0
%global pkgname pixman-sys-0.1

Name:           rust-pixman-sys-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "pixman-sys"
License:        MIT
URL:            https://github.com/cmeissl/pixman-rs
#!RemoteAsset:  sha256:a1a0483e89e81d7915defe83c51f23f6800594d64f6f4a21253ce87fd8444ada
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pixman-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
