# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name reqwest
%global full_version 0.11.27
%global pkgname reqwest-0.11

Name:           rust-reqwest-0.11
Version:        0.11.27
Release:        %autorelease
Summary:        Rust crate "reqwest"
License:        MIT OR Apache-2.0
URL:            https://github.com/seanmonstar/reqwest
#!RemoteAsset:  sha256:dd67538700a17451e7cba03ac727fb961abb7607553461627b97de0b89cf4a62
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-compression-0.4/brotli) >= 0.4.0
Requires:       crate(async-compression-0.4/gzip) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(async-compression-0.4/zlib) >= 0.4.0
Requires:       crate(base64-0.21/default) >= 0.21.0
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(cookie-0.17/default) >= 0.17.0
Requires:       crate(cookie-store-0.20/default) >= 0.20.0
Requires:       crate(encoding-rs-0.8/default) >= 0.8.0
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(futures-util-0.3) >= 0.3.0
Requires:       crate(futures-util-0.3/io) >= 0.3.0
Requires:       crate(h2-0.3/default) >= 0.3.14
Requires:       crate(h3-0.0.3/default) >= 0.0.3
Requires:       crate(h3-quinn-0.0.4/default) >= 0.0.4
Requires:       crate(hickory-resolver-0.24/default) >= 0.24.0
Requires:       crate(hickory-resolver-0.24/tokio-runtime) >= 0.24.0
Requires:       crate(http-0.2/default) >= 0.2.0
Requires:       crate(http-body-0.4/default) >= 0.4.0
Requires:       crate(hyper-0.14/client) >= 0.14.21
Requires:       crate(hyper-0.14/http1) >= 0.14.21
Requires:       crate(hyper-0.14/http2) >= 0.14.21
Requires:       crate(hyper-0.14/runtime) >= 0.14.21
Requires:       crate(hyper-0.14/tcp) >= 0.14.21
Requires:       crate(hyper-rustls-0.24) >= 0.24.0
Requires:       crate(hyper-tls-0.5/default) >= 0.5.0
Requires:       crate(ipnet-2/default) >= 2.3.0
Requires:       crate(js-sys-0.3/default) >= 0.3.45
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(mime-0.3/default) >= 0.3.16
Requires:       crate(mime-guess-2) >= 2.0.0
Requires:       crate(native-tls-0.2/alpn) >= 0.2.10
Requires:       crate(native-tls-0.2/default) >= 0.2.10
Requires:       crate(native-tls-0.2/vendored) >= 0.2.10
Requires:       crate(once-cell-1/default) >= 1.0.0
Requires:       crate(percent-encoding-2/default) >= 2.1.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Requires:       crate(quinn-0.10/ring) >= 0.10.0
Requires:       crate(quinn-0.10/runtime-tokio) >= 0.10.0
Requires:       crate(quinn-0.10/tls-rustls) >= 0.10.0
Requires:       crate(rustls-0.21/dangerous-configuration) >= 0.21.6
Requires:       crate(rustls-0.21/default) >= 0.21.6
Requires:       crate(rustls-native-certs-0.6/default) >= 0.6.0
Requires:       crate(rustls-pemfile-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(serde-urlencoded-0.7/default) >= 0.7.1
Requires:       crate(sync-wrapper-0.1/default) >= 0.1.2
Requires:       crate(system-configuration-0.5/default) >= 0.5.1
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tokio-native-tls-0.3/default) >= 0.3.0
Requires:       crate(tokio-rustls-0.24/default) >= 0.24.0
Requires:       crate(tokio-socks-0.5/default) >= 0.5.1
Requires:       crate(tokio-util-0.7/codec) >= 0.7.1
Requires:       crate(tokio-util-0.7/io) >= 0.7.1
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Requires:       crate(url-2/default) >= 2.2.0
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.68
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.18
Requires:       crate(wasm-streams-0.4/default) >= 0.4.0
Requires:       crate(web-sys-0.3/abortcontroller) >= 0.3.25
Requires:       crate(web-sys-0.3/abortsignal) >= 0.3.25
Requires:       crate(web-sys-0.3/blob) >= 0.3.25
Requires:       crate(web-sys-0.3/blobpropertybag) >= 0.3.25
Requires:       crate(web-sys-0.3/default) >= 0.3.25
Requires:       crate(web-sys-0.3/file) >= 0.3.25
Requires:       crate(web-sys-0.3/formdata) >= 0.3.25
Requires:       crate(web-sys-0.3/headers) >= 0.3.25
Requires:       crate(web-sys-0.3/readablestream) >= 0.3.25
Requires:       crate(web-sys-0.3/request) >= 0.3.25
Requires:       crate(web-sys-0.3/requestcredentials) >= 0.3.25
Requires:       crate(web-sys-0.3/requestinit) >= 0.3.25
Requires:       crate(web-sys-0.3/requestmode) >= 0.3.25
Requires:       crate(web-sys-0.3/response) >= 0.3.25
Requires:       crate(web-sys-0.3/serviceworkerglobalscope) >= 0.3.25
Requires:       crate(web-sys-0.3/window) >= 0.3.25
Requires:       crate(webpki-roots-0.25/default) >= 0.25.0
Requires:       crate(winreg-0.50/default) >= 0.50.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async-compression) = %{version}
Provides:       crate(%{pkgname}/blocking) = %{version}
Provides:       crate(%{pkgname}/brotli) = %{version}
Provides:       crate(%{pkgname}/cookie-crate) = %{version}
Provides:       crate(%{pkgname}/cookie-store) = %{version}
Provides:       crate(%{pkgname}/cookies) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/default-tls) = %{version}
Provides:       crate(%{pkgname}/deflate) = %{version}
Provides:       crate(%{pkgname}/futures-channel) = %{version}
Provides:       crate(%{pkgname}/gzip) = %{version}
Provides:       crate(%{pkgname}/h3) = %{version}
Provides:       crate(%{pkgname}/h3-quinn) = %{version}
Provides:       crate(%{pkgname}/hickory-dns) = %{version}
Provides:       crate(%{pkgname}/hickory-resolver) = %{version}
Provides:       crate(%{pkgname}/http3) = %{version}
Provides:       crate(%{pkgname}/hyper-rustls) = %{version}
Provides:       crate(%{pkgname}/hyper-tls) = %{version}
Provides:       crate(%{pkgname}/internal-proxy-sys-no-cache) = %{version}
Provides:       crate(%{pkgname}/json) = %{version}
Provides:       crate(%{pkgname}/mime-guess) = %{version}
Provides:       crate(%{pkgname}/multipart) = %{version}
Provides:       crate(%{pkgname}/native-tls) = %{version}
Provides:       crate(%{pkgname}/native-tls-alpn) = %{version}
Provides:       crate(%{pkgname}/native-tls-crate) = %{version}
Provides:       crate(%{pkgname}/native-tls-vendored) = %{version}
Provides:       crate(%{pkgname}/quinn) = %{version}
Provides:       crate(%{pkgname}/rustls) = %{version}
Provides:       crate(%{pkgname}/rustls-native-certs) = %{version}
Provides:       crate(%{pkgname}/rustls-tls) = %{version}
Provides:       crate(%{pkgname}/rustls-tls-manual-roots) = %{version}
Provides:       crate(%{pkgname}/rustls-tls-native-roots) = %{version}
Provides:       crate(%{pkgname}/rustls-tls-webpki-roots) = %{version}
Provides:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/socks) = %{version}
Provides:       crate(%{pkgname}/stream) = %{version}
Provides:       crate(%{pkgname}/tls) = %{version}
Provides:       crate(%{pkgname}/tokio-native-tls) = %{version}
Provides:       crate(%{pkgname}/tokio-rustls) = %{version}
Provides:       crate(%{pkgname}/tokio-socks) = %{version}
Provides:       crate(%{pkgname}/tokio-util) = %{version}
Provides:       crate(%{pkgname}/trust-dns) = %{version}
Provides:       crate(%{pkgname}/wasm-streams) = %{version}
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description
Source code for takopackized Rust crate "reqwest"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
