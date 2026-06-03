# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name web-time
%global full_version 1.1.0
%global pkgname web-time-1.0

Name:           rust-web-time-1.0
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "web-time"
License:        MIT OR Apache-2.0
URL:            https://github.com/daxpedda/web-time
#!RemoteAsset:  sha256:5a6580f308b1fad9207618087a65c04e7a10bc77e02c8e84e9b00dd4b12fa0bb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(js-sys-0.3/default) >= 0.3.83
Requires:       crate(wasm-bindgen-0.2) >= 0.2.106
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "web-time"

%package     -n %{name}+serde
Summary:        Drop-in replacement for std::time for Wasm in browsers - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust web-time crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
