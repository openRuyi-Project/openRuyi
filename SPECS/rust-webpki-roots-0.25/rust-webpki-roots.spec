# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name webpki-roots
%global full_version 0.25.4
%global pkgname webpki-roots-0.25

Name:           rust-webpki-roots-0.25
Version:        0.25.4
Release:        %autorelease
Summary:        Rust crate "webpki-roots"
License:        MPL-2.0
URL:            https://github.com/rustls/webpki-roots
#!RemoteAsset:  sha256:5f20c57d8d7db6d3b86154206ae5d8fba62dd39573114de97c2cb0578251f8e1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(webpki-roots) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "webpki-roots"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
