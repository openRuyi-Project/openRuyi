# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/features)
Provides:       crate(%{pkgname}/prefer-btree-collections)
Provides:       crate(%{pkgname}/simd)
Provides:       crate(%{pkgname}/validate)

%description
Source code for takopackized Rust crate "wasmparser"

%package     -n %{name}+component-model
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "component-model"
Requires:       crate(%{pkgname})
Requires:       crate(semver-1.0) >= 1.0.27
Provides:       crate(%{pkgname}/component-model)

%description -n %{name}+component-model
This metapackage enables feature "component-model" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/component-model)
Requires:       crate(%{pkgname}/features)
Requires:       crate(%{pkgname}/hash-collections)
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/simd)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/validate)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hash-collections
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "hash-collections"
Requires:       crate(%{pkgname})
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.5
Requires:       crate(indexmap-2.0) >= 2.13.0
Provides:       crate(%{pkgname}/hash-collections)

%description -n %{name}+hash-collections
This metapackage enables feature "hash-collections" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.5
Requires:       crate(hashbrown-0.15/serde) >= 0.15.5
Requires:       crate(indexmap-2.0/serde) >= 2.13.0
Requires:       crate(serde-1.0/alloc) >= 1.0.166
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Simple event-driven library for parsing WebAssembly binary files - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/std) >= 2.13.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust wasmparser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
