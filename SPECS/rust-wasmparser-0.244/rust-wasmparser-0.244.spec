# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasmparser
%global full_version 0.244.0
%global pkgname wasmparser-0.244

Name:           rust-wasmparser-0.244
Version:        0.244.0
Release:        %autorelease
Summary:        Rust crate "wasmparser"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasm-tools/tree/main/crates/wasmparser
#!RemoteAsset:  sha256:47b807c72e1bac69382b3a6fb3dbe8ea4c0ed87ff5629b8685ae6b9a611028fe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/features) = %{version}
Provides:       crate(%{pkgname}/prefer-btree-collections) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/validate) = %{version}

%description
Source code for takopackized Rust crate "wasmparser"

%package     -n %{name}+component-model
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "component-model"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(semver-1) >= 1.0.0
Provides:       crate(%{pkgname}/component-model) = %{version}

%description -n %{name}+component-model
This metapackage enables feature "component-model" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/component-model) = %{version}
Requires:       crate(%{pkgname}/features) = %{version}
Requires:       crate(%{pkgname}/hash-collections) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/simd) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/validate) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hash-collections
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "hash-collections"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.2
Requires:       crate(indexmap-2) >= 2.7.0
Provides:       crate(%{pkgname}/hash-collections) = %{version}

%description -n %{name}+hash-collections
This metapackage enables feature "hash-collections" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.2
Requires:       crate(hashbrown-0.15/serde) >= 0.15.2
Requires:       crate(indexmap-2/serde) >= 2.7.0
Requires:       crate(serde-1/alloc) >= 1.0.166
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/std) >= 2.7.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
