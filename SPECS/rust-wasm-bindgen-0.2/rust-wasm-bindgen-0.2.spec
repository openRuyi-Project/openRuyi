# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen
%global full_version 0.2.121
%global pkgname wasm-bindgen-0.2

Name:           rust-wasm-bindgen-0.2
Version:        0.2.121
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen
#!RemoteAsset:  sha256:49ace1d07c165b0864824eee619580c4689389afa9dc9ed3a4c75040d82e6790
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(once-cell-1) >= 1.12.0
Requires:       crate(rustversion-1) >= 1.0.6
Requires:       crate(wasm-bindgen-macro-0.2/default) >= 0.2.121
Requires:       crate(wasm-bindgen-shared-0.2/default) >= 0.2.121
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/enable-interning) = %{version}
Provides:       crate(%{pkgname}/gg-alloc) = %{version}
Provides:       crate(%{pkgname}/msrv) = %{version}
Provides:       crate(%{pkgname}/rustversion) = %{version}
Provides:       crate(%{pkgname}/spans) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/xxx-debug-only-print-generated-code) = %{version}

%description
Source code for takopackized Rust crate "wasm-bindgen"

%package     -n %{name}+serde
Summary:        Easy support for interacting between JS and Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wasm-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-serialize
Summary:        Easy support for interacting between JS and Rust - feature "serde-serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/serde-serialize) = %{version}

%description -n %{name}+serde-serialize
This metapackage enables feature "serde-serialize" for the Rust wasm-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Easy support for interacting between JS and Rust - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust wasm-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+strict-macro
Summary:        Easy support for interacting between JS and Rust - feature "strict-macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-bindgen-macro-0.2/strict-macro) >= 0.2.121
Provides:       crate(%{pkgname}/strict-macro) = %{version}

%description -n %{name}+strict-macro
This metapackage enables feature "strict-macro" for the Rust wasm-bindgen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
