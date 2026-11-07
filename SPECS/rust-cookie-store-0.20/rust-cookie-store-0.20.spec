# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cookie_store
%global full_version 0.20.0
%global pkgname cookie-store-0.20

Name:           rust-cookie-store-0.20
Version:        0.20.0
Release:        %autorelease
Summary:        Rust crate "cookie_store"
License:        MIT OR Apache-2.0
URL:            https://github.com/pfernie/cookie_store
#!RemoteAsset:  sha256:387461abbc748185c3a6e1673d826918b450b87ff22639429c694619a83b6cf6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cookie-0.17/default) >= 0.17.0
Requires:       crate(cookie-0.17/percent-encode) >= 0.17.0
Requires:       crate(idna-0.3/default) >= 0.3.0
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(serde-1/default) >= 1.0.147
Requires:       crate(serde-derive-1/default) >= 1.0.147
Requires:       crate(serde-json-1/default) >= 1.0.87
Requires:       crate(time-0.3/default) >= 0.3.16
Requires:       crate(url-2/default) >= 2.3.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/log-secure-cookie-values) = %{version}

%description
Source code for takopackized Rust crate "cookie_store"

%package     -n %{name}+indexmap
Summary:        Cookie storage and retrieval - feature "indexmap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-1/default) >= 1.9.1
Provides:       crate(%{pkgname}/indexmap) = %{version}
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust cookie_store crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "preserve_order" feature.

%package     -n %{name}+publicsuffix
Summary:        Cookie storage and retrieval - feature "publicsuffix" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(publicsuffix-2/default) >= 2.2.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/public-suffix) = %{version}
Provides:       crate(%{pkgname}/publicsuffix) = %{version}

%description -n %{name}+publicsuffix
This metapackage enables feature "publicsuffix" for the Rust cookie_store crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "public_suffix" features.

%package     -n %{name}+wasm-bindgen
Summary:        Cookie storage and retrieval - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/wasm-bindgen) >= 0.3.16
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust cookie_store crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
