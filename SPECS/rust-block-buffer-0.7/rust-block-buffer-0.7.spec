# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name block-buffer
%global full_version 0.7.3
%global pkgname block-buffer-0.7

Name:           rust-block-buffer-0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Rust crate "block-buffer"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/utils
#!RemoteAsset:  sha256:c0940dc441f31689269e10ac70eb1002a3a1d3ad1390e030043662eb7fe4688b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(block-padding-0.1/default) >= 0.1.0
Requires:       crate(byte-tools-0.3/default) >= 0.3.0
Requires:       crate(byteorder-1) >= 1.1.0
Requires:       crate(generic-array-0.12/default) >= 0.12.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "block-buffer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
