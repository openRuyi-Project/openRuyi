# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasi
%global full_version 0.11.1+wasi-snapshot-preview1
%global pkgname wasi-0.11

Name:           rust-wasi-0.11
Version:        0.11.1
Release:        %autorelease
Summary:        Rust crate "wasi"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasi
#!RemoteAsset:  sha256:ccf3ec651a847eb01de73ccad15eb7d99f80485de043efb2f370cd654f4ea44b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustc-std-workspace-alloc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "wasi"

%package     -n %{name}+rustc-dep-of-std
Summary:        Experimental WASI API bindings for Rust - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(%{pkgname}/rustc-std-workspace-alloc) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust wasi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
