# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wit-component
%global full_version 0.244.0
%global pkgname wit-component-0.244

Name:           rust-wit-component-0.244
Version:        0.244.0
Release:        %autorelease
Summary:        Rust crate "wit-component"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasm-tools/tree/main/crates/wit-component
#!RemoteAsset:  sha256:9d66ea20e9553b30172b5e831994e35fbde2d165325bec84fc43dbf6f4eb9cb2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(indexmap-2.0) >= 2.13.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Requires:       crate(serde-derive-1.0/default) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(wasm-encoder-0.244/std) >= 0.244.0
Requires:       crate(wasm-encoder-0.244/wasmparser) >= 0.244.0
Requires:       crate(wasm-metadata-0.244) >= 0.244.0
Requires:       crate(wasmparser-0.244/component-model) >= 0.244.0
Requires:       crate(wasmparser-0.244/simd) >= 0.244.0
Requires:       crate(wasmparser-0.244/std) >= 0.244.0
Requires:       crate(wit-parser-0.244/decoding) >= 0.244.0
Requires:       crate(wit-parser-0.244/default) >= 0.244.0
Requires:       crate(wit-parser-0.244/serde) >= 0.244.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wit-component"

%package     -n %{name}+dummy-module
Summary:        Tooling for working with `*.wit` and component files together - feature "dummy-module" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(wat-1.0) >= 1.244.0
Provides:       crate(%{pkgname}/dummy-module)
Provides:       crate(%{pkgname}/semver-check)

%description -n %{name}+dummy-module
This metapackage enables feature "dummy-module" for the Rust wit-component crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "semver-check" feature.

%package     -n %{name}+wat
Summary:        Tooling for working with `*.wit` and component files together - feature "wat"
Requires:       crate(%{pkgname})
Requires:       crate(wast-244.0) >= 244.0.0
Requires:       crate(wat-1.0) >= 1.244.0
Provides:       crate(%{pkgname}/wat)

%description -n %{name}+wat
This metapackage enables feature "wat" for the Rust wit-component crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
