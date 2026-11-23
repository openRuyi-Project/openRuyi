# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name locale
%global full_version 0.2.2
%global pkgname locale-0.2

Name:           rust-locale-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "locale"
License:        MIT
URL:            https://github.com/rust-locale/rust-locale/
#!RemoteAsset:  sha256:5fdbe492a9c0238da900a1165c42fc5067161ce292678a6fe80921f30fe307fd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Warning: Major rewrite pending for 0.3!
Source code for takopackized Rust crate "locale"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
