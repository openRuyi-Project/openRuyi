# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tree-sitter
%global full_version 0.26.8
%global pkgname tree-sitter-0.26

Name:           rust-tree-sitter-0.26
Version:        0.26.8
Release:        %autorelease
Summary:        Rust crate "tree-sitter"
License:        MIT
URL:            https://tree-sitter.github.io/tree-sitter
#!RemoteAsset:  sha256:887bd495d0582c5e3e0d8ece2233666169fa56a9644d172fc22ad179ab2d0538
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.2.48
Requires:       crate(regex-1/unicode) >= 1.11.3
Requires:       crate(regex-syntax-0.8) >= 0.8.6
Requires:       crate(serde-json-1) >= 1.0.145
Requires:       crate(serde-json-1/preserve-order) >= 1.0.145
Requires:       crate(streaming-iterator-0.1/default) >= 0.1.9
Requires:       crate(tree-sitter-language-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tree-sitter"

%package     -n %{name}+bindgen
Summary:        Rust bindings to the Tree-sitter parsing library - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.72/default) >= 0.72.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust tree-sitter crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Rust bindings to the Tree-sitter parsing library - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/perf) >= 1.11.3
Requires:       crate(regex-1/std) >= 1.11.3
Requires:       crate(regex-1/unicode) >= 1.11.3
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.6
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust tree-sitter crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+wasm
Summary:        Rust bindings to the Tree-sitter parsing library - feature "wasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/wasmtime-c-api) = %{version}
Provides:       crate(%{pkgname}/wasm) = %{version}

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust tree-sitter crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasmtime-c-api
Summary:        Rust bindings to the Tree-sitter parsing library - feature "wasmtime-c-api"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasmtime-c-api-impl-36/cranelift) >= 36.0.6
Requires:       crate(wasmtime-c-api-impl-36/gc-drc) >= 36.0.6
Provides:       crate(%{pkgname}/wasmtime-c-api) = %{version}

%description -n %{name}+wasmtime-c-api
This metapackage enables feature "wasmtime-c-api" for the Rust tree-sitter crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
