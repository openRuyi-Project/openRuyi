# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_yml
%global full_version 0.0.13
%global pkgname serde-yml-0.0.13

Name:           rust-serde-yml-0.0.13
Version:        0.0.13
Release:        %autorelease
Summary:        Rust crate "serde_yml"
License:        MIT OR Apache-2.0
URL:            https://github.com/sebastienrousseau/noyalib
#!RemoteAsset:  sha256:909764a65f86829ccdb5eea9ab355843aa02c019a7bfd47465092953565caa05
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(noyalib-0.0.5/compat-serde-yaml) >= 0.0.5
Requires:       crate(noyalib-0.0.5/std) >= 0.0.5
Requires:       crate(serde-1/default) >= 1.0.204

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
This release is a thin compatibility shim that forwards every call to `noyalib` (a pure-Rust, `#![forbid(unsafe_code)]` YAML library). Please migrate to `noyalib`.
Source code for takopackized Rust crate "serde_yml"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
