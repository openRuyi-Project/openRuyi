# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name deltae
%global full_version 0.3.2
%global pkgname deltae-0.3

Name:           rust-deltae-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "deltae"
License:        MIT
URL:            https://gitlab.com/ryanobeirne/deltae
#!RemoteAsset:  sha256:5729f5117e208430e437df2f4843f5e5952997175992d1414f94c57d61e270b4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(deltae) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "deltae"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
