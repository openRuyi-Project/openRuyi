# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_norway
%global full_version 0.9.42
%global pkgname serde-norway-0.9

Name:           rust-serde-norway-0.9
Version:        0.9.42
Release:        %autorelease
Summary:        Rust crate "serde_norway"
License:        MIT OR Apache-2.0
URL:            https://github.com/cafkafk/serde-yaml
#!RemoteAsset:  sha256:e408f29489b5fd500fab51ff1484fc859bb655f32c671f307dcd733b72e8168c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-2/default) >= 2.2.1
Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(ryu-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.203
Requires:       crate(unsafe-libyaml-norway-0.2/default) >= 0.2.13

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_norway"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
