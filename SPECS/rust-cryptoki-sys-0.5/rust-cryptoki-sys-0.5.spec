# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cryptoki-sys
%global full_version 0.5.0
%global pkgname cryptoki-sys-0.5

Name:           rust-cryptoki-sys-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "cryptoki-sys"
License:        Apache-2.0
URL:            https://github.com/parallaxsecond/rust-cryptoki
#!RemoteAsset:  sha256:f1fd850498411e4057f1cba79e6e2bc7cbe960544c1046ab46d4685c403a1121
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libloading-0.8/default) >= 0.8.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cryptoki-sys"

%package     -n %{name}+bindgen
Summary:        FFI wrapper around the PKCS #11 API - feature "bindgen" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.72/default) >= 0.72.1
Provides:       crate(%{pkgname}/bindgen) = %{version}
Provides:       crate(%{pkgname}/generate-bindings) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust cryptoki-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "generate-bindings" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
