# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustc-literal-escaper
%global full_version 0.0.7
%global pkgname rustc-literal-escaper-0.0.7

Name:           rust-rustc-literal-escaper-0.0.7
Version:        0.0.7
Release:        %autorelease
Summary:        Rust crate "rustc-literal-escaper"
License:        Apache-2.0 OR MIT
URL:            https://github.com/rust-lang/literal-escaper
#!RemoteAsset:  sha256:8be87abb9e40db7466e0681dc8ecd9dcfd40360cb10b4c8fe24a7c4c3669b198
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description
Source code for takopackized Rust crate "rustc-literal-escaper"

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
