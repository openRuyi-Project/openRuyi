# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name color_quant
%global full_version 1.1.0
%global pkgname color-quant-1.0

Name:           rust-color-quant-1.0
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "color_quant"
License:        MIT
URL:            https://github.com/image-rs/color_quant.git
#!RemoteAsset:  sha256:3d7b894f5411737b7867f4827955924d7c254fc9f4d91a6aad6b097804b1018b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(color-quant) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "color_quant"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
