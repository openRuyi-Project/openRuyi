# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hickory-client
%global full_version 0.24.4
%global pkgname hickory-client-0.24

Name:           rust-hickory-client-0.24
Version:        0.24.4
Release:        %autorelease
Summary:        Rust crate "hickory-client"
License:        MIT OR Apache-2.0
URL:            https://hickory-dns.org/
#!RemoteAsset:  sha256:156579a5cd8d1fc6f0df87cc21b6ee870db978a163a1ba484acd98a4eff5a6de
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(data-encoding-2/default) >= 2.2.0
Requires:       crate(futures-channel-0.3/std) >= 0.3.5
Requires:       crate(futures-util-0.3/std) >= 0.3.5
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(radix-trie-0.2/default) >= 0.2.0
Requires:       crate(rand-0.8/default) >= 0.8.0
Requires:       crate(thiserror-1/default) >= 1.0.20
Requires:       crate(tokio-1/default) >= 1.21.0
Requires:       crate(tokio-1/net) >= 1.21.0
Requires:       crate(tokio-1/rt) >= 1.21.0
Requires:       crate(tracing-0.1/default) >= 0.1.30

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dns-over-tls) = %{version}

%description
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
Source code for takopackized Rust crate "hickory-client"

%package     -n %{name}+backtrace
Summary:        Hickory DNS is a safe and secure DNS library - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.24/backtrace) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "backtrace" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-https
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-https"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-https) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-https) = %{version}

%description -n %{name}+dns-over-https
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dns-over-https" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-https-openssl
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-https-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-https) = %{version}
Requires:       crate(%{pkgname}/dns-over-openssl) = %{version}
Provides:       crate(%{pkgname}/dns-over-https-openssl) = %{version}

%description -n %{name}+dns-over-https-openssl
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dns-over-https-openssl" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-https-rustls
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-https-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-https) = %{version}
Requires:       crate(%{pkgname}/dns-over-rustls) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-https-rustls) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-https-rustls) = %{version}

%description -n %{name}+dns-over-https-rustls
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dns-over-https-rustls" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-native-tls
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-tls) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-native-tls) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-native-tls) = %{version}

%description -n %{name}+dns-over-native-tls
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dns-over-native-tls" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-openssl
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-tls) = %{version}
Requires:       crate(%{pkgname}/dnssec-openssl) = %{version}
Provides:       crate(%{pkgname}/dns-over-openssl) = %{version}

%description -n %{name}+dns-over-openssl
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dns-over-openssl" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-quic
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-quic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-rustls) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-quic) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-quic) = %{version}

%description -n %{name}+dns-over-quic
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dns-over-quic" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-rustls
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-tls) = %{version}
Requires:       crate(%{pkgname}/dnssec-ring) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-rustls) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-rustls) = %{version}

%description -n %{name}+dns-over-rustls
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dns-over-rustls" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.24/dnssec) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/dnssec) = %{version}

%description -n %{name}+dnssec
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dnssec" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-openssl
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(hickory-proto-0.24/dnssec-openssl) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/dnssec-openssl) = %{version}

%description -n %{name}+dnssec-openssl
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dnssec-openssl" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(hickory-proto-0.24/dnssec-ring) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/dnssec-ring) = %{version}

%description -n %{name}+dnssec-ring
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dnssec-ring" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdns
Summary:        Hickory DNS is a safe and secure DNS library - feature "mdns"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.24/mdns) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/mdns) = %{version}

%description -n %{name}+mdns
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "mdns" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-certs
Summary:        Hickory DNS is a safe and secure DNS library - feature "native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.24/native-certs) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/native-certs) = %{version}

%description -n %{name}+native-certs
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "native-certs" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Hickory DNS is a safe and secure DNS library - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.21/default) >= 0.21.6
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "rustls" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hickory DNS is a safe and secure DNS library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "serde" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-config
Summary:        Hickory DNS is a safe and secure DNS library - feature "serde-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(hickory-proto-0.24/serde-config) >= 0.24.0
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Provides:       crate(%{pkgname}/serde-config) = %{version}

%description -n %{name}+serde-config
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "serde-config" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Hickory DNS is a safe and secure DNS library - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.24/text-parsing) >= 0.24.0
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Requires:       crate(hickory-proto-0.24/webpki-roots) >= 0.24.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This is the Client library with DNSSEC support.  DNSSEC with NSEC validation for negative records, is complete. The client supports  dynamic DNS with SIG0 authenticated requests, implementing easy to use high level  funtions. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "webpki-roots" for the Rust hickory-client crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
