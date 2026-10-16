# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name auditable-extract
%global full_version 0.3.5
%global pkgname auditable-extract-0.3

Name:           rust-auditable-extract-0.3
Version:        0.3.5
Release:        %autorelease
Summary:        Rust crate "auditable-extract"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-secure-code/cargo-auditable
#!RemoteAsset:  sha256:44371e9f9759dea49c42b6c6fe4c64ea216ee2af325a4524a7180823e00d3e7a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(binfarce-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "auditable-extract"

%package     -n %{name}+wasmparser
Summary:        Extract the dependency trees embedded in binaries by `cargo auditable` - feature "wasmparser" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasmparser-0.207) >= 0.207.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/wasm) = %{version}
Provides:       crate(%{pkgname}/wasmparser) = %{version}

%description -n %{name}+wasmparser
This metapackage enables feature "wasmparser" for the Rust auditable-extract crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "wasm" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
