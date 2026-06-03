# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name webpki-roots
%global full_version 1.0.5
%global pkgname webpki-roots-1.0

Name:           rust-webpki-roots-1.0
Version:        1.0.5
Release:        %autorelease
Summary:        Rust crate "webpki-roots"
License:        CDLA-Permissive-2.0
URL:            https://github.com/rustls/webpki-roots
#!RemoteAsset:  sha256:12bed680863276c63889429bfd6cab3b99943659923822de1c8a39c49e4d722c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustls-pki-types-1.0) >= 1.13.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "webpki-roots"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
