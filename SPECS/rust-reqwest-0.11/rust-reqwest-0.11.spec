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

Requires:       crate(base64-0.21/default) >= 0.21.0
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(encoding-rs-0.8/default) >= 0.8.0
Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(futures-util-0.3) >= 0.3.0
Requires:       crate(h2-0.3/default) >= 0.3.14
Requires:       crate(http-0.2/default) >= 0.2.0
Requires:       crate(http-body-0.4/default) >= 0.4.0
Requires:       crate(hyper-0.14/client) >= 0.14.21
Requires:       crate(hyper-0.14/http1) >= 0.14.21
Requires:       crate(hyper-0.14/http2) >= 0.14.21
Requires:       crate(hyper-0.14/runtime) >= 0.14.21
Requires:       crate(hyper-0.14/tcp) >= 0.14.21
Requires:       crate(ipnet-2/default) >= 2.3.0
Requires:       crate(js-sys-0.3/default) >= 0.3.45
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(mime-0.3/default) >= 0.3.16
Requires:       crate(once-cell-1/default) >= 1.0.0
Requires:       crate(percent-encoding-2/default) >= 2.1.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(serde-urlencoded-0.7/default) >= 0.7.1
Requires:       crate(sync-wrapper-0.1/default) >= 0.1.2
Requires:       crate(system-configuration-0.5/default) >= 0.5.1
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Requires:       crate(url-2/default) >= 2.2.0
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.68
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.18
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
Requires:       crate(winreg-0.50/default) >= 0.50.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/internal-proxy-sys-no-cache) = %{version}

%patchlist
# Keep the private Rustls feature distinct from the optional dependency.
2000-Distinguish-the-internal-Rustls-feature.patch

%description
Source code for takopackized Rust crate "reqwest"

%package     -n %{name}+tls
Summary:        Higher level HTTP client library - feature "__tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-pemfile-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/tls) = %{version}

%description -n %{name}+tls
This metapackage enables feature "__tls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-compression
Summary:        Higher level HTTP client library - feature "async-compression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Provides:       crate(%{pkgname}/async-compression) = %{version}

%description -n %{name}+async-compression
This metapackage enables feature "async-compression" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking
Summary:        Higher level HTTP client library - feature "blocking"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-0.3/io) >= 0.3.0
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}/blocking) = %{version}

%description -n %{name}+blocking
This metapackage enables feature "blocking" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+brotli
Summary:        Higher level HTTP client library - feature "brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-compression) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(async-compression-0.4/brotli) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Provides:       crate(%{pkgname}/brotli) = %{version}

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cookie-crate
Summary:        Higher level HTTP client library - feature "cookie_crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cookie-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/cookie-crate) = %{version}

%description -n %{name}+cookie-crate
This metapackage enables feature "cookie_crate" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cookie-store
Summary:        Higher level HTTP client library - feature "cookie_store"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cookie-store-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/cookie-store) = %{version}

%description -n %{name}+cookie-store
This metapackage enables feature "cookie_store" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cookies
Summary:        Higher level HTTP client library - feature "cookies"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cookie-crate) = %{version}
Requires:       crate(%{pkgname}/cookie-store) = %{version}
Provides:       crate(%{pkgname}/cookies) = %{version}

%description -n %{name}+cookies
This metapackage enables feature "cookies" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default-tls
Summary:        Higher level HTTP client library - feature "default-tls" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hyper-tls) = %{version}
Requires:       crate(%{pkgname}/native-tls-crate) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(%{pkgname}/tokio-native-tls) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/default-tls) = %{version}
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+default-tls
This metapackage enables feature "default-tls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "native-tls" features.

%package     -n %{name}+deflate
Summary:        Higher level HTTP client library - feature "deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-compression) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Requires:       crate(async-compression-0.4/zlib) >= 0.4.0
Provides:       crate(%{pkgname}/deflate) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-channel
Summary:        Higher level HTTP client library - feature "futures-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-channel) = %{version}

%description -n %{name}+futures-channel
This metapackage enables feature "futures-channel" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gzip
Summary:        Higher level HTTP client library - feature "gzip"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-compression) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(async-compression-0.4/gzip) >= 0.4.0
Requires:       crate(async-compression-0.4/tokio) >= 0.4.0
Provides:       crate(%{pkgname}/gzip) = %{version}

%description -n %{name}+gzip
This metapackage enables feature "gzip" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3
Summary:        Higher level HTTP client library - feature "h3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(h3-0.0.3/default) >= 0.0.3
Provides:       crate(%{pkgname}/h3) = %{version}

%description -n %{name}+h3
This metapackage enables feature "h3" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3-quinn
Summary:        Higher level HTTP client library - feature "h3-quinn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(h3-quinn-0.0.4/default) >= 0.0.4
Provides:       crate(%{pkgname}/h3-quinn) = %{version}

%description -n %{name}+h3-quinn
This metapackage enables feature "h3-quinn" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hickory-resolver
Summary:        Higher level HTTP client library - feature "hickory-resolver" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-resolver-0.24/default) >= 0.24.0
Requires:       crate(hickory-resolver-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/hickory-dns) = %{version}
Provides:       crate(%{pkgname}/hickory-resolver) = %{version}
Provides:       crate(%{pkgname}/trust-dns) = %{version}

%description -n %{name}+hickory-resolver
This metapackage enables feature "hickory-resolver" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "hickory-dns", and "trust-dns" features.

%package     -n %{name}+http3
Summary:        Higher level HTTP client library - feature "http3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-channel) = %{version}
Requires:       crate(%{pkgname}/h3) = %{version}
Requires:       crate(%{pkgname}/h3-quinn) = %{version}
Requires:       crate(%{pkgname}/quinn) = %{version}
Requires:       crate(%{pkgname}/rustls-tls-manual-roots) = %{version}
Provides:       crate(%{pkgname}/http3) = %{version}

%description -n %{name}+http3
This metapackage enables feature "http3" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hyper-rustls
Summary:        Higher level HTTP client library - feature "hyper-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-rustls-0.24) >= 0.24.0
Provides:       crate(%{pkgname}/hyper-rustls) = %{version}

%description -n %{name}+hyper-rustls
This metapackage enables feature "hyper-rustls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hyper-tls
Summary:        Higher level HTTP client library - feature "hyper-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-tls-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/hyper-tls) = %{version}

%description -n %{name}+hyper-tls
This metapackage enables feature "hyper-tls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+internal-rustls
Summary:        Higher level HTTP client library - feature "internal-rustls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hyper-rustls) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(%{pkgname}/tokio-rustls) = %{version}
Provides:       crate(%{pkgname}/internal-rustls) = %{version}
Provides:       crate(%{pkgname}/rustls-tls-manual-roots) = %{version}

%description -n %{name}+internal-rustls
This metapackage enables feature "internal-rustls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls-tls-manual-roots" feature.

%package     -n %{name}+mime-guess
Summary:        Higher level HTTP client library - feature "mime_guess" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mime-guess-2) >= 2.0.0
Provides:       crate(%{pkgname}/mime-guess) = %{version}
Provides:       crate(%{pkgname}/multipart) = %{version}

%description -n %{name}+mime-guess
This metapackage enables feature "mime_guess" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "multipart" feature.

%package     -n %{name}+native-tls-alpn
Summary:        Higher level HTTP client library - feature "native-tls-alpn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/native-tls) = %{version}
Requires:       crate(native-tls-0.2/alpn) >= 0.2.10
Provides:       crate(%{pkgname}/native-tls-alpn) = %{version}

%description -n %{name}+native-tls-alpn
This metapackage enables feature "native-tls-alpn" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-crate
Summary:        Higher level HTTP client library - feature "native-tls-crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(native-tls-0.2/default) >= 0.2.10
Provides:       crate(%{pkgname}/native-tls-crate) = %{version}

%description -n %{name}+native-tls-crate
This metapackage enables feature "native-tls-crate" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-vendored
Summary:        Higher level HTTP client library - feature "native-tls-vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/native-tls) = %{version}
Requires:       crate(native-tls-0.2/vendored) >= 0.2.10
Provides:       crate(%{pkgname}/native-tls-vendored) = %{version}

%description -n %{name}+native-tls-vendored
This metapackage enables feature "native-tls-vendored" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quinn
Summary:        Higher level HTTP client library - feature "quinn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-0.10/ring) >= 0.10.0
Requires:       crate(quinn-0.10/runtime-tokio) >= 0.10.0
Requires:       crate(quinn-0.10/tls-rustls) >= 0.10.0
Provides:       crate(%{pkgname}/quinn) = %{version}

%description -n %{name}+quinn
This metapackage enables feature "quinn" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Higher level HTTP client library - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.21/dangerous-configuration) >= 0.21.6
Requires:       crate(rustls-0.21/default) >= 0.21.6
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-native-certs
Summary:        Higher level HTTP client library - feature "rustls-native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-native-certs-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/rustls-native-certs) = %{version}

%description -n %{name}+rustls-native-certs
This metapackage enables feature "rustls-native-certs" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls-native-roots
Summary:        Higher level HTTP client library - feature "rustls-tls-native-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/internal-rustls) = %{version}
Requires:       crate(%{pkgname}/rustls-native-certs) = %{version}
Provides:       crate(%{pkgname}/rustls-tls-native-roots) = %{version}

%description -n %{name}+rustls-tls-native-roots
This metapackage enables feature "rustls-tls-native-roots" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls-webpki-roots
Summary:        Higher level HTTP client library - feature "rustls-tls-webpki-roots" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/internal-rustls) = %{version}
Requires:       crate(%{pkgname}/webpki-roots) = %{version}
Provides:       crate(%{pkgname}/rustls-tls) = %{version}
Provides:       crate(%{pkgname}/rustls-tls-webpki-roots) = %{version}

%description -n %{name}+rustls-tls-webpki-roots
This metapackage enables feature "rustls-tls-webpki-roots" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls-tls" feature.

%package     -n %{name}+serde-json
Summary:        Higher level HTTP client library - feature "serde_json" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/json) = %{version}
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json" feature.

%package     -n %{name}+stream
Summary:        Higher level HTTP client library - feature "stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(%{pkgname}/wasm-streams) = %{version}
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}/stream) = %{version}

%description -n %{name}+stream
This metapackage enables feature "stream" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-native-tls
Summary:        Higher level HTTP client library - feature "tokio-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-native-tls-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/tokio-native-tls) = %{version}

%description -n %{name}+tokio-native-tls
This metapackage enables feature "tokio-native-tls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-rustls
Summary:        Higher level HTTP client library - feature "tokio-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-rustls-0.24/default) >= 0.24.0
Provides:       crate(%{pkgname}/tokio-rustls) = %{version}

%description -n %{name}+tokio-rustls
This metapackage enables feature "tokio-rustls" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-socks
Summary:        Higher level HTTP client library - feature "tokio-socks" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-socks-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}/socks) = %{version}
Provides:       crate(%{pkgname}/tokio-socks) = %{version}

%description -n %{name}+tokio-socks
This metapackage enables feature "tokio-socks" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "socks" feature.

%package     -n %{name}+tokio-util
Summary:        Higher level HTTP client library - feature "tokio-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-util-0.7/codec) >= 0.7.1
Requires:       crate(tokio-util-0.7/io) >= 0.7.1
Provides:       crate(%{pkgname}/tokio-util) = %{version}

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-streams
Summary:        Higher level HTTP client library - feature "wasm-streams"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-streams-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/wasm-streams) = %{version}

%description -n %{name}+wasm-streams
This metapackage enables feature "wasm-streams" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Higher level HTTP client library - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-roots-0.25/default) >= 0.25.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This metapackage enables feature "webpki-roots" for the Rust reqwest crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
