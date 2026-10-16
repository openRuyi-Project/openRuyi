# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name auditable-info
%global full_version 0.10.1
%global pkgname auditable-info-0.10

Name:           rust-auditable-info-0.10
Version:        0.10.1
Release:        %autorelease
Summary:        Rust crate "auditable-info"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-secure-code/cargo-auditable
#!RemoteAsset:  sha256:ec38df9258af35c2cc9b79343cb452cfc44114ac759aaa29ec67c37a49a8236c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(auditable-extract-0.3) >= 0.3.4
Requires:       crate(miniz-oxide-0.9/default) >= 0.9.0
Requires:       crate(miniz-oxide-0.9/std) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "auditable-info"

%package     -n %{name}+auditable-serde
Summary:        High-level crate to extract the dependency trees embedded in binaries by `cargo auditable` - feature "auditable-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(auditable-serde-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/auditable-serde) = %{version}

%description -n %{name}+auditable-serde
This metapackage enables feature "auditable-serde" for the Rust auditable-info crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        High-level crate to extract the dependency trees embedded in binaries by `cargo auditable` - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/wasm) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust auditable-info crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        High-level crate to extract the dependency trees embedded in binaries by `cargo auditable` - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/auditable-serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust auditable-info crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        High-level crate to extract the dependency trees embedded in binaries by `cargo auditable` - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.57
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust auditable-info crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm
Summary:        High-level crate to extract the dependency trees embedded in binaries by `cargo auditable` - feature "wasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(auditable-extract-0.3/wasm) >= 0.3.4
Provides:       crate(%{pkgname}/wasm) = %{version}

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust auditable-info crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
