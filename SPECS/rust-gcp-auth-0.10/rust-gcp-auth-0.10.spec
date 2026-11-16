# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gcp_auth
%global full_version 0.10.0
%global pkgname gcp-auth-0.10

Name:           rust-gcp-auth-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "gcp_auth"
License:        MIT
URL:            https://github.com/hrvolapeter/gcp_auth
#!RemoteAsset:  sha256:de2c71ea685b88a1aa50e9fb66fe0e1cb29d755f58cca41fb8c91ef604d4f4d4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.0
Requires:       crate(base64-0.21/default) >= 0.21.0
Requires:       crate(chrono-0.4/default) >= 0.4.31
Requires:       crate(chrono-0.4/serde) >= 0.4.31
Requires:       crate(home-0.5/default) >= 0.5.5
Requires:       crate(hyper-0.14/client) >= 0.14.2
Requires:       crate(hyper-0.14/default) >= 0.14.2
Requires:       crate(hyper-0.14/http2) >= 0.14.2
Requires:       crate(hyper-0.14/runtime) >= 0.14.2
Requires:       crate(hyper-rustls-0.24/http1) >= 0.24.0
Requires:       crate(hyper-rustls-0.24/http2) >= 0.24.0
Requires:       crate(hyper-rustls-0.24/tokio-runtime) >= 0.24.0
Requires:       crate(ring-0.17/default) >= 0.17.0
Requires:       crate(rustls-0.21/default) >= 0.21.0
Requires:       crate(rustls-pemfile-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/rc) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(tokio-1/default) >= 1.1.0
Requires:       crate(tokio-1/fs) >= 1.1.0
Requires:       crate(tokio-1/sync) >= 1.1.0
Requires:       crate(tracing-0.1/default) >= 0.1.29
Requires:       crate(tracing-futures-0.2/default) >= 0.2.5
Requires:       crate(url-2/default) >= 2.0.0
Requires:       crate(which-5/default) >= 5.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "gcp_auth"

%package     -n %{name}+default
Summary:        Google cloud platform (GCP) authentication using default and custom service accounts - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-rustls-0.24/http1) >= 0.24.0
Requires:       crate(hyper-rustls-0.24/http2) >= 0.24.0
Requires:       crate(hyper-rustls-0.24/rustls-native-certs) >= 0.24.0
Requires:       crate(hyper-rustls-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gcp_auth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Google cloud platform (GCP) authentication using default and custom service accounts - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-rustls-0.24/http1) >= 0.24.0
Requires:       crate(hyper-rustls-0.24/http2) >= 0.24.0
Requires:       crate(hyper-rustls-0.24/tokio-runtime) >= 0.24.0
Requires:       crate(hyper-rustls-0.24/webpki-roots) >= 0.24.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This metapackage enables feature "webpki-roots" for the Rust gcp_auth crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
