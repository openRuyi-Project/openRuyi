# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gcp_auth
%global full_version 0.7.6
%global pkgname gcp-auth-0.7

Name:           rust-gcp-auth-0.7
Version:        0.7.6
Release:        %autorelease
Summary:        Rust crate "gcp_auth"
License:        MIT
URL:            https://github.com/hrvolapeter/gcp_auth
#!RemoteAsset:  sha256:4ab5724fa45095bf1965ff491e75182818ba13f2a8755b04d484a9ec6408b622
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.0
Requires:       crate(base64-0.21/default) >= 0.21.0
Requires:       crate(dirs-next-2/default) >= 2.0.0
Requires:       crate(hyper-0.14/client) >= 0.14.2
Requires:       crate(hyper-0.14/default) >= 0.14.2
Requires:       crate(hyper-0.14/http2) >= 0.14.2
Requires:       crate(hyper-0.14/runtime) >= 0.14.2
Requires:       crate(hyper-rustls-0.23/http1) >= 0.23.0
Requires:       crate(hyper-rustls-0.23/http2) >= 0.23.0
Requires:       crate(hyper-rustls-0.23/tokio-runtime) >= 0.23.0
Requires:       crate(ring-0.16/default) >= 0.16.20
Requires:       crate(rustls-0.20/default) >= 0.20.2
Requires:       crate(rustls-pemfile-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/rc) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(time-0.3/default) >= 0.3.5
Requires:       crate(time-0.3/serde) >= 0.3.5
Requires:       crate(tokio-1/default) >= 1.1.0
Requires:       crate(tokio-1/fs) >= 1.1.0
Requires:       crate(tokio-1/sync) >= 1.1.0
Requires:       crate(tracing-0.1/default) >= 0.1.29
Requires:       crate(tracing-futures-0.2/default) >= 0.2.5
Requires:       crate(url-2/default) >= 2.0.0
Requires:       crate(which-4/default) >= 4.2.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "gcp_auth"

%package     -n %{name}+default
Summary:        Google cloud platform (GCP) authentication using default and custom service accounts - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-rustls-0.23/http1) >= 0.23.0
Requires:       crate(hyper-rustls-0.23/http2) >= 0.23.0
Requires:       crate(hyper-rustls-0.23/rustls-native-certs) >= 0.23.0
Requires:       crate(hyper-rustls-0.23/tokio-runtime) >= 0.23.0
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gcp_auth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Google cloud platform (GCP) authentication using default and custom service accounts - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-rustls-0.23/http1) >= 0.23.0
Requires:       crate(hyper-rustls-0.23/http2) >= 0.23.0
Requires:       crate(hyper-rustls-0.23/tokio-runtime) >= 0.23.0
Requires:       crate(hyper-rustls-0.23/webpki-roots) >= 0.23.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This metapackage enables feature "webpki-roots" for the Rust gcp_auth crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
