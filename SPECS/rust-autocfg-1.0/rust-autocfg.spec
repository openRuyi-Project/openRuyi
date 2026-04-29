# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name autocfg
%global full_version 1.0.1
%global pkgname autocfg-1.0

Name:           rust-autocfg-1.0
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "autocfg"
License:        Apache-2.0 OR MIT
URL:            https://github.com/cuviper/autocfg
#!RemoteAsset:  sha256:cdb031dd78e28731d87d56cc8ffef4a8f36ca26c38fe2de700543e627f8a464a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "autocfg"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
