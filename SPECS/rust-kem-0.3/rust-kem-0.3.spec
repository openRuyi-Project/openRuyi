# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kem
%global full_version 0.3.0
%global pkgname kem-0.3

Name:           rust-kem-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "kem"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:01737161ba802849cfd486b5bd209d38ba4943494c249a8126005170c7621edd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.2/default) >= 0.2.0
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.0
Requires:       crate(rand-core-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
encapsulator) to generate and encrypt a short secret key and transmit it to a receiver (a.k.a. decapsulator) confidentially
Source code for takopackized Rust crate "kem"

%package     -n %{name}+getrandom
Summary:        Traits for Key Encapsulation Mechanisms (KEMs): public-key cryptosystems designed to enable a sender (a.k.a - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crypto-common-0.2/getrandom) >= 0.2.0
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
encapsulator) to generate and encrypt a short secret key and transmit it to a receiver (a.k.a. decapsulator) confidentially
This metapackage enables feature "getrandom" for the Rust kem crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
