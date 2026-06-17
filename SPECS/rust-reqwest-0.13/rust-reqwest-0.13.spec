# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name reqwest
%global full_version 0.13.2
%global pkgname reqwest-0.13

Name:           rust-reqwest-0.13
Version:        0.13.2
Release:        %autorelease
Summary:        Rust crate "reqwest"
License:        MIT OR Apache-2.0
URL:            https://github.com/seanmonstar/reqwest
#!RemoteAsset:  sha256:ab3f43e3283ab1488b624b44b0e988d0acea0b3214e694730a055cb6b2efa801
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(bytes-1/default) >= 1.2.0
Requires:       crate(futures-core-0.3) >= 0.3.28
Requires:       crate(http-1/default) >= 1.1.0
Requires:       crate(http-body-1/default) >= 1.0.0
Requires:       crate(http-body-util-0.1/default) >= 0.1.2
Requires:       crate(hyper-1/client) >= 1.1.0
Requires:       crate(hyper-1/default) >= 1.1.0
Requires:       crate(hyper-1/http1) >= 1.1.0
Requires:       crate(hyper-util-0.1/client) >= 0.1.12
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.12
Requires:       crate(hyper-util-0.1/client-proxy) >= 0.1.12
Requires:       crate(hyper-util-0.1/default) >= 0.1.12
Requires:       crate(hyper-util-0.1/http1) >= 0.1.12
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.12
Requires:       crate(js-sys-0.3/default) >= 0.3.77
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(percent-encoding-2/default) >= 2.3.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.11
Requires:       crate(sync-wrapper-1/default) >= 1.0.0
Requires:       crate(sync-wrapper-1/futures) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tower-0.5/retry) >= 0.5.2
Requires:       crate(tower-0.5/timeout) >= 0.5.2
Requires:       crate(tower-0.5/util) >= 0.5.2
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.8
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Requires:       crate(url-2/default) >= 2.4.0
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.89
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.18
Requires:       crate(web-sys-0.3/abortcontroller) >= 0.3.28
Requires:       crate(web-sys-0.3/abortsignal) >= 0.3.28
Requires:       crate(web-sys-0.3/blob) >= 0.3.28
Requires:       crate(web-sys-0.3/blobpropertybag) >= 0.3.28
Requires:       crate(web-sys-0.3/default) >= 0.3.28
Requires:       crate(web-sys-0.3/file) >= 0.3.28
Requires:       crate(web-sys-0.3/formdata) >= 0.3.28
Requires:       crate(web-sys-0.3/headers) >= 0.3.28
Requires:       crate(web-sys-0.3/readablestream) >= 0.3.28
Requires:       crate(web-sys-0.3/request) >= 0.3.28
Requires:       crate(web-sys-0.3/requestcache) >= 0.3.28
Requires:       crate(web-sys-0.3/requestcredentials) >= 0.3.28
Requires:       crate(web-sys-0.3/requestinit) >= 0.3.28
Requires:       crate(web-sys-0.3/requestmode) >= 0.3.28
Requires:       crate(web-sys-0.3/response) >= 0.3.28
Requires:       crate(web-sys-0.3/serviceworkerglobalscope) >= 0.3.28
Requires:       crate(web-sys-0.3/window) >= 0.3.28
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/socks) = %{version}

%description
Source code for takopackized Rust crate "reqwest"

%package     -n %{name}+native-tls-no-alpn
Summary:        Higher level HTTP client library - feature "__native-tls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(hyper-tls-0.6/default) >= 0.6.0
Requires:       crate(native-tls-0.2/default) >= 0.2.10
Requires:       crate(tokio-native-tls-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/native-tls-no-alpn) = %{version}

%description -n %{name}+native-tls-no-alpn
This metapackage enables feature "__native-tls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "native-tls-no-alpn" feature.

%package     -n %{name}+native-tls-alpn
Summary:        Higher level HTTP client library - feature "__native-tls-alpn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-tls-0.6/alpn) >= 0.6.0
Requires:       crate(native-tls-0.2/alpn) >= 0.2.10
Provides:       crate(%{pkgname}/native-tls-alpn) = %{version}

%description -n %{name}+native-tls-alpn
This metapackage enables feature "__native-tls-alpn" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-no-provider
Summary:        Higher level HTTP client library - feature "__rustls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.0
Requires:       crate(rustls-0.23/std) >= 0.23.4
Requires:       crate(rustls-0.23/tls12) >= 0.23.4
Requires:       crate(rustls-platform-verifier-0.6/default) >= 0.6.0
Requires:       crate(tokio-rustls-0.26/tls12) >= 0.26.0
Provides:       crate(%{pkgname}/rustls-no-provider) = %{version}

%description -n %{name}+rustls-no-provider
This metapackage enables feature "__rustls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls-no-provider" feature.

%package     -n %{name}+rustls-aws-lc-rs
Summary:        Higher level HTTP client library - feature "__rustls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-rustls-0.27/aws-lc-rs) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.0
Requires:       crate(quinn-0.11/runtime-tokio) >= 0.11.1
Requires:       crate(quinn-0.11/rustls-aws-lc-rs) >= 0.11.1
Requires:       crate(rustls-0.23/aws-lc-rs) >= 0.23.4
Requires:       crate(rustls-0.23/std) >= 0.23.4
Requires:       crate(rustls-0.23/tls12) >= 0.23.4
Requires:       crate(tokio-rustls-0.26/aws-lc-rs) >= 0.26.0
Requires:       crate(tokio-rustls-0.26/tls12) >= 0.26.0
Provides:       crate(%{pkgname}/rustls-aws-lc-rs) = %{version}

%description -n %{name}+rustls-aws-lc-rs
This metapackage enables feature "__rustls-aws-lc-rs" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls
Summary:        Higher level HTTP client library - feature "__tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-pki-types-1/default) >= 1.9.0
Requires:       crate(rustls-pki-types-1/std) >= 1.9.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}/tls) = %{version}

%description -n %{name}+tls
This metapackage enables feature "__tls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking
Summary:        Higher level HTTP client library - feature "blocking"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Requires:       crate(futures-channel-0.3/sink) >= 0.3.0
Requires:       crate(futures-util-0.3) >= 0.3.28
Requires:       crate(futures-util-0.3/io) >= 0.3.28
Requires:       crate(futures-util-0.3/sink) >= 0.3.28
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}/blocking) = %{version}

%description -n %{name}+blocking
This metapackage enables feature "blocking" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+brotli
Summary:        Higher level HTTP client library - feature "brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tower-http-0.6/decompression-br) >= 0.6.8
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.8
Provides:       crate(%{pkgname}/brotli) = %{version}

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+charset
Summary:        Higher level HTTP client library - feature "charset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encoding-rs-0.8/default) >= 0.8.0
Requires:       crate(mime-0.3/default) >= 0.3.16
Provides:       crate(%{pkgname}/charset) = %{version}

%description -n %{name}+charset
This metapackage enables feature "charset" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cookies
Summary:        Higher level HTTP client library - feature "cookies"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cookie-0.18/default) >= 0.18.0
Requires:       crate(cookie-store-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/cookies) = %{version}

%description -n %{name}+cookies
This metapackage enables feature "cookies" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Higher level HTTP client library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/charset) = %{version}
Requires:       crate(%{pkgname}/default-tls) = %{version}
Requires:       crate(%{pkgname}/http2) = %{version}
Requires:       crate(%{pkgname}/system-proxy) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        Higher level HTTP client library - feature "deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tower-http-0.6/decompression-deflate) >= 0.6.8
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.8
Provides:       crate(%{pkgname}/deflate) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+form
Summary:        Higher level HTTP client library - feature "form" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-urlencoded-0.7/default) >= 0.7.1
Provides:       crate(%{pkgname}/form) = %{version}
Provides:       crate(%{pkgname}/query) = %{version}

%description -n %{name}+form
This metapackage enables feature "form" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "query" feature.

%package     -n %{name}+gzip
Summary:        Higher level HTTP client library - feature "gzip"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tower-http-0.6/decompression-gzip) >= 0.6.8
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.8
Provides:       crate(%{pkgname}/gzip) = %{version}

%description -n %{name}+gzip
This metapackage enables feature "gzip" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hickory-dns
Summary:        Higher level HTTP client library - feature "hickory-dns"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-resolver-0.25/default) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Requires:       crate(once-cell-1/default) >= 1.18.0
Provides:       crate(%{pkgname}/hickory-dns) = %{version}

%description -n %{name}+hickory-dns
This metapackage enables feature "hickory-dns" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http2
Summary:        Higher level HTTP client library - feature "http2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(h2-0.4/default) >= 0.4.0
Requires:       crate(hyper-1/client) >= 1.1.0
Requires:       crate(hyper-1/http1) >= 1.1.0
Requires:       crate(hyper-1/http2) >= 1.1.0
Requires:       crate(hyper-rustls-0.27/http1) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/http2) >= 0.27.0
Requires:       crate(hyper-rustls-0.27/tls12) >= 0.27.0
Requires:       crate(hyper-util-0.1/client) >= 0.1.12
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.12
Requires:       crate(hyper-util-0.1/client-proxy) >= 0.1.12
Requires:       crate(hyper-util-0.1/http1) >= 0.1.12
Requires:       crate(hyper-util-0.1/http2) >= 0.1.12
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.12
Provides:       crate(%{pkgname}/http2) = %{version}

%description -n %{name}+http2
This metapackage enables feature "http2" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http3
Summary:        Higher level HTTP client library - feature "http3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(h3-0.0.8/default) >= 0.0.8
Requires:       crate(h3-quinn-0.0.10/default) >= 0.0.10
Requires:       crate(quinn-0.11/runtime-tokio) >= 0.11.1
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}/http3) = %{version}

%description -n %{name}+http3
This metapackage enables feature "http3" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Higher level HTTP client library - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+multipart
Summary:        Higher level HTTP client library - feature "multipart"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-0.3) >= 0.3.28
Requires:       crate(mime-guess-2) >= 2.0.0
Provides:       crate(%{pkgname}/multipart) = %{version}

%description -n %{name}+multipart
This metapackage enables feature "multipart" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        Higher level HTTP client library - feature "native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/native-tls-alpn) = %{version}
Requires:       crate(%{pkgname}/native-tls-no-alpn) = %{version}
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-vendored
Summary:        Higher level HTTP client library - feature "native-tls-vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/native-tls) = %{version}
Requires:       crate(%{pkgname}/native-tls-alpn) = %{version}
Requires:       crate(native-tls-0.2/vendored) >= 0.2.10
Provides:       crate(%{pkgname}/native-tls-vendored) = %{version}

%description -n %{name}+native-tls-vendored
This metapackage enables feature "native-tls-vendored" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-vendored-no-alpn
Summary:        Higher level HTTP client library - feature "native-tls-vendored-no-alpn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/native-tls) = %{version}
Requires:       crate(native-tls-0.2/vendored) >= 0.2.10
Provides:       crate(%{pkgname}/native-tls-vendored-no-alpn) = %{version}

%description -n %{name}+native-tls-vendored-no-alpn
This metapackage enables feature "native-tls-vendored-no-alpn" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Higher level HTTP client library - feature "rustls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-aws-lc-rs) = %{version}
Requires:       crate(%{pkgname}/rustls-no-provider) = %{version}
Requires:       crate(rustls-platform-verifier-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/default-tls) = %{version}
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default-tls" feature.

%package     -n %{name}+stream
Summary:        Higher level HTTP client library - feature "stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-0.3) >= 0.3.28
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tokio-util-0.7/io) >= 0.7.9
Requires:       crate(wasm-streams-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/stream) = %{version}

%description -n %{name}+stream
This metapackage enables feature "stream" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system-proxy
Summary:        Higher level HTTP client library - feature "system-proxy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-util-0.1/client) >= 0.1.12
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.12
Requires:       crate(hyper-util-0.1/client-proxy) >= 0.1.12
Requires:       crate(hyper-util-0.1/client-proxy-system) >= 0.1.12
Requires:       crate(hyper-util-0.1/http1) >= 0.1.12
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.12
Provides:       crate(%{pkgname}/system-proxy) = %{version}

%description -n %{name}+system-proxy
This metapackage enables feature "system-proxy" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        Higher level HTTP client library - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tower-http-0.6/decompression-zstd) >= 0.6.8
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.8
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
