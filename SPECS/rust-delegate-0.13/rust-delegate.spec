# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name delegate
%global full_version 0.13.5
%global pkgname delegate-0.13

Name:           rust-delegate-0.13
Version:        0.13.5
Release:        %autorelease
Summary:        Rust crate "delegate"
License:        MIT OR Apache-2.0
URL:            https://github.com/kobzol/rust-delegate
#!RemoteAsset:  sha256:780eb241654bf097afb00fc5f054a09b687dad862e485fdcf8399bb056565370
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/visit-mut) >= 2.0.117
Provides:       crate(delegate) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "delegate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
