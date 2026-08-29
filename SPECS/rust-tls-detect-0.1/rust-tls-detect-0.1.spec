# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tls-detect
%global full_version 0.1.0
%global pkgname tls-detect-0.1

Name:           rust-tls-detect-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "tls-detect"
License:        Apache-2.0
URL:            https://github.com/alexliesenfeld/tls-detect-rs
#!RemoteAsset:  sha256:3e1800cba3e521412d15e88358ddda292fa8f157f06a66a418fed5e1b8ecb166
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.0.0/default) >= 0.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tls-detect"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
