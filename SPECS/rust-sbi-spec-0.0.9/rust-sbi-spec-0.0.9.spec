# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sbi-spec
%global full_version 0.0.9
%global pkgname sbi-spec-0.0.9

Name:           rust-sbi-spec-0.0.9
Version:        0.0.9
Release:        %autorelease
Summary:        Rust crate "sbi-spec"
License:        MulanPSL-2.0 OR MIT
URL:            https://github.com/rustsbi/rustsbi
#!RemoteAsset:  sha256:785b91fcc41c7426fc07510be49ed1db44f002b45d45c175ec7f155c3cd447a9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.11.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/legacy) = %{version}

%description
Source code for takopackized Rust crate "sbi-spec"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
