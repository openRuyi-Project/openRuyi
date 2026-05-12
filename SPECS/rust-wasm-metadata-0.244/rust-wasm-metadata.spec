# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-metadata
%global full_version 0.244.0
%global pkgname wasm-metadata-0.244

Name:           rust-wasm-metadata-0.244
Version:        0.244.0
Release:        %autorelease
Summary:        Rust crate "wasm-metadata"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasm-tools/tree/main/crates/wasm-metadata
#!RemoteAsset:  sha256:bb0e353e6a2fbdc176932bbaab493762eb1255a7900fe0fea1a2f96c296cc909
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(indexmap-2.0/serde) >= 2.13.0
Requires:       crate(wasm-encoder-0.244/component-model) >= 0.244.0
Requires:       crate(wasm-encoder-0.244/std) >= 0.244.0
Requires:       crate(wasmparser-0.244/component-model) >= 0.244.0
Requires:       crate(wasmparser-0.244/hash-collections) >= 0.244.0
Requires:       crate(wasmparser-0.244/simd) >= 0.244.0
Requires:       crate(wasmparser-0.244/std) >= 0.244.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "wasm-metadata"

%package     -n %{name}+clap
Summary:        Read and manipulate WebAssembly metadata - feature "clap"
Requires:       crate(%{pkgname})
Requires:       crate(clap-4.0/default) >= 4.0.0
Requires:       crate(clap-4.0/derive) >= 4.0.0
Provides:       crate(%{pkgname}/clap)

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust wasm-metadata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Read and manipulate WebAssembly metadata - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/oci)
Requires:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wasm-metadata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oci
Summary:        Read and manipulate WebAssembly metadata - feature "oci"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(auditable-serde-0.8/default) >= 0.8.0
Requires:       crate(flate2-1.0/default) >= 1.1.0
Requires:       crate(serde-json-1.0/default) >= 1.0.0
Requires:       crate(spdx-0.10/default) >= 0.10.1
Requires:       crate(url-2.0/default) >= 2.0.0
Provides:       crate(%{pkgname}/oci)

%description -n %{name}+oci
This metapackage enables feature "oci" for the Rust wasm-metadata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Read and manipulate WebAssembly metadata - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/alloc) >= 1.0.166
Requires:       crate(serde-derive-1.0/default) >= 1.0.166
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wasm-metadata crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
