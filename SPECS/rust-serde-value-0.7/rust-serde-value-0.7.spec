# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde-value
%global full_version 0.7.0
%global pkgname serde-value-0.7

Name:           rust-serde-value-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "serde-value"
License:        MIT
URL:            https://github.com/arcnmx/serde-value
#!RemoteAsset:  sha256:f3a1a3341211875ef120e117ea7fd5228530ae7e7036a779fdc9117be6b3282c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ordered-float-2/default) >= 2.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde-value"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
