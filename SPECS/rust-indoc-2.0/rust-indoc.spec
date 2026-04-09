# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name indoc
%global full_version 2.0.7
%global pkgname indoc-2.0

Name:           rust-indoc-2.0
Version:        2.0.7
Release:        %autorelease
Summary:        Rust crate "indoc"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/indoc
#!RemoteAsset:  sha256:79cf5c93f93228cf8efb3ba362535fb11199ac548a09ce117c9b1adc3030d706
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustversion-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "indoc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
