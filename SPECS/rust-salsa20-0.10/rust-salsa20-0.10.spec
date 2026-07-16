# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name salsa20
%global full_version 0.10.2
%global pkgname salsa20-0.10

Name:           rust-salsa20-0.10
Version:        0.10.2
Release:        %autorelease
Summary:        Rust crate "salsa20"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/stream-ciphers
#!RemoteAsset:  sha256:97a22f5af31f73a954c10289c93e8a50cc23d971e80ee446f1f6f7137a088213
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.4/default) >= 0.4.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "salsa20"

%package     -n %{name}+std
Summary:        Salsa20 Stream Cipher - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.4/std) >= 0.4.2
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust salsa20 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Salsa20 Stream Cipher - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.4/zeroize) >= 0.4.2
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust salsa20 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
