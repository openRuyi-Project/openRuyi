# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hickory-proto
%global full_version 0.24.4
%global pkgname hickory-proto-0.24

Name:           rust-hickory-proto-0.24
Version:        0.24.4
Release:        %autorelease
Summary:        Rust crate "hickory-proto"
License:        MIT OR Apache-2.0
URL:            https://hickory-dns.org/
#!RemoteAsset:  sha256:92652067c9ce6f66ce53cc38d1169daa36e6e7eb7dd3b63b5103bd9d97117248
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.43
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(data-encoding-2/default) >= 2.2.0
Requires:       crate(enum-as-inner-0.6/default) >= 0.6.0
Requires:       crate(futures-channel-0.3/std) >= 0.3.5
Requires:       crate(futures-io-0.3/std) >= 0.3.5
Requires:       crate(futures-util-0.3/std) >= 0.3.5
Requires:       crate(idna-1/default) >= 1.0.0
Requires:       crate(ipnet-2/default) >= 2.3.0
Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(rand-0.8/default) >= 0.8.0
Requires:       crate(thiserror-1/default) >= 1.0.20
Requires:       crate(tinyvec-1/alloc) >= 1.1.1
Requires:       crate(tinyvec-1/default) >= 1.1.1
Requires:       crate(tracing-0.1/default) >= 0.1.30
Requires:       crate(url-2/default) >= 2.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/dns-over-tls) = %{version}
Provides:       crate(%{pkgname}/dnssec) = %{version}
Provides:       crate(%{pkgname}/testing) = %{version}
Provides:       crate(%{pkgname}/text-parsing) = %{version}

%description
This is the foundational DNS protocol library for all Hickory DNS projects.
Source code for takopackized Rust crate "hickory-proto"

%package     -n %{name}+backtrace
Summary:        Hickory DNS is a safe and secure DNS library - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.50
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "backtrace" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Hickory DNS is a safe and secure DNS library - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "bytes" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-h3
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-h3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-quic) = %{version}
Requires:       crate(%{pkgname}/h3) = %{version}
Requires:       crate(%{pkgname}/h3-quinn) = %{version}
Requires:       crate(%{pkgname}/http) = %{version}
Requires:       crate(%{pkgname}/quinn) = %{version}
Provides:       crate(%{pkgname}/dns-over-h3) = %{version}

%description -n %{name}+dns-over-h3
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "dns-over-h3" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-https
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-https" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytes) = %{version}
Requires:       crate(%{pkgname}/dns-over-rustls) = %{version}
Requires:       crate(%{pkgname}/h2) = %{version}
Requires:       crate(%{pkgname}/http) = %{version}
Requires:       crate(%{pkgname}/tokio-runtime) = %{version}
Provides:       crate(%{pkgname}/dns-over-https) = %{version}
Provides:       crate(%{pkgname}/dns-over-https-rustls) = %{version}

%description -n %{name}+dns-over-https
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "dns-over-https" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dns-over-https-rustls" feature.

%package     -n %{name}+dns-over-native-tls
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-tls) = %{version}
Requires:       crate(%{pkgname}/native-tls) = %{version}
Requires:       crate(%{pkgname}/tokio-native-tls) = %{version}
Requires:       crate(%{pkgname}/tokio-runtime) = %{version}
Provides:       crate(%{pkgname}/dns-over-native-tls) = %{version}

%description -n %{name}+dns-over-native-tls
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "dns-over-native-tls" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-openssl
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-tls) = %{version}
Requires:       crate(%{pkgname}/openssl) = %{version}
Requires:       crate(%{pkgname}/tokio-openssl) = %{version}
Requires:       crate(%{pkgname}/tokio-runtime) = %{version}
Provides:       crate(%{pkgname}/dns-over-openssl) = %{version}

%description -n %{name}+dns-over-openssl
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "dns-over-openssl" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-quic
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-quic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytes) = %{version}
Requires:       crate(%{pkgname}/dns-over-rustls) = %{version}
Requires:       crate(%{pkgname}/quinn) = %{version}
Requires:       crate(%{pkgname}/tokio-runtime) = %{version}
Requires:       crate(rustls-0.21/quic) >= 0.21.6
Provides:       crate(%{pkgname}/dns-over-quic) = %{version}

%description -n %{name}+dns-over-quic
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "dns-over-quic" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-rustls
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-tls) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(%{pkgname}/rustls-pemfile) = %{version}
Requires:       crate(%{pkgname}/tokio-runtime) = %{version}
Requires:       crate(%{pkgname}/tokio-rustls) = %{version}
Provides:       crate(%{pkgname}/dns-over-rustls) = %{version}

%description -n %{name}+dns-over-rustls
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "dns-over-rustls" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-openssl
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(%{pkgname}/openssl) = %{version}
Provides:       crate(%{pkgname}/dnssec-openssl) = %{version}

%description -n %{name}+dnssec-openssl
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "dnssec-openssl" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(%{pkgname}/ring) = %{version}
Provides:       crate(%{pkgname}/dnssec-ring) = %{version}

%description -n %{name}+dnssec-ring
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "dnssec-ring" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h2
Summary:        Hickory DNS is a safe and secure DNS library - feature "h2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(h2-0.3/default) >= 0.3.0
Requires:       crate(h2-0.3/stream) >= 0.3.0
Provides:       crate(%{pkgname}/h2) = %{version}

%description -n %{name}+h2
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "h2" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3
Summary:        Hickory DNS is a safe and secure DNS library - feature "h3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(h3-0.0.3/default) >= 0.0.3
Provides:       crate(%{pkgname}/h3) = %{version}

%description -n %{name}+h3
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "h3" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3-quinn
Summary:        Hickory DNS is a safe and secure DNS library - feature "h3-quinn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(h3-quinn-0.0.4/default) >= 0.0.4
Provides:       crate(%{pkgname}/h3-quinn) = %{version}

%description -n %{name}+h3-quinn
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "h3-quinn" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http
Summary:        Hickory DNS is a safe and secure DNS library - feature "http"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(http-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/http) = %{version}

%description -n %{name}+http
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "http" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js-sys
Summary:        Hickory DNS is a safe and secure DNS library - feature "js-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/default) >= 0.3.44
Provides:       crate(%{pkgname}/js-sys) = %{version}

%description -n %{name}+js-sys
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "js-sys" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdns
Summary:        Hickory DNS is a safe and secure DNS library - feature "mdns"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(socket2-0.5/all) >= 0.5.0
Provides:       crate(%{pkgname}/mdns) = %{version}

%description -n %{name}+mdns
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "mdns" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-certs
Summary:        Hickory DNS is a safe and secure DNS library - feature "native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-native-certs-0.6/default) >= 0.6.3
Provides:       crate(%{pkgname}/native-certs) = %{version}

%description -n %{name}+native-certs
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "native-certs" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        Hickory DNS is a safe and secure DNS library - feature "native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(native-tls-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "native-tls" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl
Summary:        Hickory DNS is a safe and secure DNS library - feature "openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-0.10/default) >= 0.10.55
Requires:       crate(openssl-0.10/v102) >= 0.10.55
Requires:       crate(openssl-0.10/v110) >= 0.10.55
Provides:       crate(%{pkgname}/openssl) = %{version}

%description -n %{name}+openssl
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "openssl" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quinn
Summary:        Hickory DNS is a safe and secure DNS library - feature "quinn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-0.10/log) >= 0.10.0
Requires:       crate(quinn-0.10/runtime-tokio) >= 0.10.0
Requires:       crate(quinn-0.10/tls-rustls) >= 0.10.0
Provides:       crate(%{pkgname}/quinn) = %{version}

%description -n %{name}+quinn
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "quinn" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ring-0.17/default) >= 0.17.0
Requires:       crate(ring-0.17/std) >= 0.17.0
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "ring" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Hickory DNS is a safe and secure DNS library - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.21/default) >= 0.21.6
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "rustls" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-pemfile
Summary:        Hickory DNS is a safe and secure DNS library - feature "rustls-pemfile"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-pemfile-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/rustls-pemfile) = %{version}

%description -n %{name}+rustls-pemfile
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "rustls-pemfile" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hickory DNS is a safe and secure DNS library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "serde" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-config
Summary:        Hickory DNS is a safe and secure DNS library - feature "serde-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(url-2/serde) >= 2.4.0
Provides:       crate(%{pkgname}/serde-config) = %{version}

%description -n %{name}+serde-config
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "serde-config" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socket2
Summary:        Hickory DNS is a safe and secure DNS library - feature "socket2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(socket2-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/socket2) = %{version}

%description -n %{name}+socket2
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "socket2" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.21.0
Requires:       crate(tokio-1/io-util) >= 1.21.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "tokio" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-native-tls
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-native-tls-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/tokio-native-tls) = %{version}

%description -n %{name}+tokio-native-tls
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "tokio-native-tls" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-openssl
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-openssl-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/tokio-openssl) = %{version}

%description -n %{name}+tokio-openssl
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "tokio-openssl" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-runtime
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio-runtime" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/io-util) >= 1.21.0
Requires:       crate(tokio-1/net) >= 1.21.0
Requires:       crate(tokio-1/rt) >= 1.21.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.21.0
Requires:       crate(tokio-1/time) >= 1.21.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/tokio-runtime) = %{version}

%description -n %{name}+tokio-runtime
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "tokio-runtime" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio-rustls
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-rustls-0.24/default) >= 0.24.0
Requires:       crate(tokio-rustls-0.24/early-data) >= 0.24.0
Provides:       crate(%{pkgname}/tokio-rustls) = %{version}

%description -n %{name}+tokio-rustls
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "tokio-rustls" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Hickory DNS is a safe and secure DNS library - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/js-sys) = %{version}
Requires:       crate(%{pkgname}/wasm-bindgen-crate) = %{version}
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "wasm-bindgen" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen-crate
Summary:        Hickory DNS is a safe and secure DNS library - feature "wasm-bindgen-crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.58
Provides:       crate(%{pkgname}/wasm-bindgen-crate) = %{version}

%description -n %{name}+wasm-bindgen-crate
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "wasm-bindgen-crate" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Hickory DNS is a safe and secure DNS library - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-roots-0.25/default) >= 0.25.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "webpki-roots" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
