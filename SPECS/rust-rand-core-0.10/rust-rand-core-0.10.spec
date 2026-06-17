# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_core
%global full_version 0.10.1
%global pkgname rand-core-0.10

Name:           rust-rand-core-0.10
Version:        0.10.1
Release:        %autorelease
Summary:        Rust crate "rand_core"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:63b8176103e19a2643978565ca18b50549f6101881c443590420e4dc998a3c69
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rand_core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
