# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name minimal-lexical
%global full_version 0.2.1
%global pkgname minimal-lexical-0.2

Name:           rust-minimal-lexical-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "minimal-lexical"
License:        MIT/Apache-2.0
URL:            https://github.com/Alexhuszagh/minimal-lexical
#!RemoteAsset:  sha256:68354c5c6bd36d73ff3feceb05efa59b6acb7626617f4962be322a825e61f79a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/compact)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/lint)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "minimal-lexical"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
