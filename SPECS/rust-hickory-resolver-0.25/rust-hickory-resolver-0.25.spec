# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hickory-resolver
%global full_version 0.25.2
%global pkgname hickory-resolver-0.25

Name:           rust-hickory-resolver-0.25
Version:        0.25.2
Release:        %autorelease
Summary:        Rust crate "hickory-resolver"
License:        MIT OR Apache-2.0
URL:            https://hickory-dns.org/
#!RemoteAsset:  sha256:dc62a9a99b0bfb44d2ab95a7208ac952d31060efc16241c87eaf36406fecf87a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(futures-util-0.3/std) >= 0.3.5
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(moka-0.12/default) >= 0.12.0
Requires:       crate(moka-0.12/sync) >= 0.12.0
Requires:       crate(once-cell-1/critical-section) >= 1.20.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(rand-0.9/alloc) >= 0.9.0
Requires:       crate(smallvec-1/default) >= 1.6.0
Requires:       crate(thiserror-2) >= 2.0.0
Requires:       crate(tracing-0.1) >= 0.1.30

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/dnssec) = %{version}

%description
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
Source code for takopackized Rust crate "hickory-resolver"

%package     -n %{name}+quic
Summary:        Hickory DNS is a safe and secure DNS library - feature "__quic" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(quinn-0.11/log) >= 0.11.2
Requires:       crate(quinn-0.11/runtime-tokio) >= 0.11.2
Provides:       crate(%{pkgname}/h3) = %{version}
Provides:       crate(%{pkgname}/quic) = %{version}

%description -n %{name}+quic
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "__quic" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "__h3" feature.

%package     -n %{name}+tls
Summary:        Hickory DNS is a safe and secure DNS library - feature "__tls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(rustls-0.23/logging) >= 0.23.23
Requires:       crate(rustls-0.23/std) >= 0.23.23
Requires:       crate(rustls-0.23/tls12) >= 0.23.23
Requires:       crate(tokio-rustls-0.26) >= 0.26.0
Provides:       crate(%{pkgname}/https) = %{version}
Provides:       crate(%{pkgname}/tls) = %{version}

%description -n %{name}+tls
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "__tls" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "__https" feature.

%package     -n %{name}+backtrace
Summary:        Hickory DNS is a safe and secure DNS library - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.50
Requires:       crate(hickory-proto-0.25/backtrace) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "backtrace" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Hickory DNS is a safe and secure DNS library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/system-config) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "default" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(hickory-proto-0.25/dnssec-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Provides:       crate(%{pkgname}/dnssec-aws-lc-rs) = %{version}

%description -n %{name}+dnssec-aws-lc-rs
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dnssec-aws-lc-rs" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(hickory-proto-0.25/dnssec-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Provides:       crate(%{pkgname}/dnssec-ring) = %{version}

%description -n %{name}+dnssec-ring
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dnssec-ring" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "h3-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/h3) = %{version}
Requires:       crate(hickory-proto-0.25/h3-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Provides:       crate(%{pkgname}/h3-aws-lc-rs) = %{version}

%description -n %{name}+h3-aws-lc-rs
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "h3-aws-lc-rs" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+h3-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "h3-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/h3) = %{version}
Requires:       crate(hickory-proto-0.25/h3-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Provides:       crate(%{pkgname}/h3-ring) = %{version}

%description -n %{name}+h3-ring
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "h3-ring" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "https-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/https) = %{version}
Requires:       crate(hickory-proto-0.25/https-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Provides:       crate(%{pkgname}/https-aws-lc-rs) = %{version}

%description -n %{name}+https-aws-lc-rs
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "https-aws-lc-rs" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "https-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/https) = %{version}
Requires:       crate(hickory-proto-0.25/https-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Provides:       crate(%{pkgname}/https-ring) = %{version}

%description -n %{name}+https-ring
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "https-ring" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quic-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "quic-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/quic) = %{version}
Requires:       crate(hickory-proto-0.25/quic-aws-lc-rs) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(quinn-0.11/log) >= 0.11.2
Requires:       crate(quinn-0.11/runtime-tokio) >= 0.11.2
Requires:       crate(quinn-0.11/rustls-aws-lc-rs) >= 0.11.2
Provides:       crate(%{pkgname}/quic-aws-lc-rs) = %{version}

%description -n %{name}+quic-aws-lc-rs
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "quic-aws-lc-rs" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quic-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "quic-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/quic) = %{version}
Requires:       crate(hickory-proto-0.25/quic-ring) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(quinn-0.11/log) >= 0.11.2
Requires:       crate(quinn-0.11/runtime-tokio) >= 0.11.2
Requires:       crate(quinn-0.11/rustls-ring) >= 0.11.2
Provides:       crate(%{pkgname}/quic-ring) = %{version}

%description -n %{name}+quic-ring
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "quic-ring" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-platform-verifier
Summary:        Hickory DNS is a safe and secure DNS library - feature "rustls-platform-verifier"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/rustls-platform-verifier) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Provides:       crate(%{pkgname}/rustls-platform-verifier) = %{version}

%description -n %{name}+rustls-platform-verifier
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "rustls-platform-verifier" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hickory DNS is a safe and secure DNS library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/serde) >= 0.25.0
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/rc) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "serde" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system-config
Summary:        Hickory DNS is a safe and secure DNS library - feature "system-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipconfig-0.3/default) >= 0.3.0
Requires:       crate(resolv-conf-0.7/default) >= 0.7.0
Requires:       crate(resolv-conf-0.7/system) >= 0.7.0
Provides:       crate(%{pkgname}/system-config) = %{version}

%description -n %{name}+system-config
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "system-config" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-aws-lc-rs
Summary:        Hickory DNS is a safe and secure DNS library - feature "tls-aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tls-aws-lc-rs) >= 0.25.0
Provides:       crate(%{pkgname}/tls-aws-lc-rs) = %{version}

%description -n %{name}+tls-aws-lc-rs
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "tls-aws-lc-rs" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "tls-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tls-ring) >= 0.25.0
Provides:       crate(%{pkgname}/tls-ring) = %{version}

%description -n %{name}+tls-ring
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "tls-ring" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/tokio) >= 0.25.0
Requires:       crate(tokio-1/default) >= 1.21.0
Requires:       crate(tokio-1/rt) >= 1.21.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "tokio" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Hickory DNS is a safe and secure DNS library - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.25/std) >= 0.25.0
Requires:       crate(hickory-proto-0.25/webpki-roots) >= 0.25.0
Requires:       crate(webpki-roots-0.26/default) >= 0.26.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This Resolver library uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution. See Resolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "webpki-roots" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
