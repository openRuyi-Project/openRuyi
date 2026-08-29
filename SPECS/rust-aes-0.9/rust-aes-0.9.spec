# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aes
%global full_version 0.9.1
%global pkgname aes-0.9

Name:           rust-aes-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "aes"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/block-ciphers
#!RemoteAsset:  sha256:f1fc76eaeac4c9164506c466d4ffdd8ec9d0c5bf57ee97177c4d8eceb3a0e138
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.5/default) >= 0.5.0
Requires:       crate(cpubits-0.1/default) >= 0.1.0
Requires:       crate(cpufeatures-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Rijndael)
Source code for takopackized Rust crate "aes"

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the Advanced Encryption Standard (a.k.a - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/aarch64) >= 1.8.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
Rijndael)
This metapackage enables feature "zeroize" for the Rust aes crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
