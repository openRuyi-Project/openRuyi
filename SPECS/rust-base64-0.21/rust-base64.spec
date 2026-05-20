# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name base64
%global full_version 0.21.7
%global pkgname base64-0.21

Name:           rust-base64-0.21
Version:        0.21.7
Release:        %autorelease
Summary:        Rust crate "base64"
License:        MIT OR Apache-2.0
URL:            https://github.com/marshallpierce/rust-base64
#!RemoteAsset:  sha256:9d297deb1925b89f2ccc13d7635fa0714f12c87adce1c75356b39ca9b7178567
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(base64) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "base64"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
