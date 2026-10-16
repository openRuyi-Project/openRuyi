# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name twofish
%global full_version 0.7.1
%global pkgname twofish-0.7

Name:           rust-twofish-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "twofish"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/block-ciphers
#!RemoteAsset:  sha256:a78e83a30223c757c3947cd144a31014ff04298d8719ae10d03c31c0448c8013
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.4/default) >= 0.4.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "twofish"

%package     -n %{name}+zeroize
Summary:        Twofish block cipher - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.4/zeroize) >= 0.4.2
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust twofish crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
