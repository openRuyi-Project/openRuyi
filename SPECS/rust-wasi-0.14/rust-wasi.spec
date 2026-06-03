# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasi
%global full_version 0.14.2+wasi-0.2.4
%global pkgname wasi-0.14

Name:           rust-wasi-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "wasi"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasi-rs
#!RemoteAsset:  sha256:9683f9a5a998d873c0d21fcbe3c083009670149a8fab228644b8bd36b2c48cb3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(wit-bindgen-rt-0.39/bitflags) >= 0.39.0
Requires:       crate(wit-bindgen-rt-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "wasi"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
