# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytemuck_derive
%global full_version 1.10.2
%global pkgname bytemuck-derive-1.0

Name:           rust-bytemuck-derive-1.0
Version:        1.10.2
Release:        %autorelease
Summary:        Rust crate "bytemuck_derive"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/Lokathor/bytemuck
#!RemoteAsset:  sha256:f9abbd1bc6865053c427f7198e6af43bfdedc55ab791faed4fbd361d789575ff
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Provides:       crate(bytemuck-derive) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "bytemuck_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
