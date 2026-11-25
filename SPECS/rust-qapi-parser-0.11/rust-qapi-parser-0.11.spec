# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qapi-parser
%global full_version 0.11.0
%global pkgname qapi-parser-0.11

Name:           rust-qapi-parser-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "qapi-parser"
License:        MIT
URL:            https://github.com/arcnmx/qapi-rs
#!RemoteAsset:  sha256:7b37f643cfdf67a409a9323334138a11636a5db5d56cedcc780d7a82a7fb7659
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.27
Requires:       crate(serde-1/derive) >= 1.0.27
Requires:       crate(serde-json-1/default) >= 1.0.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qapi-parser"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
