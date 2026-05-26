# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aligned
%global full_version 0.4.3
%global pkgname aligned-0.4

Name:           rust-aligned-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "aligned"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded-community/aligned
#!RemoteAsset:  sha256:ee4508988c62edf04abd8d92897fca0c2995d907ce1dfeaf369dac3716a40685
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(as-slice-0.2/default) >= 0.2.1
Provides:       crate(aligned) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "aligned"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
