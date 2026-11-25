# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atomic
%global full_version 0.5.3
%global pkgname atomic-0.5

Name:           rust-atomic-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "atomic"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/atomic-rs
#!RemoteAsset:  sha256:c59bdb34bc650a32731b31bd8f0829cc15d24a708ee31559e0bb34f2bc320cba
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fallback) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "atomic"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
