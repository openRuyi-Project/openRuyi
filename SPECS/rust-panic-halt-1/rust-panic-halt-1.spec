# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name panic-halt
%global full_version 1.0.0
%global pkgname panic-halt-1

Name:           rust-panic-halt-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "panic-halt"
License:        MIT OR Apache-2.0
URL:            https://github.com/korken89/panic-halt
#!RemoteAsset:  sha256:a513e167849a384b7f9b746e517604398518590a9142f4846a32e3c2a4de7b11
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "panic-halt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
