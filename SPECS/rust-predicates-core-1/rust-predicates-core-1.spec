# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name predicates-core
%global full_version 1.0.10
%global pkgname predicates-core-1

Name:           rust-predicates-core-1
Version:        1.0.10
Release:        %autorelease
Summary:        Rust crate "predicates-core"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/predicates-rs
#!RemoteAsset:  sha256:cad38746f3166b4031b1a0d39ad9f954dd291e7854fcc0eed52ee41a0b50d144
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "predicates-core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
