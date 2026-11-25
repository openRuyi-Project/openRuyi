# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qapi-spec
%global full_version 0.3.2
%global pkgname qapi-spec-0.3

Name:           rust-qapi-spec-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "qapi-spec"
License:        MIT
URL:            https://github.com/arcnmx/qapi-rs
#!RemoteAsset:  sha256:49e6bdbbe5d13015b21a49a778a29ae3cee9c450c3154e1648aed670d57fe5ba
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(serde-1/default) >= 1.0.27
Requires:       crate(serde-1/derive) >= 1.0.27
Requires:       crate(serde-json-1/default) >= 1.0.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qapi-spec"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
