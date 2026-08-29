# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.58
Requires:       crate(indexmap-2/serde) >= 2.7.0
Requires:       crate(wasm-encoder-0.244/component-model) >= 0.244.0
Requires:       crate(wasm-encoder-0.244/std) >= 0.244.0
Requires:       crate(wasmparser-0.244/component-model) >= 0.244.0
Requires:       crate(wasmparser-0.244/hash-collections) >= 0.244.0
Requires:       crate(wasmparser-0.244/simd) >= 0.244.0
Requires:       crate(wasmparser-0.244/std) >= 0.244.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "wasm-metadata"

%package     -n %{name}+clap
Summary:        Read and manipulate WebAssembly metadata - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.0.0
Requires:       crate(clap-4/derive) >= 4.0.0
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust wasm-metadata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Read and manipulate WebAssembly metadata - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/oci) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wasm-metadata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oci
Summary:        Read and manipulate WebAssembly metadata - feature "oci"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(auditable-serde-0.8/default) >= 0.8.0
Requires:       crate(flate2-1/default) >= 1.1.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(spdx-0.10/default) >= 0.10.1
Requires:       crate(url-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/oci) = %{version}

%description -n %{name}+oci
This metapackage enables feature "oci" for the Rust wasm-metadata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Read and manipulate WebAssembly metadata - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.166
Requires:       crate(serde-derive-1/default) >= 1.0.166
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wasm-metadata crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
