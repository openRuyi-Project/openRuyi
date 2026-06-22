# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name foreign-types-shared
%global full_version 0.3.1
%global pkgname foreign-types-shared-0.3

Name:           rust-foreign-types-shared-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "foreign-types-shared"
License:        MIT OR Apache-2.0
URL:            https://github.com/sfackler/foreign-types
#!RemoteAsset:  sha256:aa9a19cbb55df58761df49b23516a86d432839add4af60fc256da840f66ed35b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "foreign-types-shared"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
