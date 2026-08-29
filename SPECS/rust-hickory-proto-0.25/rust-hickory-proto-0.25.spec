# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hickory-proto
%global full_version 0.25.2
%global pkgname hickory-proto-0.25

Name:           rust-hickory-proto-0.25
Version:        0.25.2
Release:        %autorelease
Summary:        Rust crate "hickory-proto"
License:        MIT OR Apache-2.0
URL:            https://hickory-dns.org/
#!RemoteAsset:  sha256:f8a6fe56c0038198998a6f217ca4e7ef3a5e51f46163bd6dd60b5c71ca6c6502
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.43
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(data-encoding-2/alloc) >= 2.2.0
Requires:       crate(enum-as-inner-0.6/default) >= 0.6.0
Requires:       crate(futures-channel-0.3/alloc) >= 0.3.5
Requires:       crate(futures-util-0.3/alloc) >= 0.3.5
Requires:       crate(idna-1/alloc) >= 1.0.3
Requires:       crate(idna-1/compiled-data) >= 1.0.3
Requires:       crate(ipnet-2) >= 2.3.0
Requires:       crate(once-cell-1/critical-section) >= 1.20.0
Requires:       crate(rand-0.9/alloc) >= 0.9.0
Requires:       crate(rand-0.9/std-rng) >= 0.9.0
Requires:       crate(thiserror-2) >= 2.0.0
Requires:       crate(tinyvec-1/alloc) >= 1.1.1
Requires:       crate(tinyvec-1/default) >= 1.1.1
Requires:       crate(tracing-0.1) >= 0.1.30
Requires:       crate(url-2) >= 2.5.4
Provides:       crate(%{pkgname}) = %{version}

%description
This is the foundational DNS protocol library for all Hickory DNS projects.
Source code for takopackized Rust crate "hickory-proto"

%package     -n %{name}+dnssec
Summary:        Hickory DNS is a safe and secure DNS library - feature "__dnssec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(bitflags-2/default) >= 2.4.1
Requires:       crate(rustls-pki-types-1/default) >= 1.10.0
Requires:       crate(time-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/dnssec) = %{version}

%description -n %{name}+dnssec
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "__dnssec" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3
Summary:        Hickory DNS is a safe and secure DNS library - feature "__h3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(h3-0.0.7/default) >= 0.0.7
Requires:       crate(h3-quinn-0.0.9/default) >= 0.0.9
Requires:       crate(http-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/h3) = %{version}

%description -n %{name}+h3
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "__h3" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https
Summary:        Hickory DNS is a safe and secure DNS library - feature "__https"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(h2-0.4/default) >= 0.4.0
Requires:       crate(h2-0.4/stream) >= 0.4.0
Requires:       crate(http-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/https) = %{version}

%description -n %{name}+https
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "__https" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quic
Summary:        Hickory DNS is a safe and secure DNS library - feature "__quic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Requires:       crate(quinn-0.11/log) >= 0.11.2
Requires:       crate(quinn-0.11/runtime-tokio) >= 0.11.2
Provides:       crate(%{pkgname}/quic) = %{version}

%description -n %{name}+quic
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "__quic" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls
Summary:        Hickory DNS is a safe and secure DNS library - feature "__tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(rustls-0.23/logging) >= 0.23.23
Requires:       crate(rustls-0.23/std) >= 0.23.23
Requires:       crate(rustls-0.23/tls12) >= 0.23.23
Requires:       crate(tokio-rustls-0.26/early-data) >= 0.26.0
Provides:       crate(%{pkgname}/tls) = %{version}

%description -n %{name}+tls
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "__tls" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backtrace
Summary:        Hickory DNS is a safe and secure DNS library - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.50
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "backtrace" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Hickory DNS is a safe and secure DNS library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "default" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(aws-lc-rs-1/aws-lc-sys) >= 1.12.3
Requires:       crate(aws-lc-rs-1/prebuilt-nasm) >= 1.12.3
Requires:       crate(aws-lc-rs-1/ring-io) >= 1.12.3
Provides:       crate(%{pkgname}/dnssec-aws-lc-rs) = %{version}

%description -n %{name}+dnssec-aws-lc-rs
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "dnssec-aws-lc-rs" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(ring-0.17/default) >= 0.17.0
Requires:       crate(ring-0.17/std) >= 0.17.0
Provides:       crate(%{pkgname}/dnssec-ring) = %{version}

%description -n %{name}+dnssec-ring
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "dnssec-ring" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-io
Summary:        Hickory DNS is a safe and secure DNS library - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3) >= 0.3.5
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "futures-io" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "h3-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/h3) = %{version}
Requires:       crate(%{pkgname}/quic-aws-lc-rs) = %{version}
Provides:       crate(%{pkgname}/h3-aws-lc-rs) = %{version}

%description -n %{name}+h3-aws-lc-rs
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "h3-aws-lc-rs" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "h3-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/h3) = %{version}
Requires:       crate(%{pkgname}/quic-ring) = %{version}
Provides:       crate(%{pkgname}/h3-ring) = %{version}

%description -n %{name}+h3-ring
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "h3-ring" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "https-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/https) = %{version}
Requires:       crate(%{pkgname}/tls-aws-lc-rs) = %{version}
Provides:       crate(%{pkgname}/https-aws-lc-rs) = %{version}

%description -n %{name}+https-aws-lc-rs
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "https-aws-lc-rs" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "https-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/https) = %{version}
Requires:       crate(%{pkgname}/tls-ring) = %{version}
Provides:       crate(%{pkgname}/https-ring) = %{version}

%description -n %{name}+https-ring
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "https-ring" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdns
Summary:        Hickory DNS is a safe and secure DNS library - feature "mdns"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(socket2-0.5/all) >= 0.5.0
Provides:       crate(%{pkgname}/mdns) = %{version}

%description -n %{name}+mdns
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "mdns" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-std-rand
Summary:        Hickory DNS is a safe and secure DNS library - feature "no-std-rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(critical-section-1/default) >= 1.1.1
Requires:       crate(once-cell-1/critical-section) >= 1.20.0
Provides:       crate(%{pkgname}/no-std-rand) = %{version}

%description -n %{name}+no-std-rand
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "no-std-rand" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quic-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "quic-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/quic) = %{version}
Requires:       crate(%{pkgname}/tls-aws-lc-rs) = %{version}
Requires:       crate(quinn-0.11/log) >= 0.11.2
Requires:       crate(quinn-0.11/runtime-tokio) >= 0.11.2
Requires:       crate(quinn-0.11/rustls-aws-lc-rs) >= 0.11.2
Provides:       crate(%{pkgname}/quic-aws-lc-rs) = %{version}

%description -n %{name}+quic-aws-lc-rs
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "quic-aws-lc-rs" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quic-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "quic-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/quic) = %{version}
Requires:       crate(%{pkgname}/tls-ring) = %{version}
Requires:       crate(quinn-0.11/log) >= 0.11.2
Requires:       crate(quinn-0.11/runtime-tokio) >= 0.11.2
Requires:       crate(quinn-0.11/rustls-ring) >= 0.11.2
Provides:       crate(%{pkgname}/quic-ring) = %{version}

%description -n %{name}+quic-ring
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "quic-ring" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-platform-verifier
Summary:        Hickory DNS is a safe and secure DNS library - feature "rustls-platform-verifier"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(rustls-platform-verifier-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/rustls-platform-verifier) = %{version}

%description -n %{name}+rustls-platform-verifier
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "rustls-platform-verifier" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hickory DNS is a safe and secure DNS library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(url-2/serde) >= 2.5.4
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "serde" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socket2
Summary:        Hickory DNS is a safe and secure DNS library - feature "socket2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(socket2-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/socket2) = %{version}

%description -n %{name}+socket2
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "socket2" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Hickory DNS is a safe and secure DNS library - feature "std" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(data-encoding-2/alloc) >= 2.2.0
Requires:       crate(data-encoding-2/std) >= 2.2.0
Requires:       crate(futures-channel-0.3/alloc) >= 0.3.5
Requires:       crate(futures-channel-0.3/std) >= 0.3.5
Requires:       crate(futures-io-0.3/std) >= 0.3.5
Requires:       crate(futures-util-0.3/alloc) >= 0.3.5
Requires:       crate(futures-util-0.3/std) >= 0.3.5
Requires:       crate(ipnet-2/std) >= 2.3.0
Requires:       crate(rand-0.9/alloc) >= 0.9.0
Requires:       crate(rand-0.9/std) >= 0.9.0
Requires:       crate(rand-0.9/std-rng) >= 0.9.0
Requires:       crate(rand-0.9/thread-rng) >= 0.9.0
Requires:       crate(ring-0.17/std) >= 0.17.0
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(tracing-0.1/std) >= 0.1.30
Requires:       crate(url-2/std) >= 2.5.4
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/testing) = %{version}
Provides:       crate(%{pkgname}/text-parsing) = %{version}

%description -n %{name}+std
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "std" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "testing", and "text-parsing" features.

%package     -n %{name}+tls-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "tls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(tokio-rustls-0.26/aws-lc-rs) >= 0.26.0
Requires:       crate(tokio-rustls-0.26/early-data) >= 0.26.0
Provides:       crate(%{pkgname}/tls-aws-lc-rs) = %{version}

%description -n %{name}+tls-aws-lc-rs
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "tls-aws-lc-rs" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "tls-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(tokio-rustls-0.26/early-data) >= 0.26.0
Requires:       crate(tokio-rustls-0.26/ring) >= 0.26.0
Provides:       crate(%{pkgname}/tls-ring) = %{version}

%description -n %{name}+tls-ring
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "tls-ring" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(tokio-1/default) >= 1.21.0
Requires:       crate(tokio-1/io-util) >= 1.21.0
Requires:       crate(tokio-1/macros) >= 1.21.0
Requires:       crate(tokio-1/net) >= 1.21.0
Requires:       crate(tokio-1/rt) >= 1.21.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.21.0
Requires:       crate(tokio-1/time) >= 1.21.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "tokio" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Hickory DNS is a safe and secure DNS library - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/default) >= 0.3.44
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.58
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "wasm-bindgen" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Hickory DNS is a safe and secure DNS library - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-roots-0.26/default) >= 0.26.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This is the foundational DNS protocol library for all Hickory DNS projects.
This metapackage enables feature "webpki-roots" for the Rust hickory-proto crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
