# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-tungstenite
%global full_version 0.28.0
%global pkgname tokio-tungstenite-0.28

Name:           rust-tokio-tungstenite-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "tokio-tungstenite"
License:        MIT
URL:            https://github.com/snapview/tokio-tungstenite
#!RemoteAsset:  sha256:d25a406cddcc431a75d3d9afc6a7c0f7428d4891dd973e4d54c56b46127bf857
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-util-0.3/sink) >= 0.3.28
Requires:       crate(futures-util-0.3/std) >= 0.3.28
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tungstenite-0.28) >= 0.28.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/stream) = %{version}

%description
Source code for takopackized Rust crate "tokio-tungstenite"

%package     -n %{name}+rustls-tls
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "__rustls-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/handshake) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(%{pkgname}/rustls-pki-types) = %{version}
Requires:       crate(%{pkgname}/stream) = %{version}
Requires:       crate(%{pkgname}/tokio-rustls) = %{version}
Requires:       crate(tungstenite-0.28/rustls-tls) >= 0.28.0
Provides:       crate(%{pkgname}/rustls-tls) = %{version}

%description -n %{name}+rustls-tls
This metapackage enables feature "__rustls-tls" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+connect
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "connect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/handshake) = %{version}
Requires:       crate(%{pkgname}/stream) = %{version}
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Provides:       crate(%{pkgname}/connect) = %{version}

%description -n %{name}+connect
This metapackage enables feature "connect" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/connect) = %{version}
Requires:       crate(%{pkgname}/handshake) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+handshake
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "handshake"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tungstenite-0.28/handshake) >= 0.28.0
Provides:       crate(%{pkgname}/handshake) = %{version}

%description -n %{name}+handshake
This metapackage enables feature "handshake" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/handshake) = %{version}
Requires:       crate(%{pkgname}/native-tls-crate) = %{version}
Requires:       crate(%{pkgname}/stream) = %{version}
Requires:       crate(%{pkgname}/tokio-native-tls) = %{version}
Requires:       crate(tungstenite-0.28/native-tls) >= 0.28.0
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-crate
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "native-tls-crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(native-tls-0.2/default) >= 0.2.11
Provides:       crate(%{pkgname}/native-tls-crate) = %{version}

%description -n %{name}+native-tls-crate
This metapackage enables feature "native-tls-crate" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-vendored
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "native-tls-vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/native-tls) = %{version}
Requires:       crate(native-tls-0.2/vendored) >= 0.2.11
Requires:       crate(tungstenite-0.28/native-tls-vendored) >= 0.28.0
Provides:       crate(%{pkgname}/native-tls-vendored) = %{version}

%description -n %{name}+native-tls-vendored
This metapackage enables feature "native-tls-vendored" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23) >= 0.23.0
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-native-certs
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "rustls-native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-native-certs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rustls-native-certs) = %{version}

%description -n %{name}+rustls-native-certs
This metapackage enables feature "rustls-native-certs" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-pki-types
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "rustls-pki-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-pki-types-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/rustls-pki-types) = %{version}

%description -n %{name}+rustls-pki-types
This metapackage enables feature "rustls-pki-types" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls-native-roots
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "rustls-tls-native-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-native-certs) = %{version}
Requires:       crate(%{pkgname}/rustls-tls) = %{version}
Provides:       crate(%{pkgname}/rustls-tls-native-roots) = %{version}

%description -n %{name}+rustls-tls-native-roots
This metapackage enables feature "rustls-tls-native-roots" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls-webpki-roots
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "rustls-tls-webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-tls) = %{version}
Requires:       crate(%{pkgname}/webpki-roots) = %{version}
Provides:       crate(%{pkgname}/rustls-tls-webpki-roots) = %{version}

%description -n %{name}+rustls-tls-webpki-roots
This metapackage enables feature "rustls-tls-webpki-roots" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-native-tls
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "tokio-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-native-tls-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/tokio-native-tls) = %{version}

%description -n %{name}+tokio-native-tls
This metapackage enables feature "tokio-native-tls" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-rustls
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "tokio-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-rustls-0.26) >= 0.26.0
Provides:       crate(%{pkgname}/tokio-rustls) = %{version}

%description -n %{name}+tokio-rustls
This metapackage enables feature "tokio-rustls" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+url
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "url"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tungstenite-0.28/url) >= 0.28.0
Provides:       crate(%{pkgname}/url) = %{version}

%description -n %{name}+url
This metapackage enables feature "url" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Tokio binding for Tungstenite, the Lightweight stream-based WebSocket implementation - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-roots-0.26/default) >= 0.26.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This metapackage enables feature "webpki-roots" for the Rust tokio-tungstenite crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
