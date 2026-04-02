# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name foldhash
%global full_version 0.2.0
%global pkgname foldhash-0.2

Name:           rust-foldhash-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "foldhash"
License:        Zlib
URL:            https://github.com/orlp/foldhash
#!RemoteAsset:  sha256:77ce24cb58228fbb8aa041425bb1050850ac19177686ea6e0f41a70416f56fdb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "foldhash"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
