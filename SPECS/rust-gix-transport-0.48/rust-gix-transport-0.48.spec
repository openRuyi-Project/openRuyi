# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-transport
%global full_version 0.48.0
%global pkgname gix-transport-0.48

Name:           rust-gix-transport-0.48
Version:        0.48.0
Release:        %autorelease
Summary:        Rust crate "gix-transport"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:12f7cc0179fc89d53c54e1f9ce51229494864ab4bf136132d69db1b011741ca3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(bstr-1/unicode) >= 1.12.0
Requires:       crate(gix-command-0.6/default) >= 0.6.2
Requires:       crate(gix-features-0.43/default) >= 0.43.0
Requires:       crate(gix-packetline-0.19/default) >= 0.19.1
Requires:       crate(gix-quote-0.6/default) >= 0.6.0
Requires:       crate(gix-sec-0.12/default) >= 0.12.0
Requires:       crate(gix-url-0.32/default) >= 0.32.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/http-client-insecure-credentials) = %{version}

%description
Source code for takopackized Rust crate "gix-transport"

%package     -n %{name}+async-client
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "async-client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-trait) = %{version}
Requires:       crate(%{pkgname}/futures-io) = %{version}
Requires:       crate(%{pkgname}/futures-lite) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(gix-packetline-0.19/async-io) >= 0.19.1
Provides:       crate(%{pkgname}/async-client) = %{version}

%description -n %{name}+async-client
This metapackage enables feature "async-client" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.12.0
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-trait
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "async-trait"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-trait-0.1/default) >= 0.1.51
Provides:       crate(%{pkgname}/async-trait) = %{version}

%description -n %{name}+async-trait
This metapackage enables feature "async-trait" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.22/default) >= 0.22.1
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-client
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "blocking-client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-packetline-0.19/blocking-io) >= 0.19.1
Provides:       crate(%{pkgname}/blocking-client) = %{version}

%description -n %{name}+blocking-client
This metapackage enables feature "blocking-client" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+curl
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "curl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curl-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/curl) = %{version}

%description -n %{name}+curl
This metapackage enables feature "curl" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-io
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/default) >= 0.3.16
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-lite
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "futures-lite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-lite-2/default) >= 2.1.0
Provides:       crate(%{pkgname}/futures-lite) = %{version}

%description -n %{name}+futures-lite
This metapackage enables feature "futures-lite" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gix-credentials
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "gix-credentials"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-credentials-0.30/default) >= 0.30.0
Provides:       crate(%{pkgname}/gix-credentials) = %{version}

%description -n %{name}+gix-credentials
This metapackage enables feature "gix-credentials" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-client
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "http-client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(%{pkgname}/blocking-client) = %{version}
Requires:       crate(%{pkgname}/gix-credentials) = %{version}
Requires:       crate(gix-features-0.43/io-pipe) >= 0.43.0
Provides:       crate(%{pkgname}/http-client) = %{version}

%description -n %{name}+http-client
This metapackage enables feature "http-client" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-client-curl
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "http-client-curl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/curl) = %{version}
Requires:       crate(%{pkgname}/http-client) = %{version}
Provides:       crate(%{pkgname}/http-client-curl) = %{version}

%description -n %{name}+http-client-curl
This metapackage enables feature "http-client-curl" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-client-curl-rust-tls
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "http-client-curl-rust-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/http-client-curl) = %{version}
Requires:       crate(curl-0.4/rustls) >= 0.4.0
Provides:       crate(%{pkgname}/http-client-curl-rust-tls) = %{version}

%description -n %{name}+http-client-curl-rust-tls
This metapackage enables feature "http-client-curl-rust-tls" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-client-reqwest
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "http-client-reqwest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/http-client) = %{version}
Requires:       crate(%{pkgname}/reqwest) = %{version}
Provides:       crate(%{pkgname}/http-client-reqwest) = %{version}

%description -n %{name}+http-client-reqwest
This metapackage enables feature "http-client-reqwest" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-client-reqwest-native-tls
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "http-client-reqwest-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/http-client-reqwest) = %{version}
Requires:       crate(reqwest-0.12/blocking) >= 0.12.22
Requires:       crate(reqwest-0.12/charset) >= 0.12.22
Requires:       crate(reqwest-0.12/default-tls) >= 0.12.22
Requires:       crate(reqwest-0.12/http2) >= 0.12.22
Requires:       crate(reqwest-0.12/macos-system-configuration) >= 0.12.22
Provides:       crate(%{pkgname}/http-client-reqwest-native-tls) = %{version}

%description -n %{name}+http-client-reqwest-native-tls
This metapackage enables feature "http-client-reqwest-native-tls" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-client-reqwest-rust-tls
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "http-client-reqwest-rust-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/http-client-reqwest) = %{version}
Requires:       crate(reqwest-0.12/blocking) >= 0.12.22
Requires:       crate(reqwest-0.12/charset) >= 0.12.22
Requires:       crate(reqwest-0.12/http2) >= 0.12.22
Requires:       crate(reqwest-0.12/macos-system-configuration) >= 0.12.22
Requires:       crate(reqwest-0.12/rustls-tls) >= 0.12.22
Provides:       crate(%{pkgname}/http-client-reqwest-rust-tls) = %{version}

%description -n %{name}+http-client-reqwest-rust-tls
This metapackage enables feature "http-client-reqwest-rust-tls" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-client-reqwest-rust-tls-trust-dns
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "http-client-reqwest-rust-tls-trust-dns"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/http-client-reqwest) = %{version}
Requires:       crate(reqwest-0.12/blocking) >= 0.12.22
Requires:       crate(reqwest-0.12/charset) >= 0.12.22
Requires:       crate(reqwest-0.12/http2) >= 0.12.22
Requires:       crate(reqwest-0.12/macos-system-configuration) >= 0.12.22
Requires:       crate(reqwest-0.12/rustls-tls) >= 0.12.22
Requires:       crate(reqwest-0.12/trust-dns) >= 0.12.22
Provides:       crate(%{pkgname}/http-client-reqwest-rust-tls-trust-dns) = %{version}

%description -n %{name}+http-client-reqwest-rust-tls-trust-dns
This metapackage enables feature "http-client-reqwest-rust-tls-trust-dns" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pin-project-lite
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "pin-project-lite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.6
Provides:       crate(%{pkgname}/pin-project-lite) = %{version}

%description -n %{name}+pin-project-lite
This metapackage enables feature "pin-project-lite" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reqwest
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "reqwest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/blocking) >= 0.12.22
Requires:       crate(reqwest-0.12/charset) >= 0.12.22
Requires:       crate(reqwest-0.12/http2) >= 0.12.22
Requires:       crate(reqwest-0.12/macos-system-configuration) >= 0.12.22
Provides:       crate(%{pkgname}/reqwest) = %{version}

%description -n %{name}+reqwest
This metapackage enables feature "reqwest" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project dedicated to implementing the git transport layer - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.114
Requires:       crate(serde-1/std) >= 1.0.114
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-transport crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
