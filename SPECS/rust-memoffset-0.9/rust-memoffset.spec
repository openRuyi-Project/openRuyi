# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memoffset
%global full_version 0.9.1
%global pkgname memoffset-0.9

Name:           rust-memoffset-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "memoffset"
License:        MIT
URL:            https://github.com/Gilnaa/memoffset
#!RemoteAsset:  sha256:488016bfae457b036d996092f6cb448677611ce4449e970ceaf42695203f218a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/unstable-const)
Provides:       crate(%{pkgname}/unstable-offset-of)

%description
Source code for takopackized Rust crate "memoffset"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
