# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name polyval
%global full_version 0.6.2
%global pkgname polyval-0.6

Name:           rust-polyval-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "polyval"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/universal-hashes
#!RemoteAsset:  sha256:9d1fe60d06143b2430aa532c94cfe9e29783047f06c0d7fd359a9a51b729fa25
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(cpufeatures-0.2/default) >= 0.2.0
Requires:       crate(opaque-debug-0.3/default) >= 0.3.0
Requires:       crate(universal-hash-0.5) >= 0.5.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "polyval"

%package     -n %{name}+std
Summary:        GHASH-like universal hash over GF(2^128) useful for constructing a Message Authentication Code (MAC) - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(universal-hash-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust polyval crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        GHASH-like universal hash over GF(2^128) useful for constructing a Message Authentication Code (MAC) - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust polyval crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
