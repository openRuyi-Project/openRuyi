# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyper-rustls
%global full_version 0.23.2
%global pkgname hyper-rustls-0.23

Name:           rust-hyper-rustls-0.23
Version:        0.23.2
Release:        %autorelease
Summary:        Rust crate "hyper-rustls"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/ctz/hyper-rustls
#!RemoteAsset:  sha256:1788965e61b367cd03a62950836d5cd41560c3577d90e40e0819373194d1661c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(http-0.2/default) >= 0.2.0
Requires:       crate(hyper-0.14/client) >= 0.14.0
Requires:       crate(rustls-0.20) >= 0.20.1
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-rustls-0.23) >= 0.23.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "hyper-rustls"

%package     -n %{name}+default
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/http1) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/native-tokio) = %{version}
Requires:       crate(%{pkgname}/tls12) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http1
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "http1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-0.14/client) >= 0.14.0
Requires:       crate(hyper-0.14/http1) >= 0.14.0
Provides:       crate(%{pkgname}/http1) = %{version}

%description -n %{name}+http1
This metapackage enables feature "http1" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http2
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "http2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-0.14/client) >= 0.14.0
Requires:       crate(hyper-0.14/http2) >= 0.14.0
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
Requires:       crate(rustls-0.20/logging) >= 0.20.1
Requires:       crate(tokio-rustls-0.23/logging) >= 0.23.0
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tokio
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "native-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-native-certs) = %{version}
Requires:       crate(%{pkgname}/tokio-runtime) = %{version}
Provides:       crate(%{pkgname}/native-tokio) = %{version}

%description -n %{name}+native-tokio
This metapackage enables feature "native-tokio" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-native-certs
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "rustls-native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-native-certs-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/rustls-native-certs) = %{version}

%description -n %{name}+rustls-native-certs
This metapackage enables feature "rustls-native-certs" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls12
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "tls12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.20/tls12) >= 0.20.1
Requires:       crate(tokio-rustls-0.23/tls12) >= 0.23.0
Provides:       crate(%{pkgname}/tls12) = %{version}

%description -n %{name}+tls12
This metapackage enables feature "tls12" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-runtime
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "tokio-runtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-0.14/client) >= 0.14.0
Requires:       crate(hyper-0.14/runtime) >= 0.14.0
Provides:       crate(%{pkgname}/tokio-runtime) = %{version}

%description -n %{name}+tokio-runtime
This metapackage enables feature "tokio-runtime" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-roots-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This metapackage enables feature "webpki-roots" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-tokio
Summary:        Rustls+hyper integration for pure rust HTTPS - feature "webpki-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio-runtime) = %{version}
Requires:       crate(%{pkgname}/webpki-roots) = %{version}
Provides:       crate(%{pkgname}/webpki-tokio) = %{version}

%description -n %{name}+webpki-tokio
This metapackage enables feature "webpki-tokio" for the Rust hyper-rustls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
