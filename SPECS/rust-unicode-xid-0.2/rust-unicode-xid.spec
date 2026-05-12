# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-xid
%global full_version 0.2.6
%global pkgname unicode-xid-0.2

Name:           rust-unicode-xid-0.2
Version:        0.2.6
Release:        %autorelease
Summary:        Rust crate "unicode-xid"
License:        MIT OR Apache-2.0
URL:            https://github.com/unicode-rs/unicode-xid
#!RemoteAsset:  sha256:ebc1c04c71510c7f702b52b7c350734c9ff1295c464a03335b00bb84fc54f853
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/bench)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/no-std)

%description
Source code for takopackized Rust crate "unicode-xid"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
