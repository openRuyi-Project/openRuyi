# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name riscv-types
%global full_version 0.1.0
%global pkgname riscv-types-0.1

Name:           rust-riscv-types-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "riscv-types"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded/riscv
#!RemoteAsset:  sha256:d3f2ad9f15a07f4a0e1677124f9120ce7e83ab7e1ca7186af0ca9da529b62e80
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "riscv-types"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
