# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zeroize
%global full_version 1.8.2
%global pkgname zeroize-1.0

Name:           rust-zeroize-1.0
Version:        1.8.2
Release:        %autorelease
Summary:        Rust crate "zeroize"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/utils/tree/master/zeroize
#!RemoteAsset:  sha256:b97154e67e32c85465826e8bcc1c59429aaaf107c1e4a9e53c8d8ccd5eff88d0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/aarch64)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/simd)
Provides:       crate(%{pkgname}/std)

%description
Uses a portable pure Rust implementation that works everywhere, even WASM!
Source code for takopackized Rust crate "zeroize"

%package     -n %{name}+serde
Summary:        Securely clear secrets from memory with a simple trait built on stable Rust primitives which guarantee memory is zeroed using an operation will not be 'optimized away' by the compiler - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
Uses a portable pure Rust implementation that works everywhere, even WASM!
This metapackage enables feature "serde" for the Rust zeroize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize-derive
Summary:        Securely clear secrets from memory with a simple trait built on stable Rust primitives which guarantee memory is zeroed using an operation will not be 'optimized away' by the compiler - feature "zeroize_derive" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-derive-1.0/default) >= 1.3
Provides:       crate(%{pkgname}/derive)
Provides:       crate(%{pkgname}/zeroize-derive)

%description -n %{name}+zeroize-derive
Uses a portable pure Rust implementation that works everywhere, even WASM!
This metapackage enables feature "zeroize_derive" for the Rust zeroize crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
