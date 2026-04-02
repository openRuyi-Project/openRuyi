# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-credential-libsecret
%global full_version 0.5.2
%global pkgname cargo-credential-libsecret-0.5

Name:           rust-cargo-credential-libsecret-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "cargo-credential-libsecret"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:90161b8b1b98a28f0fbdfccafb6adcf2b0be948a4fad3acc31461abf5447debe
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(cargo-credential-0.4/default) >= 0.4.9
Requires:       crate(libloading-0.8/default) >= 0.8.9
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cargo-credential-libsecret"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
