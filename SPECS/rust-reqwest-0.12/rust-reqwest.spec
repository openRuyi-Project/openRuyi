# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name reqwest
%global full_version 0.12.28
%global pkgname reqwest-0.12

Name:           rust-reqwest-0.12
Version:        0.12.28
Release:        %autorelease
Summary:        Rust crate "reqwest"
License:        MIT OR Apache-2.0
URL:            https://github.com/seanmonstar/reqwest
#!RemoteAsset:  sha256:eddd3ca559203180a307f12d114c268abf583f59b03cb906fd0b3ff8646c1147
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(bytes-1.0/default) >= 1.11.1
Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(http-1.0/default) >= 1.4.0
Requires:       crate(http-body-1.0/default) >= 1.0.1
Requires:       crate(http-body-util-0.1/default) >= 0.1.3
Requires:       crate(hyper-1.0/client) >= 1.9.0
Requires:       crate(hyper-1.0/default) >= 1.9.0
Requires:       crate(hyper-1.0/http1) >= 1.9.0
Requires:       crate(hyper-util-0.1/client) >= 0.1.20
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.20
Requires:       crate(hyper-util-0.1/client-proxy) >= 0.1.20
Requires:       crate(hyper-util-0.1/default) >= 0.1.20
Requires:       crate(hyper-util-0.1/http1) >= 0.1.20
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.20
Requires:       crate(js-sys-0.3/default) >= 0.3.94
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(percent-encoding-2.0/default) >= 2.3.2
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(serde-urlencoded-0.7/default) >= 0.7.1
Requires:       crate(sync-wrapper-1.0/default) >= 1.0.2
Requires:       crate(sync-wrapper-1.0/futures) >= 1.0.2
Requires:       crate(tokio-1.0/net) >= 1.50.0
Requires:       crate(tokio-1.0/time) >= 1.50.0
Requires:       crate(tower-0.5/retry) >= 0.5.3
Requires:       crate(tower-0.5/timeout) >= 0.5.3
Requires:       crate(tower-0.5/util) >= 0.5.3
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.8
Requires:       crate(tower-service-0.3/default) >= 0.3.3
Requires:       crate(url-2.0/default) >= 2.5.8
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.117
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.67
Requires:       crate(web-sys-0.3/abortcontroller) >= 0.3.94
Requires:       crate(web-sys-0.3/abortsignal) >= 0.3.94
Requires:       crate(web-sys-0.3/blob) >= 0.3.94
Requires:       crate(web-sys-0.3/blobpropertybag) >= 0.3.94
Requires:       crate(web-sys-0.3/default) >= 0.3.94
Requires:       crate(web-sys-0.3/file) >= 0.3.94
Requires:       crate(web-sys-0.3/formdata) >= 0.3.94
Requires:       crate(web-sys-0.3/headers) >= 0.3.94
Requires:       crate(web-sys-0.3/readablestream) >= 0.3.94
Requires:       crate(web-sys-0.3/request) >= 0.3.94
Requires:       crate(web-sys-0.3/requestcache) >= 0.3.94
Requires:       crate(web-sys-0.3/requestcredentials) >= 0.3.94
Requires:       crate(web-sys-0.3/requestinit) >= 0.3.94
Requires:       crate(web-sys-0.3/requestmode) >= 0.3.94
Requires:       crate(web-sys-0.3/response) >= 0.3.94
Requires:       crate(web-sys-0.3/serviceworkerglobalscope) >= 0.3.94
Requires:       crate(web-sys-0.3/window) >= 0.3.94
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/socks)
Provides:       crate(%{pkgname}/trust-dns)

%description
Source code for takopackized Rust crate "reqwest"

%package     -n %{name}+rustls
Summary:        Higher level HTTP client library - feature "__rustls" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/tls)
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.7
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.7
Requires:       crate(rustls-0.23/std) >= 0.23.4
Requires:       crate(rustls-0.23/tls12) >= 0.23.4
Requires:       crate(tokio-rustls-0.26/tls12) >= 0.26.0
Provides:       crate(%{pkgname}/rustls)
Provides:       crate(%{pkgname}/rustls-tls-manual-roots-no-provider)
Provides:       crate(%{pkgname}/rustls-tls-no-provider)

%description -n %{name}+rustls
This metapackage enables feature "__rustls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls-tls-manual-roots-no-provider", and "rustls-tls-no-provider" features.

%package     -n %{name}+rustls-ring
Summary:        Higher level HTTP client library - feature "__rustls-ring"
Requires:       crate(%{pkgname})
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.7
Requires:       crate(hyper-rustls-0.27/ring) >= 0.27.7
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.7
Requires:       crate(quinn-0.11/ring) >= 0.11.1
Requires:       crate(quinn-0.11/runtime-tokio) >= 0.11.1
Requires:       crate(quinn-0.11/rustls) >= 0.11.1
Requires:       crate(rustls-0.23/ring) >= 0.23.4
Requires:       crate(rustls-0.23/std) >= 0.23.4
Requires:       crate(rustls-0.23/tls12) >= 0.23.4
Requires:       crate(tokio-rustls-0.26/ring) >= 0.26.0
Requires:       crate(tokio-rustls-0.26/tls12) >= 0.26.0
Provides:       crate(%{pkgname}/rustls-ring)

%description -n %{name}+rustls-ring
This metapackage enables feature "__rustls-ring" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls
Summary:        Higher level HTTP client library - feature "__tls"
Requires:       crate(%{pkgname})
Requires:       crate(rustls-pki-types-1.0/default) >= 1.9.0
Requires:       crate(rustls-pki-types-1.0/std) >= 1.9.0
Requires:       crate(tokio-1.0/io-util) >= 1.50.0
Requires:       crate(tokio-1.0/net) >= 1.50.0
Requires:       crate(tokio-1.0/time) >= 1.50.0
Provides:       crate(%{pkgname}/tls)

%description -n %{name}+tls
This metapackage enables feature "__tls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking
Summary:        Higher level HTTP client library - feature "blocking"
Requires:       crate(%{pkgname})
Requires:       crate(futures-channel-0.3/default) >= 0.3.32
Requires:       crate(futures-channel-0.3/sink) >= 0.3.32
Requires:       crate(futures-util-0.3) >= 0.3.32
Requires:       crate(futures-util-0.3/io) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Requires:       crate(tokio-1.0/net) >= 1.50.0
Requires:       crate(tokio-1.0/sync) >= 1.50.0
Requires:       crate(tokio-1.0/time) >= 1.50.0
Provides:       crate(%{pkgname}/blocking)

%description -n %{name}+blocking
This metapackage enables feature "blocking" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+brotli
Summary:        Higher level HTTP client library - feature "brotli"
Requires:       crate(%{pkgname})
Requires:       crate(tower-http-0.6/decompression-br) >= 0.6.8
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.8
Provides:       crate(%{pkgname}/brotli)

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+charset
Summary:        Higher level HTTP client library - feature "charset"
Requires:       crate(%{pkgname})
Requires:       crate(encoding-rs-0.8/default) >= 0.8.35
Requires:       crate(mime-0.3/default) >= 0.3.17
Provides:       crate(%{pkgname}/charset)

%description -n %{name}+charset
This metapackage enables feature "charset" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cookies
Summary:        Higher level HTTP client library - feature "cookies"
Requires:       crate(%{pkgname})
Requires:       crate(cookie-0.18/default) >= 0.18.0
Requires:       crate(cookie-store-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/cookies)

%description -n %{name}+cookies
This metapackage enables feature "cookies" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Higher level HTTP client library - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/charset)
Requires:       crate(%{pkgname}/default-tls)
Requires:       crate(%{pkgname}/http2)
Requires:       crate(%{pkgname}/system-proxy)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default-tls
Summary:        Higher level HTTP client library - feature "default-tls" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/tls)
Requires:       crate(hyper-tls-0.6/default) >= 0.6.0
Requires:       crate(native-tls-0.2/default) >= 0.2.10
Requires:       crate(tokio-native-tls-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/default-tls)
Provides:       crate(%{pkgname}/native-tls)

%description -n %{name}+default-tls
This metapackage enables feature "default-tls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "native-tls" feature.

%package     -n %{name}+deflate
Summary:        Higher level HTTP client library - feature "deflate"
Requires:       crate(%{pkgname})
Requires:       crate(tower-http-0.6/decompression-deflate) >= 0.6.8
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.8
Provides:       crate(%{pkgname}/deflate)

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gzip
Summary:        Higher level HTTP client library - feature "gzip"
Requires:       crate(%{pkgname})
Requires:       crate(tower-http-0.6/decompression-gzip) >= 0.6.8
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.8
Provides:       crate(%{pkgname}/gzip)

%description -n %{name}+gzip
This metapackage enables feature "gzip" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h2
Summary:        Higher level HTTP client library - feature "h2"
Requires:       crate(%{pkgname})
Requires:       crate(h2-0.4/default) >= 0.4.13
Provides:       crate(%{pkgname}/h2)

%description -n %{name}+h2
This metapackage enables feature "h2" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hickory-dns
Summary:        Higher level HTTP client library - feature "hickory-dns"
Requires:       crate(%{pkgname})
Requires:       crate(hickory-resolver-0.25/default) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Requires:       crate(once-cell-1.0/default) >= 1.18
Provides:       crate(%{pkgname}/hickory-dns)

%description -n %{name}+hickory-dns
This metapackage enables feature "hickory-dns" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http2
Summary:        Higher level HTTP client library - feature "http2"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/h2)
Requires:       crate(hyper-1.0/client) >= 1.9.0
Requires:       crate(hyper-1.0/http1) >= 1.9.0
Requires:       crate(hyper-1.0/http2) >= 1.9.0
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.7
Requires:       crate(hyper-rustls-0.27/http2) >= 0.27.7
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.7
Requires:       crate(hyper-util-0.1/client) >= 0.1.20
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.20
Requires:       crate(hyper-util-0.1/client-proxy) >= 0.1.20
Requires:       crate(hyper-util-0.1/http1) >= 0.1.20
Requires:       crate(hyper-util-0.1/http2) >= 0.1.20
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.20
Provides:       crate(%{pkgname}/http2)

%description -n %{name}+http2
This metapackage enables feature "http2" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http3
Summary:        Higher level HTTP client library - feature "http3"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rustls-tls-manual-roots)
Requires:       crate(h3-0.0.8/default) >= 0.0.8
Requires:       crate(h3-quinn-0.0.10/default) >= 0.0.10
Requires:       crate(quinn-0.11/runtime-tokio) >= 0.11.1
Requires:       crate(quinn-0.11/rustls) >= 0.11.1
Requires:       crate(tokio-1.0/macros) >= 1.50.0
Requires:       crate(tokio-1.0/net) >= 1.50.0
Requires:       crate(tokio-1.0/time) >= 1.50.0
Provides:       crate(%{pkgname}/http3)

%description -n %{name}+http3
This metapackage enables feature "http3" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Higher level HTTP client library - feature "json"
Requires:       crate(%{pkgname})
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Provides:       crate(%{pkgname}/json)

%description -n %{name}+json
This metapackage enables feature "json" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+multipart
Summary:        Higher level HTTP client library - feature "multipart"
Requires:       crate(%{pkgname})
Requires:       crate(futures-util-0.3) >= 0.3.32
Requires:       crate(mime-guess-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/multipart)

%description -n %{name}+multipart
This metapackage enables feature "multipart" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-alpn
Summary:        Higher level HTTP client library - feature "native-tls-alpn"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/native-tls)
Requires:       crate(hyper-tls-0.6/alpn) >= 0.6.0
Requires:       crate(native-tls-0.2/alpn) >= 0.2.10
Provides:       crate(%{pkgname}/native-tls-alpn)

%description -n %{name}+native-tls-alpn
This metapackage enables feature "native-tls-alpn" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-vendored
Summary:        Higher level HTTP client library - feature "native-tls-vendored"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/native-tls)
Requires:       crate(native-tls-0.2/vendored) >= 0.2.10
Provides:       crate(%{pkgname}/native-tls-vendored)

%description -n %{name}+native-tls-vendored
This metapackage enables feature "native-tls-vendored" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls-manual-roots
Summary:        Higher level HTTP client library - feature "rustls-tls-manual-roots"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rustls-ring)
Requires:       crate(%{pkgname}/rustls-tls-manual-roots-no-provider)
Provides:       crate(%{pkgname}/rustls-tls-manual-roots)

%description -n %{name}+rustls-tls-manual-roots
This metapackage enables feature "rustls-tls-manual-roots" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls-native-roots
Summary:        Higher level HTTP client library - feature "rustls-tls-native-roots"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rustls-ring)
Requires:       crate(%{pkgname}/rustls-tls-native-roots-no-provider)
Provides:       crate(%{pkgname}/rustls-tls-native-roots)

%description -n %{name}+rustls-tls-native-roots
This metapackage enables feature "rustls-tls-native-roots" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls-native-roots-no-provider
Summary:        Higher level HTTP client library - feature "rustls-tls-native-roots-no-provider"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rustls)
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.7
Requires:       crate(hyper-rustls-0.27/native-tokio) >= 0.27.7
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.7
Requires:       crate(rustls-native-certs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rustls-tls-native-roots-no-provider)

%description -n %{name}+rustls-tls-native-roots-no-provider
This metapackage enables feature "rustls-tls-native-roots-no-provider" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls-webpki-roots
Summary:        Higher level HTTP client library - feature "rustls-tls-webpki-roots" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rustls-ring)
Requires:       crate(%{pkgname}/rustls-tls-webpki-roots-no-provider)
Provides:       crate(%{pkgname}/rustls-tls)
Provides:       crate(%{pkgname}/rustls-tls-webpki-roots)

%description -n %{name}+rustls-tls-webpki-roots
This metapackage enables feature "rustls-tls-webpki-roots" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls-tls" feature.

%package     -n %{name}+rustls-tls-webpki-roots-no-provider
Summary:        Higher level HTTP client library - feature "rustls-tls-webpki-roots-no-provider"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rustls)
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.7
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.7
Requires:       crate(hyper-rustls-0.27/webpki-tokio) >= 0.27.7
Requires:       crate(webpki-roots-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/rustls-tls-webpki-roots-no-provider)

%description -n %{name}+rustls-tls-webpki-roots-no-provider
This metapackage enables feature "rustls-tls-webpki-roots-no-provider" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stream
Summary:        Higher level HTTP client library - feature "stream"
Requires:       crate(%{pkgname})
Requires:       crate(futures-util-0.3) >= 0.3.32
Requires:       crate(tokio-1.0/fs) >= 1.50.0
Requires:       crate(tokio-1.0/net) >= 1.50.0
Requires:       crate(tokio-1.0/time) >= 1.50.0
Requires:       crate(tokio-util-0.7/io) >= 0.7.9
Requires:       crate(wasm-streams-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/stream)

%description -n %{name}+stream
This metapackage enables feature "stream" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system-proxy
Summary:        Higher level HTTP client library - feature "system-proxy" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(hyper-util-0.1/client) >= 0.1.20
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.20
Requires:       crate(hyper-util-0.1/client-proxy) >= 0.1.20
Requires:       crate(hyper-util-0.1/client-proxy-system) >= 0.1.20
Requires:       crate(hyper-util-0.1/http1) >= 0.1.20
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.20
Provides:       crate(%{pkgname}/macos-system-configuration)
Provides:       crate(%{pkgname}/system-proxy)

%description -n %{name}+system-proxy
This metapackage enables feature "system-proxy" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "macos-system-configuration" feature.

%package     -n %{name}+zstd
Summary:        Higher level HTTP client library - feature "zstd"
Requires:       crate(%{pkgname})
Requires:       crate(tower-http-0.6/decompression-zstd) >= 0.6.8
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.8
Provides:       crate(%{pkgname}/zstd)

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
