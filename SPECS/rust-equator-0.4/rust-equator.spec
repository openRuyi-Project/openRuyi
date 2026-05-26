# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name equator
%global full_version 0.4.2
%global pkgname equator-0.4

Name:           rust-equator-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "equator"
License:        MIT
URL:            https://github.com/sarah-ek/equator/
#!RemoteAsset:  sha256:4711b213838dfee0117e3be6ac926007d7f433d7bbe33595975d4190cb07e6fc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(equator-macro-0.4/default) >= 0.4.2
Provides:       crate(equator) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "equator"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
