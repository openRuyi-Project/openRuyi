# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cryptoki
%global full_version 0.12.1
%global pkgname cryptoki-0.12

Name:           rust-cryptoki-0.12
Version:        0.12.1
Release:        %autorelease
Summary:        Rust crate "cryptoki"
License:        Apache-2.0
URL:            https://github.com/parallaxsecond/rust-cryptoki
#!RemoteAsset:  sha256:625cf4599c43d69a16996ce2573fc80745a0b0300c962f0bfa11d55b6cab2b2d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.10.0
Requires:       crate(cryptoki-sys-0.5/default) >= 0.5.0
Requires:       crate(libloading-0.8/default) >= 0.8.9
Requires:       crate(log-0.4/default) >= 0.4.28
Requires:       crate(secrecy-0.10/default) >= 0.10.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cryptoki"

%package     -n %{name}+generate-bindings
Summary:        Rust-native wrapper around the PKCS #11 API - feature "generate-bindings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cryptoki-sys-0.5/generate-bindings) >= 0.5.0
Provides:       crate(%{pkgname}/generate-bindings) = %{version}

%description -n %{name}+generate-bindings
This metapackage enables feature "generate-bindings" for the Rust cryptoki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Rust-native wrapper around the PKCS #11 API - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(secrecy-0.10/serde) >= 0.10.3
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust cryptoki crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
