# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name codspeed
%global full_version 2.10.1
%global pkgname codspeed-2.0

Name:           rust-codspeed-2.0
Version:        2.10.1
Release:        %autorelease
Summary:        Rust crate "codspeed"
License:        MIT OR Apache-2.0
URL:            https://codspeed.io
#!RemoteAsset:  sha256:93f4cce9c27c49c4f101fffeebb1826f41a9df2e7498b7cd4d95c0658b796c6c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(colored-2.0/default) >= 2.2.0
Requires:       crate(libc-0.2/default) >= 0.2.185
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(uuid-1.0/default) >= 1.23.1
Requires:       crate(uuid-1.0/v4) >= 1.23.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "codspeed"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
