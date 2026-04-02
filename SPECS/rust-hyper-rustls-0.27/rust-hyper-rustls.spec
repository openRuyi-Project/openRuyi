# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyper-rustls
%global full_version 0.27.7
%global pkgname hyper-rustls-0.27

Name:           rust-hyper-rustls-0.27
Version:        0.27.7
Release:        %autorelease
Summary:        Rust crate "hyper-rustls"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/rustls/hyper-rustls
#!RemoteAsset:  sha256:e3c93eb611681b207e1fe55d5a71ecf91572ec8a6705cdb6857f7d8d5242cf58
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(http-1.0/default) >= 1.4.0
Requires:       crate(hyper-1.0) >= 1.9.0
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.20
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.20
Requires:       crate(rustls-0.23) >= 0.23.37
Requires:       crate(rustls-pki-types-1.0/default) >= 1.14.0
Requires:       crate(tokio-1.0/default) >= 1.50.0
Requires:       crate(tokio-rustls-0.26) >= 0.26.4
Requires:       crate(tower-service-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "hyper-rustls"

%package     -n %{name}+aws-lc-rs
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "aws-lc-rs"
Requires:       crate(%{pkgname})
Requires:       crate(rustls-0.23/aws-lc-rs) >= 0.23.37
Provides:       crate(%{pkgname}/aws-lc-rs)

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws-lc-rs" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/aws-lc-rs)
Requires:       crate(%{pkgname}/http1)
Requires:       crate(%{pkgname}/logging)
Requires:       crate(%{pkgname}/native-tokio)
Requires:       crate(%{pkgname}/tls12)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fips
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "fips"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/aws-lc-rs)
Requires:       crate(rustls-0.23/fips) >= 0.23.37
Provides:       crate(%{pkgname}/fips)

%description -n %{name}+fips
This metapackage enables feature "fips" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http1
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "http1"
Requires:       crate(%{pkgname})
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.20
Requires:       crate(hyper-util-0.1/http1) >= 0.1.20
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.20
Provides:       crate(%{pkgname}/http1)

%description -n %{name}+http1
This metapackage enables feature "http1" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http2
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "http2"
Requires:       crate(%{pkgname})
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.20
Requires:       crate(hyper-util-0.1/http2) >= 0.1.20
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.20
Provides:       crate(%{pkgname}/http2)

%description -n %{name}+http2
This metapackage enables feature "http2" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "log"
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "logging"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/log)
Requires:       crate(rustls-0.23/logging) >= 0.23.37
Requires:       crate(tokio-rustls-0.26/logging) >= 0.26.4
Provides:       crate(%{pkgname}/logging)

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "ring"
Requires:       crate(%{pkgname})
Requires:       crate(rustls-0.23/ring) >= 0.23.37
Provides:       crate(%{pkgname}/ring)

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-native-certs
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "rustls-native-certs" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rustls-native-certs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/native-tokio)
Provides:       crate(%{pkgname}/rustls-native-certs)

%description -n %{name}+rustls-native-certs
This metapackage enables feature "rustls-native-certs" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "native-tokio" feature.

%package     -n %{name}+rustls-platform-verifier
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "rustls-platform-verifier"
Requires:       crate(%{pkgname})
Requires:       crate(rustls-platform-verifier-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/rustls-platform-verifier)

%description -n %{name}+rustls-platform-verifier
This metapackage enables feature "rustls-platform-verifier" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls12
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "tls12"
Requires:       crate(%{pkgname})
Requires:       crate(rustls-0.23/tls12) >= 0.23.37
Requires:       crate(tokio-rustls-0.26/tls12) >= 0.26.4
Provides:       crate(%{pkgname}/tls12)

%description -n %{name}+tls12
This metapackage enables feature "tls12" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "webpki-roots" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(webpki-roots-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/webpki-roots)
Provides:       crate(%{pkgname}/webpki-tokio)

%description -n %{name}+webpki-roots
This metapackage enables feature "webpki-roots" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "webpki-tokio" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
