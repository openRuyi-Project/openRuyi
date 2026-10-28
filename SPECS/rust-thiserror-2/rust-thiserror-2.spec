# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thiserror
%global full_version 2.0.20
%global pkgname thiserror-2

Name:           rust-thiserror-2
Version:        2.0.20
Release:        %autorelease
Summary:        Rust crate "thiserror"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/thiserror
#!RemoteAsset:  sha256:ec86235f5fcc2a73650310756d2ac5b138a5780bbbdfae3eeccec992c435ba4f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thiserror-impl-2/default) >= 2.0.20

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "thiserror"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
