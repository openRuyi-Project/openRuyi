# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name supports-color
%global full_version 2.0.0
%global pkgname supports-color-2

Name:           rust-supports-color-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "supports-color"
License:        Apache-2.0
URL:            https://github.com/zkat/supports-color
#!RemoteAsset:  sha256:4950e7174bffabe99455511c39707310e7e9b440364a2fcb1cc21521be57b354
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(is-ci-1/default) >= 1.1.1
Requires:       crate(is-terminal-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "supports-color"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
