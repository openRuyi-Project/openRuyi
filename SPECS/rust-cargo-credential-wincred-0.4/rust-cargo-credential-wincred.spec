# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-credential-wincred
%global full_version 0.4.17
%global pkgname cargo-credential-wincred-0.4

Name:           rust-cargo-credential-wincred-0.4
Version:        0.4.17
Release:        %autorelease
Summary:        Rust crate "cargo-credential-wincred"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:c35397b066a83f2e036fb23fca2fb400bfa65e8e8453c21e0b1690cf8250e414
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cargo-credential-0.4/default) >= 0.4.9
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-security-credentials) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cargo-credential-wincred"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
