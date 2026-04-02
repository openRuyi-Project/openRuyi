# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-hashtable
%global full_version 0.9.0
%global pkgname gix-hashtable-0.9

Name:           rust-gix-hashtable-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "gix-hashtable"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:c35300b54896153e55d53f4180460931ccd69b7e8d2f6b9d6401122cdedc4f07
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(hashbrown-0.15/inline-more) >= 0.15.5
Requires:       crate(parking-lot-0.12/default) >= 0.12.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-hashtable"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
