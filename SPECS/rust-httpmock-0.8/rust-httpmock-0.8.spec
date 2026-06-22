# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name httpmock
%global full_version 0.8.3
%global pkgname httpmock-0.8

Name:           rust-httpmock-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "httpmock"
License:        MIT
URL:            https://github.com/httpmock/httpmock
#!RemoteAsset:  sha256:bf4888a4d02d8e1f92ffb6b4965cf5ff56dda36ef41975f41c6fa0f6bde78c4e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(assert-json-diff-2/default) >= 2.0.0
Requires:       crate(async-object-pool-0.2/default) >= 0.2.0
Requires:       crate(async-trait-0.1/default) >= 0.1.0
Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(bytes-1/serde) >= 1.0.0
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.0
Requires:       crate(form-urlencoded-1/default) >= 1.0.0
Requires:       crate(futures-timer-3/default) >= 3.0.0
Requires:       crate(futures-util-0.3/default) >= 0.3.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Requires:       crate(hyper-1/client) >= 1.0.0
Requires:       crate(hyper-1/default) >= 1.0.0
Requires:       crate(hyper-1/http1) >= 1.0.0
Requires:       crate(hyper-1/server) >= 1.0.0
Requires:       crate(hyper-util-0.1/default) >= 0.1.0
Requires:       crate(hyper-util-0.1/http1) >= 0.1.0
Requires:       crate(hyper-util-0.1/server) >= 0.1.0
Requires:       crate(hyper-util-0.1/server-auto) >= 0.1.0
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.0
Requires:       crate(path-tree-0.8/default) >= 0.8.0
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(serde-regex-1/default) >= 1.0.0
Requires:       crate(similar-2/default) >= 2.0.0
Requires:       crate(stringmetrics-2/default) >= 2.0.0
Requires:       crate(tabwriter-1/default) >= 1.0.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.43.0
Requires:       crate(tokio-1/macros) >= 1.43.0
Requires:       crate(tokio-1/net) >= 1.43.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.43.0
Requires:       crate(tokio-1/signal) >= 1.43.0
Requires:       crate(tokio-1/sync) >= 1.43.0
Requires:       crate(tracing-0.1/default) >= 0.1.0
Requires:       crate(tracing-0.1/log) >= 0.1.0
Requires:       crate(url-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/experimental) = %{version}

%description
Source code for takopackized Rust crate "httpmock"

%package     -n %{name}+clap
Summary:        HTTP mocking library for Rust - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.0.0
Requires:       crate(clap-4/derive) >= 4.0.0
Requires:       crate(clap-4/env) >= 4.0.0
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+colored
Summary:        HTTP mocking library for Rust - feature "colored" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(colored-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/color) = %{version}
Provides:       crate(%{pkgname}/colored) = %{version}

%description -n %{name}+colored
This metapackage enables feature "colored" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "color" feature.

%package     -n %{name}+headers
Summary:        HTTP mocking library for Rust - feature "headers" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(headers-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/cookies) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/headers) = %{version}

%description -n %{name}+headers
This metapackage enables feature "headers" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cookies", and "default" features.

%package     -n %{name}+http2
Summary:        HTTP mocking library for Rust - feature "http2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-1/client) >= 1.0.0
Requires:       crate(hyper-1/http1) >= 1.0.0
Requires:       crate(hyper-1/http2) >= 1.0.0
Requires:       crate(hyper-1/server) >= 1.0.0
Requires:       crate(hyper-util-0.1/http1) >= 0.1.0
Requires:       crate(hyper-util-0.1/http2) >= 0.1.0
Requires:       crate(hyper-util-0.1/server) >= 0.1.0
Requires:       crate(hyper-util-0.1/server-auto) >= 0.1.0
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.0
Provides:       crate(%{pkgname}/http2) = %{version}

%description -n %{name}+http2
This metapackage enables feature "http2" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https
Summary:        HTTP mocking library for Rust - feature "https"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hyper-rustls) = %{version}
Requires:       crate(%{pkgname}/if-addrs) = %{version}
Requires:       crate(%{pkgname}/rcgen) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(%{pkgname}/rustls-pki-types) = %{version}
Requires:       crate(%{pkgname}/tls-detect) = %{version}
Requires:       crate(%{pkgname}/tokio-rustls) = %{version}
Requires:       crate(rustls-0.23/ring) >= 0.23.0
Requires:       crate(rustls-0.23/std) >= 0.23.0
Requires:       crate(rustls-0.23/tls12) >= 0.23.0
Provides:       crate(%{pkgname}/https) = %{version}

%description -n %{name}+https
This metapackage enables feature "https" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hyper-rustls
Summary:        HTTP mocking library for Rust - feature "hyper-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/logging) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/native-tokio) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.0
Provides:       crate(%{pkgname}/hyper-rustls) = %{version}

%description -n %{name}+hyper-rustls
This metapackage enables feature "hyper-rustls" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+if-addrs
Summary:        HTTP mocking library for Rust - feature "if-addrs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(if-addrs-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/if-addrs) = %{version}

%description -n %{name}+if-addrs
This metapackage enables feature "if-addrs" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proxy
Summary:        HTTP mocking library for Rust - feature "proxy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hyper-rustls) = %{version}
Requires:       crate(%{pkgname}/remote-https) = %{version}
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/http2) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/logging) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/native-tokio) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.0
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.0
Requires:       crate(hyper-util-0.1/http1) >= 0.1.0
Requires:       crate(hyper-util-0.1/http2) >= 0.1.0
Requires:       crate(hyper-util-0.1/server) >= 0.1.0
Requires:       crate(hyper-util-0.1/server-auto) >= 0.1.0
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.0
Provides:       crate(%{pkgname}/proxy) = %{version}

%description -n %{name}+proxy
This metapackage enables feature "proxy" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rcgen
Summary:        HTTP mocking library for Rust - feature "rcgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rcgen-0.13/default) >= 0.13.0
Requires:       crate(rcgen-0.13/pem) >= 0.13.0
Requires:       crate(rcgen-0.13/x509-parser) >= 0.13.0
Provides:       crate(%{pkgname}/rcgen) = %{version}

%description -n %{name}+rcgen
This metapackage enables feature "rcgen" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+record
Summary:        HTTP mocking library for Rust - feature "record"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proxy) = %{version}
Requires:       crate(%{pkgname}/serde-yaml) = %{version}
Provides:       crate(%{pkgname}/record) = %{version}

%description -n %{name}+record
This metapackage enables feature "record" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+remote
Summary:        HTTP mocking library for Rust - feature "remote"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.0
Requires:       crate(hyper-util-0.1/http1) >= 0.1.0
Requires:       crate(hyper-util-0.1/http2) >= 0.1.0
Requires:       crate(hyper-util-0.1/server) >= 0.1.0
Requires:       crate(hyper-util-0.1/server-auto) >= 0.1.0
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.0
Provides:       crate(%{pkgname}/remote) = %{version}

%description -n %{name}+remote
This metapackage enables feature "remote" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+remote-https
Summary:        HTTP mocking library for Rust - feature "remote-https"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hyper-rustls) = %{version}
Requires:       crate(%{pkgname}/remote) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/http2) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/logging) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/native-tokio) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/ring) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.0
Requires:       crate(rustls-0.23/ring) >= 0.23.0
Requires:       crate(rustls-0.23/std) >= 0.23.0
Requires:       crate(rustls-0.23/tls12) >= 0.23.0
Provides:       crate(%{pkgname}/remote-https) = %{version}

%description -n %{name}+remote-https
This metapackage enables feature "remote-https" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        HTTP mocking library for Rust - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/std) >= 0.23.0
Requires:       crate(rustls-0.23/tls12) >= 0.23.0
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-pki-types
Summary:        HTTP mocking library for Rust - feature "rustls-pki-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-pki-types-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/rustls-pki-types) = %{version}

%description -n %{name}+rustls-pki-types
This metapackage enables feature "rustls-pki-types" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-yaml
Summary:        HTTP mocking library for Rust - feature "serde_yaml"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-yaml-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/serde-yaml) = %{version}

%description -n %{name}+serde-yaml
This metapackage enables feature "serde_yaml" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+standalone
Summary:        HTTP mocking library for Rust - feature "standalone"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clap) = %{version}
Requires:       crate(%{pkgname}/cookies) = %{version}
Requires:       crate(%{pkgname}/http2) = %{version}
Requires:       crate(%{pkgname}/record) = %{version}
Requires:       crate(%{pkgname}/remote) = %{version}
Requires:       crate(%{pkgname}/remote-https) = %{version}
Requires:       crate(%{pkgname}/tracing-subscriber) = %{version}
Provides:       crate(%{pkgname}/standalone) = %{version}

%description -n %{name}+standalone
This metapackage enables feature "standalone" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-detect
Summary:        HTTP mocking library for Rust - feature "tls-detect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tls-detect-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/tls-detect) = %{version}

%description -n %{name}+tls-detect
This metapackage enables feature "tls-detect" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-rustls
Summary:        HTTP mocking library for Rust - feature "tokio-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-rustls-0.26/logging) >= 0.26.0
Requires:       crate(tokio-rustls-0.26/tls12) >= 0.26.0
Provides:       crate(%{pkgname}/tokio-rustls) = %{version}

%description -n %{name}+tokio-rustls
This metapackage enables feature "tokio-rustls" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-subscriber
Summary:        HTTP mocking library for Rust - feature "tracing-subscriber"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/env-filter) >= 0.3.0
Provides:       crate(%{pkgname}/tracing-subscriber) = %{version}

%description -n %{name}+tracing-subscriber
This metapackage enables feature "tracing-subscriber" for the Rust httpmock crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
