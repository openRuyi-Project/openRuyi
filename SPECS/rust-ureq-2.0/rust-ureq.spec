# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ureq
%global full_version 2.12.1
%global pkgname ureq-2.0

Name:           rust-ureq-2.0
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

Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(once-cell-1.0/default) >= 1.21.3
Requires:       crate(url-2.0/default) >= 2.5.8
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/proxy-from-env)

%description
Source code for takopackized Rust crate "ureq"

%package     -n %{name}+charset
Summary:        Simple, safe HTTP client - feature "charset"
Requires:       crate(%{pkgname})
Requires:       crate(encoding-rs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/charset)

%description -n %{name}+charset
This metapackage enables feature "charset" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Simple, safe HTTP client - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gzip)
Requires:       crate(%{pkgname}/tls)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gzip
Summary:        Simple, safe HTTP client - feature "gzip"
Requires:       crate(%{pkgname})
Requires:       crate(flate2-1.0/default) >= 1.1.5
Provides:       crate(%{pkgname}/gzip)

%description -n %{name}+gzip
This metapackage enables feature "gzip" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-crate
Summary:        Simple, safe HTTP client - feature "http-crate"
Requires:       crate(%{pkgname})
Requires:       crate(http-1.0/default) >= 1.1
Provides:       crate(%{pkgname}/http-crate)

%description -n %{name}+http-crate
This metapackage enables feature "http-crate" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Simple, safe HTTP client - feature "json"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Provides:       crate(%{pkgname}/json)

%description -n %{name}+json
This metapackage enables feature "json" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        Simple, safe HTTP client - feature "native-tls"
Requires:       crate(%{pkgname})
Requires:       crate(native-tls-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/native-tls)

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socks-proxy
Summary:        Simple, safe HTTP client - feature "socks-proxy"
Requires:       crate(%{pkgname})
Requires:       crate(socks-0.3/default) >= 0.3.4
Provides:       crate(%{pkgname}/socks-proxy)

%description -n %{name}+socks-proxy
This metapackage enables feature "socks-proxy" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls
Summary:        Simple, safe HTTP client - feature "tls"
Requires:       crate(%{pkgname})
Requires:       crate(rustls-0.23/logging) >= 0.23.36
Requires:       crate(rustls-0.23/ring) >= 0.23.36
Requires:       crate(rustls-0.23/std) >= 0.23.36
Requires:       crate(rustls-0.23/tls12) >= 0.23.36
Requires:       crate(rustls-pki-types-1.0/default) >= 1.13.2
Requires:       crate(webpki-roots-0.26/default) >= 0.26.11
Provides:       crate(%{pkgname}/tls)

%description -n %{name}+tls
This metapackage enables feature "tls" for the Rust ureq crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
