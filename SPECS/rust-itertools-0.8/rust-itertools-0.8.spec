# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name itertools
%global full_version 0.8.2
%global pkgname itertools-0.8

Name:           rust-itertools-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "itertools"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/rust-itertools
#!RemoteAsset:  sha256:f56a2d0bc861f9165be4eb3442afd3c236d8a98afd426f65d92324ae1091a484
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description
Source code for takopackized Rust crate "itertools"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
