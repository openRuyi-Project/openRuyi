# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tonic
%global full_version 0.14.2
%global pkgname tonic-0.14

Name:           rust-tonic-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "tonic"
License:        MIT
URL:            https://github.com/hyperium/tonic
#!RemoteAsset:  sha256:eb7613188ce9f7df5bfe185db26c5814347d110db17920415cf2fbcad85e7203
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(http-body-1/default) >= 1.0.0
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Requires:       crate(percent-encoding-2/default) >= 2.1.0
Requires:       crate(pin-project-1/default) >= 1.0.11
Requires:       crate(sync-wrapper-1/default) >= 1.0.2
Requires:       crate(tokio-stream-0.1) >= 0.1.16
Requires:       crate(tower-layer-0.3/default) >= 0.3.0
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Requires:       crate(tracing-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tonic"

%package     -n %{name}+tls-any
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "_tls-any"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls-connect-info) = %{version}
Requires:       crate(tokio-1) >= 1.0.0
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Provides:       crate(%{pkgname}/tls-any) = %{version}

%description -n %{name}+tls-any
This metapackage enables feature "_tls-any" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+channel
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-1/client) >= 1.0.0
Requires:       crate(hyper-1/default) >= 1.0.0
Requires:       crate(hyper-1/http1) >= 1.0.0
Requires:       crate(hyper-1/http2) >= 1.0.0
Requires:       crate(hyper-timeout-0.5/default) >= 0.5.0
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.4
Requires:       crate(hyper-util-0.1/default) >= 0.1.4
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.4
Requires:       crate(tokio-1) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tower-0.5) >= 0.5.0
Requires:       crate(tower-0.5/balance) >= 0.5.0
Requires:       crate(tower-0.5/buffer) >= 0.5.0
Requires:       crate(tower-0.5/discover) >= 0.5.0
Requires:       crate(tower-0.5/limit) >= 0.5.0
Requires:       crate(tower-0.5/load-shed) >= 0.5.0
Requires:       crate(tower-0.5/util) >= 0.5.0
Provides:       crate(%{pkgname}/channel) = %{version}

%description -n %{name}+channel
This metapackage enables feature "channel" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+codegen
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "codegen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-trait-0.1/default) >= 0.1.13
Provides:       crate(%{pkgname}/codegen) = %{version}

%description -n %{name}+codegen
This metapackage enables feature "codegen" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/codegen) = %{version}
Requires:       crate(%{pkgname}/router) = %{version}
Requires:       crate(%{pkgname}/transport) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "deflate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/deflate) = %{version}
Provides:       crate(%{pkgname}/gzip) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "gzip" feature.

%package     -n %{name}+router
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "router"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(axum-0.8) >= 0.8.0
Requires:       crate(tower-0.5) >= 0.5.0
Requires:       crate(tower-0.5/util) >= 0.5.0
Provides:       crate(%{pkgname}/router) = %{version}

%description -n %{name}+router
This metapackage enables feature "router" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+server
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "server"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(h2-0.4/default) >= 0.4.0
Requires:       crate(hyper-1/default) >= 1.0.0
Requires:       crate(hyper-1/http1) >= 1.0.0
Requires:       crate(hyper-1/http2) >= 1.0.0
Requires:       crate(hyper-1/server) >= 1.0.0
Requires:       crate(hyper-util-0.1/default) >= 0.1.4
Requires:       crate(hyper-util-0.1/server-auto) >= 0.1.4
Requires:       crate(hyper-util-0.1/service) >= 0.1.4
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.4
Requires:       crate(socket2-0.6/all) >= 0.6.0
Requires:       crate(socket2-0.6/default) >= 0.6.0
Requires:       crate(tokio-1) >= 1.0.0
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tokio-stream-0.1/net) >= 0.1.16
Requires:       crate(tower-0.5) >= 0.5.0
Requires:       crate(tower-0.5/limit) >= 0.5.0
Requires:       crate(tower-0.5/load-shed) >= 0.5.0
Requires:       crate(tower-0.5/util) >= 0.5.0
Provides:       crate(%{pkgname}/server) = %{version}

%description -n %{name}+server
This metapackage enables feature "server" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-aws-lc
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tls-aws-lc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls-any) = %{version}
Requires:       crate(tokio-rustls-0.26/aws-lc-rs) >= 0.26.1
Requires:       crate(tokio-rustls-0.26/logging) >= 0.26.1
Requires:       crate(tokio-rustls-0.26/tls12) >= 0.26.1
Provides:       crate(%{pkgname}/tls-aws-lc) = %{version}

%description -n %{name}+tls-aws-lc
This metapackage enables feature "tls-aws-lc" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-connect-info
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tls-connect-info"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-rustls-0.26/logging) >= 0.26.1
Requires:       crate(tokio-rustls-0.26/tls12) >= 0.26.1
Provides:       crate(%{pkgname}/tls-connect-info) = %{version}

%description -n %{name}+tls-connect-info
This metapackage enables feature "tls-connect-info" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-native-roots
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tls-native-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/channel) = %{version}
Requires:       crate(%{pkgname}/tls-any) = %{version}
Requires:       crate(rustls-native-certs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/tls-native-roots) = %{version}

%description -n %{name}+tls-native-roots
This metapackage enables feature "tls-native-roots" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-ring
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tls-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls-any) = %{version}
Requires:       crate(tokio-rustls-0.26/logging) >= 0.26.1
Requires:       crate(tokio-rustls-0.26/ring) >= 0.26.1
Requires:       crate(tokio-rustls-0.26/tls12) >= 0.26.1
Provides:       crate(%{pkgname}/tls-ring) = %{version}

%description -n %{name}+tls-ring
This metapackage enables feature "tls-ring" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-webpki-roots
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tls-webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/channel) = %{version}
Requires:       crate(%{pkgname}/tls-any) = %{version}
Requires:       crate(webpki-roots-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/tls-webpki-roots) = %{version}

%description -n %{name}+tls-webpki-roots
This metapackage enables feature "tls-webpki-roots" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+transport
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "transport"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/channel) = %{version}
Requires:       crate(%{pkgname}/server) = %{version}
Provides:       crate(%{pkgname}/transport) = %{version}

%description -n %{name}+transport
This metapackage enables feature "transport" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
