# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tinytemplate
%global full_version 1.2.1
%global pkgname tinytemplate-1.0

Name:           rust-tinytemplate-1.0
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "tinytemplate"
License:        Apache-2.0 OR MIT
URL:            https://github.com/bheisler/TinyTemplate
#!RemoteAsset:  sha256:be4d6b5f19ff7664e8c98d03e2139cb510db9b0a60b55f8e8709b689d939b6bc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "tinytemplate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
