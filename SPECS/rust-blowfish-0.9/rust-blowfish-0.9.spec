# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name blowfish
%global full_version 0.9.1
%global pkgname blowfish-0.9

Name:           rust-blowfish-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "blowfish"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/block-ciphers
#!RemoteAsset:  sha256:e412e2cd0f2b2d93e02543ceae7917b3c70331573df19ee046bcbc35e45e87d7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1) >= 1.1.0
Requires:       crate(cipher-0.4/default) >= 0.4.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bcrypt) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "blowfish"

%package     -n %{name}+zeroize
Summary:        Blowfish block cipher - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.4/zeroize) >= 0.4.2
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust blowfish crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
