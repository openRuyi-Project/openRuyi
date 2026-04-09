# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-normalization
%global full_version 0.1.25
%global pkgname unicode-normalization-0.1

Name:           rust-unicode-normalization-0.1
Version:        0.1.25
Release:        %autorelease
Summary:        Rust crate "unicode-normalization"
License:        MIT OR Apache-2.0
URL:            https://github.com/unicode-rs/unicode-normalization
#!RemoteAsset:  sha256:5fd4f6878c9cb28d874b009da9e8d183b5abc80117c40bbd187a1fde336be6e8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tinyvec-1.0/alloc) >= 1.0.0
Requires:       crate(tinyvec-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "unicode-normalization"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
