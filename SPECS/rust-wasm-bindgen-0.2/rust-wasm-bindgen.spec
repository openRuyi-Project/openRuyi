# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen
%global full_version 0.2.117
%global pkgname wasm-bindgen-0.2

Name:           rust-wasm-bindgen-0.2
Version:        0.2.117
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen
#!RemoteAsset:  sha256:0551fc1bb415591e3372d0bc4780db7e587d84e2a7e79da121051c5c4b89d0b0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(once-cell-1.0) >= 1.21.4
Requires:       crate(rustversion-1.0/default) >= 1.0.22
Requires:       crate(wasm-bindgen-macro-0.2/default) >= 0.2.117
Requires:       crate(wasm-bindgen-shared-0.2/default) >= 0.2.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/enable-interning)
Provides:       crate(%{pkgname}/gg-alloc)
Provides:       crate(%{pkgname}/msrv)
Provides:       crate(%{pkgname}/rustversion)
Provides:       crate(%{pkgname}/spans)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/xxx-debug-only-print-generated-code)

%description
Source code for takopackized Rust crate "wasm-bindgen"

%package     -n %{name}+serde
Summary:        Easy support for interacting between JS and Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wasm-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-serialize
Summary:        Easy support for interacting between JS and Rust - feature "serde-serialize"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/serde-json)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/serde-serialize)

%description -n %{name}+serde-serialize
This metapackage enables feature "serde-serialize" for the Rust wasm-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Easy support for interacting between JS and Rust - feature "serde_json"
Requires:       crate(%{pkgname})
Requires:       crate(serde-json-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json)

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust wasm-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+strict-macro
Summary:        Easy support for interacting between JS and Rust - feature "strict-macro"
Requires:       crate(%{pkgname})
Requires:       crate(wasm-bindgen-macro-0.2/strict-macro) >= 0.2.117
Provides:       crate(%{pkgname}/strict-macro)

%description -n %{name}+strict-macro
This metapackage enables feature "strict-macro" for the Rust wasm-bindgen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
