# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name untrusted
%global full_version 0.9.0
%global pkgname untrusted-0.9

Name:           rust-untrusted-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "untrusted"
License:        ISC
URL:            https://github.com/briansmith/untrusted
#!RemoteAsset:  sha256:8ecb6da28b8a351d773b68d5825ac39017e680750f980f3a1a85cd8dd28a47c1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "untrusted"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
