# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name getrandom
%global full_version 0.3.4
%global pkgname getrandom-0.3

Name:           rust-getrandom-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "getrandom"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-random/getrandom
#!RemoteAsset:  sha256:899def5c37c4fd7b2664648c28120ecec138e4d395b459e5ca34f9cce2dd77fd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2) >= 0.2.184
Requires:       crate(r-efi-5.0) >= 5.3.0
Requires:       crate(wasip2-1.0) >= 1.0.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "getrandom"

%package     -n %{name}+wasm-js
Summary:        Small cross-platform library for retrieving random data from system source - feature "wasm_js"
Requires:       crate(%{pkgname})
Requires:       crate(js-sys-0.3) >= 0.3.94
Requires:       crate(wasm-bindgen-0.2) >= 0.2.117
Provides:       crate(%{pkgname}/wasm-js)

%description -n %{name}+wasm-js
This metapackage enables feature "wasm_js" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
