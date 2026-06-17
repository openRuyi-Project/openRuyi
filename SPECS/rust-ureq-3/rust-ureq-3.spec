# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ureq
%global full_version 3.3.0
%global pkgname ureq-3

Name:           rust-ureq-3
Version:        3.3.0
Release:        %autorelease
Summary:        Rust crate "ureq"
License:        MIT OR Apache-2.0
URL:            https://github.com/algesten/ureq
#!RemoteAsset:  sha256:dea7109cdcd5864d4eeb1b58a1648dc9bf520360d7af16ec26d0a9354bafcfc0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(log-0.4/default) >= 0.4.25
Requires:       crate(percent-encoding-2/default) >= 2.3.1
Requires:       crate(ureq-proto-0.6/client) >= 0.6.0
Requires:       crate(utf8-zero-0.8/default) >= 0.8.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/rustls) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}

%description
Source code for takopackized Rust crate "ureq"

%package     -n %{name}+doc
Summary:        Simple, safe HTTP client - feature "_doc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/aws-lc-rs) >= 0.23.22
Requires:       crate(rustls-0.23/logging) >= 0.23.22
Requires:       crate(rustls-0.23/std) >= 0.23.22
Requires:       crate(rustls-0.23/tls12) >= 0.23.22
Provides:       crate(%{pkgname}/doc) = %{version}

%description -n %{name}+doc
This metapackage enables feature "_doc" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Simple, safe HTTP client - feature "_ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/logging) >= 0.23.22
Requires:       crate(rustls-0.23/ring) >= 0.23.22
Requires:       crate(rustls-0.23/std) >= 0.23.22
Requires:       crate(rustls-0.23/tls12) >= 0.23.22
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "_ring" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls
Summary:        Simple, safe HTTP client - feature "_tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-pki-types-1/std) >= 1.11.0
Provides:       crate(%{pkgname}/tls) = %{version}

%description -n %{name}+tls
This metapackage enables feature "_tls" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+url
Summary:        Simple, safe HTTP client - feature "_url"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(url-2) >= 2.3.1
Provides:       crate(%{pkgname}/url) = %{version}

%description -n %{name}+url
This metapackage enables feature "_url" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+brotli
Summary:        Simple, safe HTTP client - feature "brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(brotli-decompressor-5/default) >= 5.0.0
Provides:       crate(%{pkgname}/brotli) = %{version}

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+charset
Summary:        Simple, safe HTTP client - feature "charset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encoding-rs-0.8/default) >= 0.8.34
Provides:       crate(%{pkgname}/charset) = %{version}

%description -n %{name}+charset
This metapackage enables feature "charset" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cookies
Summary:        Simple, safe HTTP client - feature "cookies"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/url) = %{version}
Requires:       crate(cookie-store-0.22/preserve-order) >= 0.22.0
Provides:       crate(%{pkgname}/cookies) = %{version}

%description -n %{name}+cookies
This metapackage enables feature "cookies" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Simple, safe HTTP client - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gzip) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gzip
Summary:        Simple, safe HTTP client - feature "gzip"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.30
Provides:       crate(%{pkgname}/gzip) = %{version}

%description -n %{name}+gzip
This metapackage enables feature "gzip" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Simple, safe HTTP client - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cookie-store-0.22/preserve-order) >= 0.22.0
Requires:       crate(cookie-store-0.22/serde-json) >= 0.22.0
Requires:       crate(serde-1/std) >= 1.0.138
Requires:       crate(serde-json-1/std) >= 1.0.120
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+multipart
Summary:        Simple, safe HTTP client - feature "multipart"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Requires:       crate(mime-guess-2/default) >= 2.0.5
Provides:       crate(%{pkgname}/multipart) = %{version}

%description -n %{name}+multipart
This metapackage enables feature "multipart" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        Simple, safe HTTP client - feature "native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/native-tls-no-default) = %{version}
Requires:       crate(%{pkgname}/native-tls-webpki-roots) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(der-0.8/pem) >= 0.8.0
Requires:       crate(der-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-no-default
Summary:        Simple, safe HTTP client - feature "native-tls-no-default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(der-0.8/pem) >= 0.8.0
Requires:       crate(der-0.8/std) >= 0.8.0
Requires:       crate(native-tls-0.2) >= 0.2.14
Provides:       crate(%{pkgname}/native-tls-no-default) = %{version}

%description -n %{name}+native-tls-no-default
This metapackage enables feature "native-tls-no-default" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-webpki-roots
Summary:        Simple, safe HTTP client - feature "native-tls-webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-root-certs-1) >= 1.0.0
Provides:       crate(%{pkgname}/native-tls-webpki-roots) = %{version}

%description -n %{name}+native-tls-webpki-roots
This metapackage enables feature "native-tls-webpki-roots" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+platform-verifier
Summary:        Simple, safe HTTP client - feature "platform-verifier"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-platform-verifier-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/platform-verifier) = %{version}

%description -n %{name}+platform-verifier
This metapackage enables feature "platform-verifier" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Simple, safe HTTP client - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ring) = %{version}
Requires:       crate(%{pkgname}/rustls-no-provider) = %{version}
Requires:       crate(%{pkgname}/rustls-webpki-roots) = %{version}
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-no-provider
Summary:        Simple, safe HTTP client - feature "rustls-no-provider"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(rustls-0.23/logging) >= 0.23.22
Requires:       crate(rustls-0.23/std) >= 0.23.22
Requires:       crate(rustls-0.23/tls12) >= 0.23.22
Provides:       crate(%{pkgname}/rustls-no-provider) = %{version}

%description -n %{name}+rustls-no-provider
This metapackage enables feature "rustls-no-provider" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-webpki-roots
Summary:        Simple, safe HTTP client - feature "rustls-webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-roots-1) >= 1.0.0
Provides:       crate(%{pkgname}/rustls-webpki-roots) = %{version}

%description -n %{name}+rustls-webpki-roots
This metapackage enables feature "rustls-webpki-roots" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socks-proxy
Summary:        Simple, safe HTTP client - feature "socks-proxy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(socks-0.3/default) >= 0.3.4
Provides:       crate(%{pkgname}/socks-proxy) = %{version}

%description -n %{name}+socks-proxy
This metapackage enables feature "socks-proxy" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored
Summary:        Simple, safe HTTP client - feature "vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(native-tls-0.2/vendored) >= 0.2.14
Provides:       crate(%{pkgname}/vendored) = %{version}

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+win-system-proxy
Summary:        Simple, safe HTTP client - feature "win-system-proxy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(winreg-0.56/default) >= 0.56.0
Provides:       crate(%{pkgname}/win-system-proxy) = %{version}

%description -n %{name}+win-system-proxy
This metapackage enables feature "win-system-proxy" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
