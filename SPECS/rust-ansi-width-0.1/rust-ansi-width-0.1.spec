# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ansi-width
%global full_version 0.1.0
%global pkgname ansi-width-0.1

Name:           rust-ansi-width-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "ansi-width"
License:        MIT
URL:            FIXME
#!RemoteAsset:  sha256:219e3ce6f2611d83b51ec2098a12702112c29e57203a6b0a0929b2cddb486608
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-width-0.1/default) >= 0.1.11

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ansi-width"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
