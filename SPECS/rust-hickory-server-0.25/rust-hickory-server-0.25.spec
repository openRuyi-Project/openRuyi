# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hickory-server
%global full_version 0.25.2
%global pkgname hickory-server-0.25

Name:           rust-hickory-server-0.25
Version:        0.25.2
Release:        %autorelease
Summary:        Rust crate "hickory-server"
License:        MIT OR Apache-2.0
URL:            https://hickory-dns.org/
#!RemoteAsset:  sha256:d53e5fe811b941c74ee46b8818228bfd2bc2688ba276a0eaeb0f2c95ea3b2585
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.43
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(data-encoding-2) >= 2.2.0
Requires:       crate(enum-as-inner-0.6/default) >= 0.6.0
Requires:       crate(futures-util-0.3/std) >= 0.3.5
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(ipnet-2/serde) >= 2.3.0
Requires:       crate(ipnet-2/std) >= 2.3.0
Requires:       crate(prefix-trie-0.7/default) >= 0.7.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(thiserror-2) >= 2.0.0
Requires:       crate(time-0.3/default) >= 0.3.0
Requires:       crate(tokio-1/default) >= 1.21.0
Requires:       crate(tokio-1/macros) >= 1.21.0
Requires:       crate(tokio-1/net) >= 1.21.0
Requires:       crate(tokio-1/sync) >= 1.21.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.9
Requires:       crate(tracing-0.1) >= 0.1.30
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dnssec) = %{version}
Provides:       crate(%{pkgname}/testing) = %{version}

%description
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
Source code for takopackized Rust crate "hickory-server"

%package     -n %{name}+h3
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "__h3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/quic) = %{version}
Requires:       crate(h3-0.0.7/default) >= 0.0.7
Requires:       crate(h3-quinn-0.0.9/default) >= 0.0.9
Provides:       crate(%{pkgname}/h3) = %{version}

%description -n %{name}+h3
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "__h3" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "__https"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(h2-0.4/default) >= 0.4.0
Requires:       crate(h2-0.4/stream) >= 0.4.0
Requires:       crate(http-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/https) = %{version}

%description -n %{name}+https
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "__https" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "__tls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/logging) >= 0.23.23
Requires:       crate(rustls-0.23/std) >= 0.23.23
Requires:       crate(rustls-0.23/tls12) >= 0.23.23
Requires:       crate(tokio-rustls-0.26) >= 0.26.0
Provides:       crate(%{pkgname}/quic) = %{version}
Provides:       crate(%{pkgname}/tls) = %{version}

%description -n %{name}+tls
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "__tls" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "__quic" feature.

%package     -n %{name}+backtrace
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/backtrace) >= 0.25.0
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "backtrace" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "dnssec-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(hickory-proto-0.25/dnssec-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-recursor-0.25/dnssec-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-recursor-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/dnssec-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/rc) >= 1.0.0
Provides:       crate(%{pkgname}/dnssec-aws-lc-rs) = %{version}

%description -n %{name}+dnssec-aws-lc-rs
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dnssec-aws-lc-rs" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-ring
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "dnssec-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(hickory-proto-0.25/dnssec-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-recursor-0.25/dnssec-ring) >= 0.25.0
Requires:       crate(hickory-recursor-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/dnssec-ring) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/rc) >= 1.0.0
Provides:       crate(%{pkgname}/dnssec-ring) = %{version}

%description -n %{name}+dnssec-ring
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "dnssec-ring" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "h3-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/h3) = %{version}
Requires:       crate(%{pkgname}/quic-aws-lc-rs) = %{version}
Requires:       crate(hickory-proto-0.25/h3-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/h3-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/h3-aws-lc-rs) = %{version}

%description -n %{name}+h3-aws-lc-rs
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "h3-aws-lc-rs" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3-ring
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "h3-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/h3) = %{version}
Requires:       crate(%{pkgname}/quic-ring) = %{version}
Requires:       crate(hickory-proto-0.25/h3-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/h3-ring) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/h3-ring) = %{version}

%description -n %{name}+h3-ring
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "h3-ring" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "https-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/https) = %{version}
Requires:       crate(%{pkgname}/tls-aws-lc-rs) = %{version}
Requires:       crate(hickory-proto-0.25/https-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/https-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/https-aws-lc-rs) = %{version}

%description -n %{name}+https-aws-lc-rs
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "https-aws-lc-rs" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https-ring
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "https-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/https) = %{version}
Requires:       crate(%{pkgname}/tls-ring) = %{version}
Requires:       crate(hickory-proto-0.25/https-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/https-ring) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/https-ring) = %{version}

%description -n %{name}+https-ring
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "https-ring" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+metrics
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "metrics"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(metrics-0.24/default) >= 0.24.1
Provides:       crate(%{pkgname}/metrics) = %{version}

%description -n %{name}+metrics
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "metrics" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quic-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "quic-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/quic) = %{version}
Requires:       crate(%{pkgname}/tls-aws-lc-rs) = %{version}
Requires:       crate(hickory-proto-0.25/quic-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/quic-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/quic-aws-lc-rs) = %{version}

%description -n %{name}+quic-aws-lc-rs
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "quic-aws-lc-rs" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quic-ring
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "quic-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/quic) = %{version}
Requires:       crate(%{pkgname}/tls-ring) = %{version}
Requires:       crate(hickory-proto-0.25/quic-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/quic-ring) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/quic-ring) = %{version}

%description -n %{name}+quic-ring
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "quic-ring" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+recursor
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "recursor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-recursor-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/recursor) = %{version}

%description -n %{name}+recursor
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "recursor" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+resolver
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "resolver" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/blocklist) = %{version}
Provides:       crate(%{pkgname}/resolver) = %{version}

%description -n %{name}+resolver
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "resolver" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "blocklist" feature.

%package     -n %{name}+rusqlite
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "rusqlite" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rusqlite-0.35/bundled) >= 0.35.0
Requires:       crate(rusqlite-0.35/default) >= 0.35.0
Requires:       crate(rusqlite-0.35/time) >= 0.35.0
Provides:       crate(%{pkgname}/rusqlite) = %{version}
Provides:       crate(%{pkgname}/sqlite) = %{version}

%description -n %{name}+rusqlite
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "rusqlite" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "sqlite" feature.

%package     -n %{name}+rustls-platform-verifier
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "rustls-platform-verifier"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-resolver-0.25/rustls-platform-verifier) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/rustls-platform-verifier) = %{version}

%description -n %{name}+rustls-platform-verifier
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "rustls-platform-verifier" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "tls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tls-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tls-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/tls-aws-lc-rs) = %{version}

%description -n %{name}+tls-aws-lc-rs
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "tls-aws-lc-rs" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-ring
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "tls-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/text-parsing) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tls-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tls-ring) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Provides:       crate(%{pkgname}/tls-ring) = %{version}

%description -n %{name}+tls-ring
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "tls-ring" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+toml
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "toml"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-0.8/default) >= 0.8.14
Provides:       crate(%{pkgname}/toml) = %{version}

%description -n %{name}+toml
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "toml" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Hickory DNS is a safe and secure DNS server with DNSSEC support - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-resolver-0.25/serde) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/system-config) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/tokio) >= 0.25.0
Requires:       crate(hickory-resolver-0.25/webpki-roots) >= 0.25.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
Eventually this could be a replacement for BIND9. The DNSSEC support allows  for live signing of all records, in it does not currently support  records signed offline. The server supports dynamic DNS with SIG0 authenticated  requests. Hickory DNS is based on the Tokio and Futures libraries, which means  it should be easily integrated into other software that also use those  libraries.
This metapackage enables feature "webpki-roots" for the Rust hickory-server crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
