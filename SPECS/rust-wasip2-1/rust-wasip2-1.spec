# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasip2
%global full_version 1.0.3+wasi-0.2.9
%global pkgname wasip2-1

Name:           rust-wasip2-1
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "wasip2"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasi-rs
#!RemoteAsset:  sha256:20064672db26d7cdc89c7798c48a0fdfac8213434a1186e5ef29fd560ae223d6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(wit-bindgen-0.57) >= 0.57.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "wasip2"

%package     -n %{name}+bitflags
Summary:        WASIp2 API bindings for Rust - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wit-bindgen-0.57/bitflags) >= 0.57.1
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust wasip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        WASIp2 API bindings for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wasip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        WASIp2 API bindings for Rust - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(wit-bindgen-0.57/rustc-dep-of-std) >= 0.57.1
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust wasip2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
