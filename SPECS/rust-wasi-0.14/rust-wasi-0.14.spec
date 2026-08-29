# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasi
%global full_version 0.14.7+wasi-0.2.4
%global pkgname wasi-0.14

Name:           rust-wasi-0.14
Version:        0.14.7
Release:        %autorelease
Summary:        Rust crate "wasi"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasi-rs
#!RemoteAsset:  sha256:883478de20367e224c0090af9cf5f9fa85bed63a95c1abf3afc5c083ebc06e8c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(wasip2-1) >= 1.0.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "wasi"

%package     -n %{name}+bitflags
Summary:        WASI API bindings for Rust - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasip2-1/bitflags) >= 1.0.1
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust wasi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        WASI API bindings for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasip2-1/default) >= 1.0.1
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wasi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        WASI API bindings for Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasip2-1/std) >= 1.0.1
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust wasi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
