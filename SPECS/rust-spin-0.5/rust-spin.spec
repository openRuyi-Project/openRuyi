# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name spin
%global full_version 0.5.2
%global pkgname spin-0.5

Name:           rust-spin-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "spin"
License:        MIT
URL:            https://github.com/mvdnes/spin-rs.git
#!RemoteAsset:  sha256:6e63cff320ae2c57904679ba7cb63280a3dc4613885beafb148ee7bf9aa9042d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(spin) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
They may contain data, are usable without `std`, and static initializers are available.
Source code for takopackized Rust crate "spin"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
