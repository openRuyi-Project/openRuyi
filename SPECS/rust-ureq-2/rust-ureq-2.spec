# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ureq
%global full_version 2.12.1
%global pkgname ureq-2

Name:           rust-ureq-2
Version:        2.12.1
Release:        %autorelease
Summary:        Rust crate "ureq"
License:        MIT OR Apache-2.0
URL:            https://github.com/algesten/ureq
#!RemoteAsset:  sha256:02d1a66277ed75f640d608235660df48c8e3c19f3b4edb6a263315626cc3c01d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(once-cell-1/default) >= 1.0.0
Requires:       crate(url-2/default) >= 2.5.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/proxy-from-env) = %{version}

%description
Source code for takopackized Rust crate "ureq"

%package     -n %{name}+brotli
Summary:        Simple, safe HTTP client - feature "brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(brotli-decompressor-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/brotli) = %{version}

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+charset
Summary:        Simple, safe HTTP client - feature "charset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encoding-rs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/charset) = %{version}

%description -n %{name}+charset
This metapackage enables feature "charset" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cookies
Summary:        Simple, safe HTTP client - feature "cookies"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cookie-0.18) >= 0.18.0
Requires:       crate(cookie-store-0.21/preserve-order) >= 0.21.1
Requires:       crate(cookie-store-0.21/serde-json) >= 0.21.1
Provides:       crate(%{pkgname}/cookies) = %{version}

%description -n %{name}+cookies
This metapackage enables feature "cookies" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Simple, safe HTTP client - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gzip) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gzip
Summary:        Simple, safe HTTP client - feature "gzip"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.22
Provides:       crate(%{pkgname}/gzip) = %{version}

%description -n %{name}+gzip
This metapackage enables feature "gzip" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-crate
Summary:        Simple, safe HTTP client - feature "http-crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(http-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/http-crate) = %{version}

%description -n %{name}+http-crate
This metapackage enables feature "http-crate" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-interop
Summary:        Simple, safe HTTP client - feature "http-interop"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(http-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/http-interop) = %{version}

%description -n %{name}+http-interop
This metapackage enables feature "http-interop" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Simple, safe HTTP client - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.97
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-certs
Summary:        Simple, safe HTTP client - feature "native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-native-certs-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/native-certs) = %{version}

%description -n %{name}+native-certs
This metapackage enables feature "native-certs" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        Simple, safe HTTP client - feature "native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(native-tls-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socks-proxy
Summary:        Simple, safe HTTP client - feature "socks-proxy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(socks-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/socks-proxy) = %{version}

%description -n %{name}+socks-proxy
This metapackage enables feature "socks-proxy" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+testdeps
Summary:        Simple, safe HTTP client - feature "testdeps"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hootbin-0.1/default) >= 0.1.5
Provides:       crate(%{pkgname}/testdeps) = %{version}

%description -n %{name}+testdeps
This metapackage enables feature "testdeps" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls
Summary:        Simple, safe HTTP client - feature "tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/logging) >= 0.23.19
Requires:       crate(rustls-0.23/ring) >= 0.23.19
Requires:       crate(rustls-0.23/std) >= 0.23.19
Requires:       crate(rustls-0.23/tls12) >= 0.23.19
Requires:       crate(rustls-pki-types-1/default) >= 1.0.0
Requires:       crate(webpki-roots-0.26/default) >= 0.26.0
Provides:       crate(%{pkgname}/tls) = %{version}

%description -n %{name}+tls
This metapackage enables feature "tls" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
