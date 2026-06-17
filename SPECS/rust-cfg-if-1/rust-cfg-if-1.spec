# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cfg-if
%global full_version 1.0.4
%global pkgname cfg-if-1

Name:           rust-cfg-if-1
Version:        1.0.4
Release:        %autorelease
Summary:        Rust crate "cfg-if"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cfg-if
#!RemoteAsset:  sha256:9330f8b2ff13f34540b44e946ef35111825727b38d33286ef986142615121801
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description
Structured like an if-else chain, the first matching branch is the item that gets emitted.
Source code for takopackized Rust crate "cfg-if"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
