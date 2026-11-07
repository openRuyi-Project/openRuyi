# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memchr
%global full_version 0.1.11
%global pkgname memchr-0.1

Name:           rust-memchr-0.1
Version:        0.1.11
Release:        %autorelease
Summary:        Rust crate "memchr"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/rust-memchr
#!RemoteAsset:  sha256:d8b629fb514376c675b98c1421e80b151d3817ac42d7c667717d282761418d20
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "memchr"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
