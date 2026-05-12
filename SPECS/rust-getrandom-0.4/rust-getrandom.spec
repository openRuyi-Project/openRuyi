# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name getrandom
%global full_version 0.4.2
%global pkgname getrandom-0.4

Name:           rust-getrandom-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "getrandom"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-random/getrandom
#!RemoteAsset:  sha256:0de51e6874e94e7bf76d726fc5d13ba782deca734ff60d5bb2fb2607c7406555
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2) >= 0.2.183
Requires:       crate(r-efi-6.0) >= 6.0.0
Requires:       crate(wasip2-1.0) >= 1.0.2
Requires:       crate(wasip3-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "getrandom"

%package     -n %{name}+sys-rng
Summary:        Small cross-platform library for retrieving random data from system source - feature "sys_rng"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/sys-rng)

%description -n %{name}+sys-rng
This metapackage enables feature "sys_rng" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-js
Summary:        Small cross-platform library for retrieving random data from system source - feature "wasm_js"
Requires:       crate(%{pkgname})
Requires:       crate(js-sys-0.3) >= 0.3.77
Requires:       crate(wasm-bindgen-0.2) >= 0.2.98
Provides:       crate(%{pkgname}/wasm-js)

%description -n %{name}+wasm-js
This metapackage enables feature "wasm_js" for the Rust getrandom crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
