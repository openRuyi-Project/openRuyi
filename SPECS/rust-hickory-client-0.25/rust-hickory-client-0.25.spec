# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hickory-client
%global full_version 0.25.2
%global pkgname hickory-client-0.25

Name:           rust-hickory-client-0.25
Version:        0.25.2
Release:        %autorelease
Summary:        Rust crate "hickory-client"
License:        MIT OR Apache-2.0
URL:            https://hickory-dns.org/
#!RemoteAsset:  sha256:c466cd63a4217d5b2b8e32f23f58312741ce96e3c84bf7438677d2baff0fc555
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(data-encoding-2) >= 2.2.0
Requires:       crate(futures-channel-0.3/std) >= 0.3.5
Requires:       crate(futures-util-0.3/std) >= 0.3.5
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(once-cell-1/critical-section) >= 1.20.0
Requires:       crate(radix-trie-0.2/default) >= 0.2.0
Requires:       crate(rand-0.9/alloc) >= 0.9.0
Requires:       crate(thiserror-2) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.21.0
Requires:       crate(tokio-1/net) >= 1.21.0
Requires:       crate(tokio-1/rt) >= 1.21.0
Requires:       crate(tracing-0.1) >= 0.1.30
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dnssec) = %{version}

%description
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
Source code for takopackized Rust crate "hickory-client"

%package     -n %{name}+backtrace
Summary:        Hickory DNS is a safe and secure DNS library - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/backtrace) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "backtrace" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(hickory-proto-0.25/dnssec-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/dnssec-aws-lc-rs) = %{version}

%description -n %{name}+dnssec-aws-lc-rs
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dnssec-aws-lc-rs" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(hickory-proto-0.25/dnssec-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/dnssec-ring) = %{version}

%description -n %{name}+dnssec-ring
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dnssec-ring" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "h3-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/h3-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/h3-aws-lc-rs) = %{version}

%description -n %{name}+h3-aws-lc-rs
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "h3-aws-lc-rs" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "h3-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/h3-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/h3-ring) = %{version}

%description -n %{name}+h3-ring
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "h3-ring" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "https-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/https-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/https-aws-lc-rs) = %{version}

%description -n %{name}+https-aws-lc-rs
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "https-aws-lc-rs" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "https-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/https-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/https-ring) = %{version}

%description -n %{name}+https-ring
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "https-ring" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdns
Summary:        Hickory DNS is a safe and secure DNS library - feature "mdns"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/mdns) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/mdns) = %{version}

%description -n %{name}+mdns
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "mdns" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quic-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "quic-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/quic-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/quic-aws-lc-rs) = %{version}

%description -n %{name}+quic-aws-lc-rs
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "quic-aws-lc-rs" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quic-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "quic-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/quic-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/quic-ring) = %{version}

%description -n %{name}+quic-ring
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "quic-ring" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-platform-verifier
Summary:        Hickory DNS is a safe and secure DNS library - feature "rustls-platform-verifier"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/rustls-platform-verifier) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/rustls-platform-verifier) = %{version}

%description -n %{name}+rustls-platform-verifier
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "rustls-platform-verifier" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hickory DNS is a safe and secure DNS library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "serde" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "tls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tls-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/tls-aws-lc-rs) = %{version}

%description -n %{name}+tls-aws-lc-rs
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "tls-aws-lc-rs" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "tls-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tls-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/tls-ring) = %{version}

%description -n %{name}+tls-ring
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "tls-ring" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Hickory DNS is a safe and secure DNS library - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-proto-0.25/webpki-roots) >= 0.25.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  functions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "webpki-roots" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
