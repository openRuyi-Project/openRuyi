# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cookie_store
%global full_version 0.22.1
%global pkgname cookie-store-0.22

Name:           rust-cookie-store-0.22
Version:        0.22.1
Release:        %autorelease
Summary:        Rust crate "cookie_store"
License:        MIT OR Apache-2.0
URL:            https://github.com/pfernie/cookie_store
#!RemoteAsset:  sha256:15b2c103cf610ec6cae3da84a766285b42fd16aad564758459e6ecf128c75206
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cookie-0.18/default) >= 0.18.0
Requires:       crate(cookie-0.18/percent-encode) >= 0.18.0
Requires:       crate(document-features-0.2/default) >= 0.2.10
Requires:       crate(idna-1/default) >= 1.0.0
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(url-2/default) >= 2.3.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/log-secure-cookie-values) = %{version}

%description
Source code for takopackized Rust crate "cookie_store"

%package     -n %{name}+default
Summary:        Cookie storage and retrieval - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/public-suffix) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust cookie_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preserve-order
Summary:        Cookie storage and retrieval - feature "preserve_order"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.6.0
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+preserve-order
This metapackage enables feature "preserve_order" for the Rust cookie_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+public-suffix
Summary:        Cookie storage and retrieval - feature "public_suffix"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(publicsuffix-2/default) >= 2.2.3
Provides:       crate(%{pkgname}/public-suffix) = %{version}

%description -n %{name}+public-suffix
This metapackage enables feature "public_suffix" for the Rust cookie_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Cookie storage and retrieval - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.147
Requires:       crate(serde-derive-1/default) >= 1.0.147
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust cookie_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Cookie storage and retrieval - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.87
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust cookie_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-ron
Summary:        Cookie storage and retrieval - feature "serde_ron"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(ron-0.10/default) >= 0.10.1
Provides:       crate(%{pkgname}/serde-ron) = %{version}

%description -n %{name}+serde-ron
This metapackage enables feature "serde_ron" for the Rust cookie_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Cookie storage and retrieval - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/wasm-bindgen) >= 0.3.47
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust cookie_store crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
