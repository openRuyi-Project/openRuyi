# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-encoder
%global full_version 0.244.0
%global pkgname wasm-encoder-0.244

Name:           rust-wasm-encoder-0.244
Version:        0.244.0
Release:        %autorelease
Summary:        Rust crate "wasm-encoder"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasm-tools/tree/main/crates/wasm-encoder
#!RemoteAsset:  sha256:990065f2fe63003fe337b932cfb5e3b80e0b4d0f5ff650e6985b1048f62c8319
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(leb128fmt-0.1) >= 0.1.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "wasm-encoder"

%package     -n %{name}+component-model
Summary:        Low-level WebAssembly encoder - feature "component-model"
Requires:       crate(%{pkgname})
Requires:       crate(wasmparser-0.244/component-model) >= 0.244.0
Requires:       crate(wasmparser-0.244/simd) >= 0.244.0
Provides:       crate(%{pkgname}/component-model)

%description -n %{name}+component-model
This metapackage enables feature "component-model" for the Rust wasm-encoder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Low-level WebAssembly encoder - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/component-model)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wasm-encoder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Low-level WebAssembly encoder - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(wasmparser-0.244/simd) >= 0.244.0
Requires:       crate(wasmparser-0.244/std) >= 0.244.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust wasm-encoder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasmparser
Summary:        Low-level WebAssembly encoder - feature "wasmparser"
Requires:       crate(%{pkgname})
Requires:       crate(wasmparser-0.244/simd) >= 0.244.0
Provides:       crate(%{pkgname}/wasmparser)

%description -n %{name}+wasmparser
This metapackage enables feature "wasmparser" for the Rust wasm-encoder crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
