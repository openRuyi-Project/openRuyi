# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name const-random-macro
%global full_version 0.1.16
%global pkgname const-random-macro-0.1

Name:           rust-const-random-macro-0.1
Version:        0.1.16
Release:        %autorelease
Summary:        Rust crate "const-random-macro"
License:        MIT OR Apache-2.0
URL:            https://github.com/tkaitchuck/constrandom
#!RemoteAsset:  sha256:f9d839f2a20b0aee515dc581a6172f2321f96cab76c1a38a4c584a194955390e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.2/default) >= 0.2.0
Requires:       crate(once-cell-1/alloc) >= 1.15.0
Requires:       crate(once-cell-1/race) >= 1.15.0
Requires:       crate(tiny-keccak-2/default) >= 2.0.2
Requires:       crate(tiny-keccak-2/shake) >= 2.0.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "const-random-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
