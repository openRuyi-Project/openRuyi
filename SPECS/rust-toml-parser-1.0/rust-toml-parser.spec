# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml_parser
%global full_version 1.0.10+spec-1.1.0
%global pkgname toml-parser-1.0

Name:           rust-toml-parser-1.0
Version:        1.0.10
Release:        %autorelease
Summary:        Rust crate "toml_parser"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:7df25b4befd31c4816df190124375d5a20c6b6921e2cad937316de3fccd63420
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winnow-1.0) >= 1.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unsafe)

%description
Source code for takopackized Rust crate "toml_parser"

%package     -n %{name}+debug
Summary:        Yet another format-preserving TOML parser - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(anstream-0.6/default) >= 0.6.20
Requires:       crate(anstyle-1.0/default) >= 1.0.11
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust toml_parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simd
Summary:        Yet another format-preserving TOML parser - feature "simd"
Requires:       crate(%{pkgname})
Requires:       crate(winnow-1.0/simd) >= 1.0.0
Provides:       crate(%{pkgname}/simd)

%description -n %{name}+simd
This metapackage enables feature "simd" for the Rust toml_parser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
