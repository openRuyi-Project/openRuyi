# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(hyper-1) >= 1.0.0
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.0
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.0
Requires:       crate(rustls-0.23) >= 0.23.0
Requires:       crate(rustls-pki-types-1/default) >= 1.0.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-rustls-0.26) >= 0.26.0
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "hyper-rustls"

%package     -n %{name}+aws-lc-rs
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/aws-lc-rs) >= 0.23.0
Provides:       crate(%{pkgname}/aws-lc-rs) = %{version}

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws-lc-rs" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(%{pkgname}/http1) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/native-tokio) = %{version}
Requires:       crate(%{pkgname}/tls12) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fips
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(rustls-0.23/fips) >= 0.23.0
Provides:       crate(%{pkgname}/fips) = %{version}

%description -n %{name}+fips
This metapackage enables feature "fips" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http1
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "http1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.0
Requires:       crate(hyper-util-0.1/http1) >= 0.1.0
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.0
Provides:       crate(%{pkgname}/http1) = %{version}

%description -n %{name}+http1
This metapackage enables feature "http1" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http2
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "http2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.0
Requires:       crate(hyper-util-0.1/http2) >= 0.1.0
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.0
Provides:       crate(%{pkgname}/http2) = %{version}

%description -n %{name}+http2
This metapackage enables feature "http2" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(rustls-0.23/logging) >= 0.23.0
Requires:       crate(tokio-rustls-0.26/logging) >= 0.26.0
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/ring) >= 0.23.0
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-native-certs
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "rustls-native-certs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-native-certs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/native-tokio) = %{version}
Provides:       crate(%{pkgname}/rustls-native-certs) = %{version}

%description -n %{name}+rustls-native-certs
This metapackage enables feature "rustls-native-certs" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "native-tokio" feature.

%package     -n %{name}+rustls-platform-verifier
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "rustls-platform-verifier"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-platform-verifier-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/rustls-platform-verifier) = %{version}

%description -n %{name}+rustls-platform-verifier
This metapackage enables feature "rustls-platform-verifier" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls12
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "tls12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.23/tls12) >= 0.23.0
Requires:       crate(tokio-rustls-0.26/tls12) >= 0.26.0
Provides:       crate(%{pkgname}/tls12) = %{version}

%description -n %{name}+tls12
This metapackage enables feature "tls12" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "webpki-roots" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-roots-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}
Provides:       crate(%{pkgname}/webpki-tokio) = %{version}

%description -n %{name}+webpki-roots
This metapackage enables feature "webpki-roots" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "webpki-tokio" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
