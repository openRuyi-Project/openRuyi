# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wit-parser
%global full_version 0.244.0
%global pkgname wit-parser-0.244

Name:           rust-wit-parser-0.244
Version:        0.244.0
Release:        %autorelease
Summary:        Rust crate "wit-parser"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasm-tools/tree/main/crates/wit-parser
#!RemoteAsset:  sha256:ecc8ac4bc1dc3381b7f59c34f00b67e18f910c2c0f50015669dde7def656a736
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(id-arena-2.0/default) >= 2.3.0
Requires:       crate(indexmap-2.0/std) >= 2.13.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(semver-1.0) >= 1.0.27
Requires:       crate(unicode-xid-0.2/default) >= 0.2.6
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "wit-parser"

%package     -n %{name}+decoding
Summary:        Tooling for parsing `*.wit` files and working with their contents - feature "decoding"
Requires:       crate(%{pkgname})
Requires:       crate(wasmparser-0.244/component-model) >= 0.244.0
Requires:       crate(wasmparser-0.244/features) >= 0.244.0
Requires:       crate(wasmparser-0.244/simd) >= 0.244.0
Requires:       crate(wasmparser-0.244/std) >= 0.244.0
Requires:       crate(wasmparser-0.244/validate) >= 0.244.0
Provides:       crate(%{pkgname}/decoding)

%description -n %{name}+decoding
This metapackage enables feature "decoding" for the Rust wit-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Tooling for parsing `*.wit` files and working with their contents - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/decoding)
Requires:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust wit-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Tooling for parsing `*.wit` files and working with their contents - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde-json)
Requires:       crate(indexmap-2.0/serde) >= 2.13.0
Requires:       crate(indexmap-2.0/std) >= 2.13.0
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Requires:       crate(serde-derive-1.0/default) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wit-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Tooling for parsing `*.wit` files and working with their contents - feature "serde_json"
Requires:       crate(%{pkgname})
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Provides:       crate(%{pkgname}/serde-json)

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust wit-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wat
Summary:        Tooling for parsing `*.wit` files and working with their contents - feature "wat"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/decoding)
Requires:       crate(wat-1.0/component-model) >= 1.244.0
Provides:       crate(%{pkgname}/wat)

%description -n %{name}+wat
This metapackage enables feature "wat" for the Rust wit-parser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
