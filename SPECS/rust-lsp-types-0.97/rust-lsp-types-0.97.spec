# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lsp-types
%global full_version 0.97.0
%global pkgname lsp-types-0.97

Name:           rust-lsp-types-0.97
Version:        0.97.0
Release:        %autorelease
Summary:        Rust crate "lsp-types"
License:        MIT
URL:            https://github.com/gluon-lang/lsp-types
#!RemoteAsset:  sha256:53353550a17c04ac46c585feb189c2db82154fc84b79c7a66c96c2c644f66071
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.1
Requires:       crate(fluent-uri-0.1/default) >= 0.1.4
Requires:       crate(serde-1/default) >= 1.0.34
Requires:       crate(serde-1/derive) >= 1.0.34
Requires:       crate(serde-json-1/default) >= 1.0.50
Requires:       crate(serde-repr-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/proposed) = %{version}

%description
Source code for takopackized Rust crate "lsp-types"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
