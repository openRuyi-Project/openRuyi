# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name webpki-roots
%global full_version 0.26.11
%global pkgname webpki-roots-0.26

Name:           rust-webpki-roots-0.26
Version:        0.26.11
Release:        %autorelease
Summary:        Rust crate "webpki-roots"
License:        CDLA-Permissive-2.0
URL:            https://github.com/rustls/webpki-roots
#!RemoteAsset:  sha256:521bc38abb08001b01866da9f51eb7c5d647a19260e00054a8c7fd5f9e57f7a9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "webpki-roots"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
