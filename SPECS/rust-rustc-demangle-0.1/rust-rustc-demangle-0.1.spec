# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustc-demangle
%global full_version 0.1.27
%global pkgname rustc-demangle-0.1

Name:           rust-rustc-demangle-0.1
Version:        0.1.27
Release:        %autorelease
Summary:        Rust crate "rustc-demangle"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/rustc-demangle
#!RemoteAsset:  sha256:b50b8869d9fc858ce7266cce0194bd74df58b9d0e3f6df3a9fc8eb470d95c09d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compiler-builtins) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "rustc-demangle"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
