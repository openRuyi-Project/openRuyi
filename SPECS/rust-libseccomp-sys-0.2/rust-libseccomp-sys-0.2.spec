# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libseccomp-sys
%global full_version 0.2.1
%global pkgname libseccomp-sys-0.2

Name:           rust-libseccomp-sys-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "libseccomp-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/libseccomp-rs/libseccomp-rs
#!RemoteAsset:  sha256:9a7cbbd4ad467251987c6e5b47d53b11a5a05add08f2447a9e2d70aef1e0d138
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "libseccomp-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
