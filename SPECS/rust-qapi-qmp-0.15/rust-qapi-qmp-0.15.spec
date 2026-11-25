# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qapi-qmp
%global full_version 0.15.0
%global pkgname qapi-qmp-0.15

Name:           rust-qapi-qmp-0.15
Version:        0.15.0
Release:        %autorelease
Summary:        Rust crate "qapi-qmp"
License:        MIT
URL:            https://github.com/arcnmx/qapi-rs
#!RemoteAsset:  sha256:45303cac879d89361cad0287ae15f9ae1e7799b904b474152414aeece39b9875
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(qapi-codegen-0.11) >= 0.11.1
Requires:       crate(qapi-spec-0.3/default) >= 0.3.0
Requires:       crate(serde-1/default) >= 1.0.27
Requires:       crate(serde-1/derive) >= 1.0.27

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qapi-qmp"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
