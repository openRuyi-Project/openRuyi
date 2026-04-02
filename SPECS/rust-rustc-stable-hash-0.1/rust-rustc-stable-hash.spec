# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustc-stable-hash
%global full_version 0.1.2
%global pkgname rustc-stable-hash-0.1

Name:           rust-rustc-stable-hash-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "rustc-stable-hash"
License:        Apache-2.0 OR MIT
URL:            https://github.com/rust-lang/rustc-stable-hash
#!RemoteAsset:  sha256:781442f29170c5c93b7185ad559492601acdc71d5bb0706f5868094f45cfcd08
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)

%description
Source code for takopackized Rust crate "rustc-stable-hash"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
