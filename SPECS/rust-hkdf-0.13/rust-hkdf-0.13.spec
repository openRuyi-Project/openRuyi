# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hkdf
%global full_version 0.13.0
%global pkgname hkdf-0.13

Name:           rust-hkdf-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "hkdf"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/KDFs/
#!RemoteAsset:  sha256:4aaa26c720c68b866f2c96ef5c1264b3e6f473fe5d4ce61cd44bbe913e553018
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hmac-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hkdf"

%package     -n %{name}+kdf
Summary:        HMAC-based Extract-and-Expand Key Derivation Function (HKDF) - feature "kdf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(kdf-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/kdf) = %{version}

%description -n %{name}+kdf
This metapackage enables feature "kdf" for the Rust hkdf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
