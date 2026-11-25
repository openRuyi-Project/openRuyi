# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls
%global full_version 0.24.0-dev.1
%global pkgname rustls-0.24.0-dev.1

Name:           rust-rustls-0.24.0-dev.1
Version:        0.24.0
Release:        %autorelease
Summary:        Rust crate "rustls"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/rustls/rustls
#!RemoteAsset:  sha256:aea97a47e031d09563e2b411eca6522d03ca605514b5f06f0fe78923d6652d28
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/alloc) >= 1.16.0
Requires:       crate(once-cell-1/race) >= 1.16.0
Requires:       crate(once-cell-1/std) >= 1.16.0
Requires:       crate(rustls-pki-types-1/alloc) >= 1.15.0
Requires:       crate(rustls-pki-types-1/default) >= 1.15.0
Requires:       crate(rustls-pki-types-1/std) >= 1.15.0
Requires:       crate(subtle-2) >= 2.5.0
Requires:       crate(zeroize-1/default) >= 1.8.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rustls"

%package     -n %{name}+brotli
Summary:        Modern TLS library written in Rust - feature "brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(brotli-8/std) >= 8.0.0
Requires:       crate(brotli-decompressor-5/default) >= 5.0.0
Provides:       crate(%{pkgname}/brotli) = %{version}

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Modern TLS library written in Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(%{pkgname}/webpki) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Modern TLS library written in Rust - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.17/default-hasher) >= 0.17.0
Requires:       crate(hashbrown-0.17/inline-more) >= 0.17.0
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Modern TLS library written in Rust - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.8
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki
Summary:        Modern TLS library written in Rust - feature "webpki"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-webpki-0.104.0-alpha.7/alloc) >= 0.104.0-alpha.7
Provides:       crate(%{pkgname}/webpki) = %{version}

%description -n %{name}+webpki
This metapackage enables feature "webpki" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib
Summary:        Modern TLS library written in Rust - feature "zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zlib-rs-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/zlib) = %{version}

%description -n %{name}+zlib
This metapackage enables feature "zlib" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
