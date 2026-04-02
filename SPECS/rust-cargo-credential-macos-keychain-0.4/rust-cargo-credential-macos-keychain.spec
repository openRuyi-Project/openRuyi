# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-credential-macos-keychain
%global full_version 0.4.17
%global pkgname cargo-credential-macos-keychain-0.4

Name:           rust-cargo-credential-macos-keychain-0.4
Version:        0.4.17
Release:        %autorelease
Summary:        Rust crate "cargo-credential-macos-keychain"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:e95b9c2431165b30ea111f2933ed6799bfa9a66c9503046064cf8f001960ea1b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cargo-credential-0.4/default) >= 0.4.9
Requires:       crate(security-framework-3.0/default) >= 3.7.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cargo-credential-macos-keychain"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
