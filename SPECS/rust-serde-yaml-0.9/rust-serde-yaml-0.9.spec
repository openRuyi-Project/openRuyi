# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_yaml
%global full_version 0.9.34+deprecated
%global pkgname serde-yaml-0.9

Name:           rust-serde-yaml-0.9
Version:        0.9.34
Release:        %autorelease
Summary:        Rust crate "serde_yaml"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/serde-yaml
#!RemoteAsset:  sha256:6a8b1a1a2ebf674015cc02edccce75287f1a0130d394307b36743c2f5d504b47
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-2/default) >= 2.2.1
Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(ryu-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.195
Requires:       crate(unsafe-libyaml-0.2/default) >= 0.2.11
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_yaml"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
