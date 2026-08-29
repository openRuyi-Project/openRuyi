# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name poly1305
%global full_version 0.8.0
%global pkgname poly1305-0.8

Name:           rust-poly1305-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "poly1305"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/universal-hashes
#!RemoteAsset:  sha256:8159bd90725d2df49889a078b54f4f79e87f1f8a8444194cdca81d38f5393abf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cpufeatures-0.2/default) >= 0.2.0
Requires:       crate(opaque-debug-0.3/default) >= 0.3.0
Requires:       crate(universal-hash-0.5) >= 0.5.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "poly1305"

%package     -n %{name}+std
Summary:        Poly1305 universal hash function and message authentication code - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(universal-hash-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust poly1305 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Poly1305 universal hash function and message authentication code - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust poly1305 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
