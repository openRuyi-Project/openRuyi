# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qapi-codegen
%global full_version 0.11.3
%global pkgname qapi-codegen-0.11

Name:           rust-qapi-codegen-0.11
Version:        0.11.3
Release:        %autorelease
Summary:        Rust crate "qapi-codegen"
License:        MIT
URL:            https://github.com/arcnmx/qapi-rs
#!RemoteAsset:  sha256:fb959fed63a69baa2e3ae57224d885e686bc3f56c9bb3b03406969980ea57a44
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(qapi-parser-0.11/default) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qapi-codegen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
