# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name chunked_transfer
%global full_version 1.0.0
%global pkgname chunked-transfer-1.0

Name:           rust-chunked-transfer-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "chunked_transfer"
License:        Apache-2.0
URL:            https://github.com/frewsxcv/rust-chunked-transfer
#!RemoteAsset:  sha256:f98beb6554de08a14bd7b5c6014963c79d6a25a1c66b1d4ecb9e733ccba51d6c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(chunked-transfer) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "chunked_transfer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
