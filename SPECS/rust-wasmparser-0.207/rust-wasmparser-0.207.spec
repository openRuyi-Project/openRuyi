# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasmparser
%global full_version 0.207.0
%global pkgname wasmparser-0.207

Name:           rust-wasmparser-0.207
Version:        0.207.0
Release:        %autorelease
Summary:        Rust crate "wasmparser"
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/bytecodealliance/wasm-tools/tree/main/crates/wasmparser
#!RemoteAsset:  sha256:e19bb9f8ab07616da582ef8adb24c54f1424c7ec876720b7da9db8ec0626c92c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "wasmparser"

%package     -n %{name}+default
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/validate) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+validate
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "validate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ahash-0.8) >= 0.8.11
Requires:       crate(hashbrown-0.14/ahash) >= 0.14.3
Requires:       crate(indexmap-2) >= 2.0.0
Requires:       crate(semver-1) >= 1.0.0
Provides:       crate(%{pkgname}/validate) = %{version}

%description -n %{name}+validate
This metapackage enables feature "validate" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
