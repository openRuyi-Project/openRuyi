# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml_parser
%global full_version 1.1.2+spec-1.1.0
%global pkgname toml-parser-1

Name:           rust-toml-parser-1
Version:        1.1.2
Release:        %autorelease
Summary:        Rust crate "toml_parser"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:a2abe9b86193656635d2411dc43050282ca48aa31c2451210f4202550afb7526
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winnow-1) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unsafe) = %{version}

%description
Source code for takopackized Rust crate "toml_parser"

%package     -n %{name}+debug
Summary:        Yet another format-preserving TOML parser - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(anstream-1/default) >= 1.0.0
Requires:       crate(anstyle-1/default) >= 1.0.14
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust toml_parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simd
Summary:        Yet another format-preserving TOML parser - feature "simd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(winnow-1/simd) >= 1.0.0
Provides:       crate(%{pkgname}/simd) = %{version}

%description -n %{name}+simd
This metapackage enables feature "simd" for the Rust toml_parser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
