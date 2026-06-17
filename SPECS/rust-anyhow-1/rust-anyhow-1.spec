# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anyhow
%global full_version 1.0.102
%global pkgname anyhow-1

Name:           rust-anyhow-1
Version:        1.0.102
Release:        %autorelease
Summary:        Rust crate "anyhow"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/anyhow
#!RemoteAsset:  sha256:7f202df86484c868dbad7eaa557ef785d5c66295e41b460ef922eca0723b842c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/backtrace) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "anyhow"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
