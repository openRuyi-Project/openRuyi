# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-quote
%global full_version 0.6.2
%global pkgname gix-quote-0.6

Name:           rust-gix-quote-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "gix-quote"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:96fc2ff2ec8cc0c92807f02eab1f00eb02619fc2810d13dc42679492fcc36757
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-quote"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
