# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fallible-streaming-iterator
%global full_version 0.1.9
%global pkgname fallible-streaming-iterator-0.1

Name:           rust-fallible-streaming-iterator-0.1
Version:        0.1.9
Release:        %autorelease
Summary:        Rust crate "fallible-streaming-iterator"
License:        MIT OR Apache-2.0
URL:            https://github.com/sfackler/fallible-streaming-iterator
#!RemoteAsset:  sha256:7360491ce676a36bf9bb3c56c1aa791658183a54d2744120f27285738d90465a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "fallible-streaming-iterator"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
