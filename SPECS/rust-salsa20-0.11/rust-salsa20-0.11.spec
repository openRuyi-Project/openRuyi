# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name salsa20
%global full_version 0.11.0
%global pkgname salsa20-0.11

Name:           rust-salsa20-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "salsa20"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/stream-ciphers
#!RemoteAsset:  sha256:2f874456e72520ff1375a06c588eaf074b0f01f9e9e1aada45bd9b7954a6e42c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(cipher-0.5/default) >= 0.5.0
Requires:       crate(cipher-0.5/stream-wrapper) >= 0.5.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "salsa20"

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the Salsa20 stream cipher - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.5/stream-wrapper) >= 0.5.0
Requires:       crate(cipher-0.5/zeroize) >= 0.5.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust salsa20 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
