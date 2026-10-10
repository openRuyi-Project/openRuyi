# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name riscv-decode
%global full_version 0.2.3
%global pkgname riscv-decode-0.2

Name:           rust-riscv-decode-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "riscv-decode"
License:        MIT OR Apache-2.0
URL:            https://github.com/fintelia/riscv-decode
#!RemoteAsset:  sha256:68b59d645e392e041ad18f5e529ed13242d8405c66bb192f59703ea2137017d0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "riscv-decode"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
