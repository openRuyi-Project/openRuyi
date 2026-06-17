# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tungstenite
%global full_version 0.28.0
%global pkgname tungstenite-0.28

Name:           rust-tungstenite-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "tungstenite"
License:        MIT OR Apache-2.0
URL:            https://github.com/snapview/tungstenite-rs
#!RemoteAsset:  sha256:8628dcc84e5a09eb3d8423d6cb682965dea9133204e8fb3efee74c2a0c259442
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.9.0
Requires:       crate(log-0.4/default) >= 0.4.8
Requires:       crate(rand-0.9/default) >= 0.9.0
Requires:       crate(thiserror-2/default) >= 2.0.7
Requires:       crate(utf-8-0.7/default) >= 0.7.5
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tungstenite"

%package     -n %{name}+rustls-tls
Summary:        Lightweight stream-based WebSocket implementation - feature "__rustls-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(%{pkgname}/rustls-pki-types) = %{version}
Provides:       crate(%{pkgname}/rustls-tls) = %{version}

%description -n %{name}+rustls-tls
This metapackage enables feature "__rustls-tls" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+data-encoding
Summary:        Lightweight stream-based WebSocket implementation - feature "data-encoding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(data-encoding-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/data-encoding) = %{version}

%description -n %{name}+data-encoding
This metapackage enables feature "data-encoding" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+handshake
Summary:        Lightweight stream-based WebSocket implementation - feature "handshake" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/data-encoding) = %{version}
Requires:       crate(%{pkgname}/http) = %{version}
Requires:       crate(%{pkgname}/httparse) = %{version}
Requires:       crate(%{pkgname}/sha1) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/handshake) = %{version}

%description -n %{name}+handshake
This metapackage enables feature "handshake" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+http
Summary:        Lightweight stream-based WebSocket implementation - feature "http"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(http-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/http) = %{version}

%description -n %{name}+http
This metapackage enables feature "http" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+httparse
Summary:        Lightweight stream-based WebSocket implementation - feature "httparse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(httparse-1/default) >= 1.3.4
Provides:       crate(%{pkgname}/httparse) = %{version}

%description -n %{name}+httparse
This metapackage enables feature "httparse" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-crate
Summary:        Lightweight stream-based WebSocket implementation - feature "native-tls-crate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(native-tls-0.2/default) >= 0.2.3
Provides:       crate(%{pkgname}/native-tls) = %{version}
Provides:       crate(%{pkgname}/native-tls-crate) = %{version}

%description -n %{name}+native-tls-crate
This metapackage enables feature "native-tls-crate" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "native-tls" feature.

%package     -n %{name}+native-tls-vendored
Summary:        Lightweight stream-based WebSocket implementation - feature "native-tls-vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/native-tls) = %{version}
Requires:       crate(native-tls-0.2/vendored) >= 0.2.3
Provides:       crate(%{pkgname}/native-tls-vendored) = %{version}

%description -n %{name}+native-tls-vendored
This metapackage enables feature "native-tls-vendored" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Lightweight stream-based WebSocket implementation - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/std) >= 0.23.0
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-native-certs
Summary:        Lightweight stream-based WebSocket implementation - feature "rustls-native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-native-certs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rustls-native-certs) = %{version}

%description -n %{name}+rustls-native-certs
This metapackage enables feature "rustls-native-certs" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-pki-types
Summary:        Lightweight stream-based WebSocket implementation - feature "rustls-pki-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-pki-types-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/rustls-pki-types) = %{version}

%description -n %{name}+rustls-pki-types
This metapackage enables feature "rustls-pki-types" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls-native-roots
Summary:        Lightweight stream-based WebSocket implementation - feature "rustls-tls-native-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-native-certs) = %{version}
Requires:       crate(%{pkgname}/rustls-tls) = %{version}
Provides:       crate(%{pkgname}/rustls-tls-native-roots) = %{version}

%description -n %{name}+rustls-tls-native-roots
This metapackage enables feature "rustls-tls-native-roots" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls-webpki-roots
Summary:        Lightweight stream-based WebSocket implementation - feature "rustls-tls-webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-tls) = %{version}
Requires:       crate(%{pkgname}/webpki-roots) = %{version}
Provides:       crate(%{pkgname}/rustls-tls-webpki-roots) = %{version}

%description -n %{name}+rustls-tls-webpki-roots
This metapackage enables feature "rustls-tls-webpki-roots" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1
Summary:        Lightweight stream-based WebSocket implementation - feature "sha1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha1-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/sha1) = %{version}

%description -n %{name}+sha1
This metapackage enables feature "sha1" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+url
Summary:        Lightweight stream-based WebSocket implementation - feature "url"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(url-2/default) >= 2.1.0
Provides:       crate(%{pkgname}/url) = %{version}

%description -n %{name}+url
This metapackage enables feature "url" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Lightweight stream-based WebSocket implementation - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-roots-0.26/default) >= 0.26.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This metapackage enables feature "webpki-roots" for the Rust tungstenite crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
