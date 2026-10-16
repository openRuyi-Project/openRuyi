# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name deunicode
%global full_version 1.6.2
%global pkgname deunicode-1

Name:           rust-deunicode-1
Version:        1.6.2
Release:        %autorelease
Summary:        Rust crate "deunicode"
License:        BSD-3-Clause
URL:            https://lib.rs/crates/deunicode
#!RemoteAsset:  sha256:abd57806937c9cc163efc8ea3910e00a62e2aeb0b8119f1793a978088f8f6b04
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Suppors Emoji and Chinese.
Source code for takopackized Rust crate "deunicode"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
