# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tonic
%global full_version 0.6.2
%global pkgname tonic-0.6

Name:           rust-tonic-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "tonic"
License:        MIT
URL:            https://github.com/hyperium/tonic
#!RemoteAsset:  sha256:ff08f4649d10a70ffa3522ca559031285d8e421d727ac85c60825761818f5d0a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-stream-0.3/default) >= 0.3.0
Requires:       crate(base64-0.13/default) >= 0.13.0
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(futures-util-0.3) >= 0.3.0
Requires:       crate(http-0.2/default) >= 0.2.0
Requires:       crate(http-body-0.4/default) >= 0.4.4
Requires:       crate(percent-encoding-2/default) >= 2.1.0
Requires:       crate(pin-project-1/default) >= 1.0.0
Requires:       crate(tokio-stream-0.1/default) >= 0.1.0
Requires:       crate(tokio-util-0.6/codec) >= 0.6.0
Requires:       crate(tokio-util-0.6/default) >= 0.6.0
Requires:       crate(tower-layer-0.3/default) >= 0.3.0
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Requires:       crate(tracing-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tonic"

%package     -n %{name}+async-trait
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "async-trait" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-trait-0.1/default) >= 0.1.13
Provides:       crate(%{pkgname}/async-trait) = %{version}
Provides:       crate(%{pkgname}/codegen) = %{version}

%description -n %{name}+async-trait
This metapackage enables feature "async-trait" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "codegen" feature.

%package     -n %{name}+default
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/codegen) = %{version}
Requires:       crate(%{pkgname}/prost) = %{version}
Requires:       crate(%{pkgname}/transport) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flate2
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "flate2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/compression) = %{version}
Provides:       crate(%{pkgname}/flate2) = %{version}

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compression" feature.

%package     -n %{name}+h2
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "h2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(h2-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/h2) = %{version}

%description -n %{name}+h2
This metapackage enables feature "h2" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hyper
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "hyper"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-0.14/default) >= 0.14.14
Requires:       crate(hyper-0.14/full) >= 0.14.14
Provides:       crate(%{pkgname}/hyper) = %{version}

%description -n %{name}+hyper
This metapackage enables feature "hyper" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hyper-timeout
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "hyper-timeout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-timeout-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/hyper-timeout) = %{version}

%description -n %{name}+hyper-timeout
This metapackage enables feature "hyper-timeout" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prost
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "prost"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/prost-derive) = %{version}
Requires:       crate(%{pkgname}/prost1) = %{version}
Provides:       crate(%{pkgname}/prost) = %{version}

%description -n %{name}+prost
This metapackage enables feature "prost" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prost-derive
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "prost-derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-derive-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/prost-derive) = %{version}

%description -n %{name}+prost-derive
This metapackage enables feature "prost-derive" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prost1
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "prost1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/prost1) = %{version}

%description -n %{name}+prost1
This metapackage enables feature "prost1" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-native-certs
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "rustls-native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-native-certs-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/rustls-native-certs) = %{version}

%description -n %{name}+rustls-native-certs
This metapackage enables feature "rustls-native-certs" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio-rustls) = %{version}
Requires:       crate(%{pkgname}/transport) = %{version}
Provides:       crate(%{pkgname}/tls) = %{version}
Provides:       crate(%{pkgname}/tls-roots-common) = %{version}

%description -n %{name}+tls
This metapackage enables feature "tls" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tls-roots-common" feature.

%package     -n %{name}+tls-roots
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tls-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-native-certs) = %{version}
Requires:       crate(%{pkgname}/tls-roots-common) = %{version}
Provides:       crate(%{pkgname}/tls-roots) = %{version}

%description -n %{name}+tls-roots
This metapackage enables feature "tls-roots" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-webpki-roots
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tls-webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tls-roots-common) = %{version}
Requires:       crate(%{pkgname}/webpki-roots) = %{version}
Provides:       crate(%{pkgname}/tls-webpki-roots) = %{version}

%description -n %{name}+tls-webpki-roots
This metapackage enables feature "tls-webpki-roots" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.1
Requires:       crate(tokio-1/net) >= 1.0.1
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-rustls
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tokio-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-rustls-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/tokio-rustls) = %{version}

%description -n %{name}+tokio-rustls
This metapackage enables feature "tokio-rustls" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tower
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tower"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tower-0.4/balance) >= 0.4.7
Requires:       crate(tower-0.4/buffer) >= 0.4.7
Requires:       crate(tower-0.4/default) >= 0.4.7
Requires:       crate(tower-0.4/discover) >= 0.4.7
Requires:       crate(tower-0.4/limit) >= 0.4.7
Requires:       crate(tower-0.4/load) >= 0.4.7
Requires:       crate(tower-0.4/make) >= 0.4.7
Requires:       crate(tower-0.4/timeout) >= 0.4.7
Requires:       crate(tower-0.4/util) >= 0.4.7
Provides:       crate(%{pkgname}/tower) = %{version}

%description -n %{name}+tower
This metapackage enables feature "tower" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-futures
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "tracing-futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-futures-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/tracing-futures) = %{version}

%description -n %{name}+tracing-futures
This metapackage enables feature "tracing-futures" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+transport
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "transport"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/h2) = %{version}
Requires:       crate(%{pkgname}/hyper) = %{version}
Requires:       crate(%{pkgname}/hyper-timeout) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/tower) = %{version}
Requires:       crate(%{pkgname}/tracing-futures) = %{version}
Requires:       crate(tokio-1/macros) >= 1.0.1
Requires:       crate(tokio-1/net) >= 1.0.1
Requires:       crate(tokio-1/time) >= 1.0.1
Provides:       crate(%{pkgname}/transport) = %{version}

%description -n %{name}+transport
This metapackage enables feature "transport" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webpki-roots
Summary:        GRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility - feature "webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(webpki-roots-0.21/default) >= 0.21.1
Provides:       crate(%{pkgname}/webpki-roots) = %{version}

%description -n %{name}+webpki-roots
This metapackage enables feature "webpki-roots" for the Rust tonic crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
