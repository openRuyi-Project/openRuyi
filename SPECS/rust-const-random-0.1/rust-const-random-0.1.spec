# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name const-random
%global full_version 0.1.18
%global pkgname const-random-0.1

Name:           rust-const-random-0.1
Version:        0.1.18
Release:        %autorelease
Summary:        Rust crate "const-random"
License:        MIT OR Apache-2.0
URL:            https://github.com/tkaitchuck/constrandom
#!RemoteAsset:  sha256:87e00182fe74b066627d63b85fd550ac2998d4b0bd86bfed477a0ae4c7c71359
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-random-macro-0.1/default) >= 0.1.16

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "const-random"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
