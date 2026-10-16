# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hickory-resolver
%global full_version 0.24.4
%global pkgname hickory-resolver-0.24

Name:           rust-hickory-resolver-0.24
Version:        0.24.4
Release:        %autorelease
Summary:        Rust crate "hickory-resolver"
License:        MIT OR Apache-2.0
URL:            https://hickory-dns.org/
#!RemoteAsset:  sha256:cbb117a1ca520e111743ab2f6688eddee69db4e0ea242545a604dce8a66fd22e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(futures-util-0.3/std) >= 0.3.5
Requires:       crate(hickory-proto-0.24) >= 0.24.0
Requires:       crate(lru-cache-0.1/default) >= 0.1.2
Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(rand-0.8/default) >= 0.8.0
Requires:       crate(smallvec-1/default) >= 1.6.0
Requires:       crate(thiserror-1/default) >= 1.0.20
Requires:       crate(tracing-0.1/default) >= 0.1.30

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/dnssec) = %{version}
Provides:       crate(%{pkgname}/testing) = %{version}

%description
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
Source code for takopackized Rust crate "hickory-resolver"

%package     -n %{name}+backtrace
Summary:        Hickory DNS is a safe and secure DNS library - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.50
Requires:       crate(hickory-proto-0.24/backtrace) >= 0.24.0
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "backtrace" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Hickory DNS is a safe and secure DNS library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/system-config) = %{version}
Requires:       crate(%{pkgname}/tokio-runtime) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "default" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-h3
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-h3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-rustls) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-h3) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-h3) = %{version}

%description -n %{name}+dns-over-h3
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dns-over-h3" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-https
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-https"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-https) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-https) = %{version}

%description -n %{name}+dns-over-https
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dns-over-https" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-https-rustls
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-https-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-https) = %{version}
Requires:       crate(%{pkgname}/dns-over-rustls) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-https-rustls) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-https-rustls) = %{version}

%description -n %{name}+dns-over-https-rustls
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dns-over-https-rustls" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-native-tls
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-tls) = %{version}
Requires:       crate(%{pkgname}/tokio-native-tls) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-native-tls) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-native-tls) = %{version}

%description -n %{name}+dns-over-native-tls
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dns-over-native-tls" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-openssl
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-tls) = %{version}
Requires:       crate(%{pkgname}/tokio-openssl) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-openssl) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-openssl) = %{version}

%description -n %{name}+dns-over-openssl
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dns-over-openssl" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-quic
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-quic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-rustls) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-quic) >= 0.24.0
Requires:       crate(rustls-0.21/quic) >= 0.21.6
Provides:       crate(%{pkgname}/dns-over-quic) = %{version}

%description -n %{name}+dns-over-quic
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dns-over-quic" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dns-over-rustls
Summary:        Hickory DNS is a safe and secure DNS library - feature "dns-over-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dns-over-tls) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(%{pkgname}/tokio-rustls) = %{version}
Requires:       crate(hickory-proto-0.24/dns-over-rustls) >= 0.24.0
Provides:       crate(%{pkgname}/dns-over-rustls) = %{version}

%description -n %{name}+dns-over-rustls
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dns-over-rustls" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-openssl
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(hickory-proto-0.24/dnssec-openssl) >= 0.24.0
Provides:       crate(%{pkgname}/dnssec-openssl) = %{version}

%description -n %{name}+dnssec-openssl
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dnssec-openssl" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dnssec-ring
Summary:        Hickory DNS is a safe and secure DNS library - feature "dnssec-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dnssec) = %{version}
Requires:       crate(hickory-proto-0.24/dnssec-ring) >= 0.24.0
Provides:       crate(%{pkgname}/dnssec-ring) = %{version}

%description -n %{name}+dnssec-ring
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "dnssec-ring" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipconfig
Summary:        Hickory DNS is a safe and secure DNS library - feature "ipconfig"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipconfig-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/ipconfig) = %{version}

%description -n %{name}+ipconfig
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "ipconfig" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-certs
Summary:        Hickory DNS is a safe and secure DNS library - feature "native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.24/native-certs) >= 0.24.0
Requires:       crate(rustls-native-certs-0.6/default) >= 0.6.3
Provides:       crate(%{pkgname}/native-certs) = %{version}

%description -n %{name}+native-certs
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "native-certs" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+resolv-conf
Summary:        Hickory DNS is a safe and secure DNS library - feature "resolv-conf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(resolv-conf-0.7/default) >= 0.7.0
Requires:       crate(resolv-conf-0.7/system) >= 0.7.0
Provides:       crate(%{pkgname}/resolv-conf) = %{version}

%description -n %{name}+resolv-conf
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "resolv-conf" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Hickory DNS is a safe and secure DNS library - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.21/default) >= 0.21.6
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "rustls" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hickory DNS is a safe and secure DNS library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "serde" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-config
Summary:        Hickory DNS is a safe and secure DNS library - feature "serde-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(hickory-proto-0.24/serde-config) >= 0.24.0
Provides:       crate(%{pkgname}/serde-config) = %{version}

%description -n %{name}+serde-config
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "serde-config" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system-config
Summary:        Hickory DNS is a safe and secure DNS library - feature "system-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ipconfig) = %{version}
Requires:       crate(%{pkgname}/resolv-conf) = %{version}
Provides:       crate(%{pkgname}/system-config) = %{version}

%description -n %{name}+system-config
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "system-config" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.21.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "tokio" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-native-tls
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-native-tls-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/tokio-native-tls) = %{version}

%description -n %{name}+tokio-native-tls
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "tokio-native-tls" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-openssl
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-openssl-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/tokio-openssl) = %{version}

%description -n %{name}+tokio-openssl
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "tokio-openssl" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-runtime
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio-runtime" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.24/tokio-runtime) >= 0.24.0
Requires:       crate(tokio-1/rt) >= 1.21.0
Provides:       crate(%{pkgname}/dns-over-tls) = %{version}
Provides:       crate(%{pkgname}/tokio-runtime) = %{version}

%description -n %{name}+tokio-runtime
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "tokio-runtime" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dns-over-tls" feature.

%package     -n %{name}+tokio-rustls
Summary:        Hickory DNS is a safe and secure DNS library - feature "tokio-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-rustls-0.24/default) >= 0.24.0
Provides:       crate(%{pkgname}/tokio-rustls) = %{version}

%description -n %{name}+tokio-rustls
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "tokio-rustls" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Hickory DNS is a safe and secure DNS library - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hickory-proto-0.24/webpki-roots) >= 0.24.0
Requires:       crate(webpki-roots-0.25/default) >= 0.25.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This Resolver library  uses the Client library to perform all DNS queries. The Resolver is intended to be a high-level library for any DNS record resolution see Resolver and AsyncResolver for supported resolution types. The Client can be used for other queries.
This metapackage enables feature "webpki-roots" for the Rust hickory-resolver crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
