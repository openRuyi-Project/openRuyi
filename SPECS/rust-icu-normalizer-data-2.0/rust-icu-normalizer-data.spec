# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_normalizer_data
%global full_version 2.2.0
%global pkgname icu-normalizer-data-2.0

Name:           rust-icu-normalizer-data-2.0
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "icu_normalizer_data"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:da3be0ae77ea334f4da67c12f149704f19f81d1adf7c51cf482943e84a2bad38
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "icu_normalizer_data"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
