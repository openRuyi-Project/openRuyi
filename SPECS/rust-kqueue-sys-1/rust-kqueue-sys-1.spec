# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kqueue-sys
%global full_version 1.1.0
%global pkgname kqueue-sys-1

Name:           rust-kqueue-sys-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "kqueue-sys"
License:        MIT
URL:            https://gitlab.com/rust-kqueue/rust-kqueue-sys
#!RemoteAsset:  sha256:a7b65860415f949f23fa882e669f2dbd4a0f0eeb1acdd56790b30494afd7da2f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2) >= 2.11.0
Requires:       crate(libc-0.2/default) >= 0.2.74
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "kqueue-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
