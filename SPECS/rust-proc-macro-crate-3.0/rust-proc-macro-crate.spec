# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-crate
%global full_version 3.4.0
%global pkgname proc-macro-crate-3.0

Name:           rust-proc-macro-crate-3.0
Version:        3.4.0
Release:        %autorelease
Summary:        Rust crate "proc-macro-crate"
License:        MIT OR Apache-2.0
URL:            https://github.com/bkchr/proc-macro-crate
#!RemoteAsset:  sha256:219cb19e96be00ab2e37d6e299658a0cfa83e52429179969b0f0121b4ac46983
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(toml-edit-0.23/parse) >= 0.23.6
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "proc-macro-crate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
