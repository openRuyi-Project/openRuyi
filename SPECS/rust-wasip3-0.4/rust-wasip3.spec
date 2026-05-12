# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasip3
%global full_version 0.4.0+wasi-0.3.0-rc-2026-01-06
%global pkgname wasip3-0.4

Name:           rust-wasip3-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "wasip3"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasi-rs
#!RemoteAsset:  sha256:5428f8bf88ea5ddc08faddef2ac4a67e390b88186c703ce6dbd955e1c145aca5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(wit-bindgen-0.51/async) >= 0.51.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wasip3"

%package     -n %{name}+http-compat
Summary:        WASIp3 API bindings for Rust - feature "http-compat"
Requires:       crate(%{pkgname})
Requires:       crate(bytes-1.0/default) >= 1.10.1
Requires:       crate(http-1.0/default) >= 1.3.1
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(thiserror-2.0/default) >= 2.0.17
Requires:       crate(wit-bindgen-0.51/async) >= 0.51.0
Requires:       crate(wit-bindgen-0.51/async-spawn) >= 0.51.0
Provides:       crate(%{pkgname}/http-compat)

%description -n %{name}+http-compat
This metapackage enables feature "http-compat" for the Rust wasip3 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
