# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quinn
%global full_version 0.10.2
%global pkgname quinn-0.10

Name:           rust-quinn-0.10
Version:        0.10.2
Release:        %autorelease
Summary:        Rust crate "quinn"
License:        MIT OR Apache-2.0
URL:            https://github.com/quinn-rs/quinn
#!RemoteAsset:  sha256:8cc2c5017e4b43d5995dcea317bc46c1e09404c0a9664d2908f7f02dfe943d75
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Requires:       crate(quinn-proto-0.10) >= 0.10.2
Requires:       crate(quinn-udp-0.4) >= 0.4.0
Requires:       crate(rustc-hash-1/default) >= 1.1.0
Requires:       crate(thiserror-1/default) >= 1.0.21
Requires:       crate(tokio-1/default) >= 1.28.1
Requires:       crate(tokio-1/sync) >= 1.28.1
Requires:       crate(tracing-0.1/default) >= 0.1.10

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/lock-tracking) = %{version}

%description
Source code for takopackized Rust crate "quinn"

%package     -n %{name}+async-io
Summary:        Versatile QUIC transport protocol implementation - feature "async-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-io-1/default) >= 1.6.0
Provides:       crate(%{pkgname}/async-io) = %{version}

%description -n %{name}+async-io
This metapackage enables feature "async-io" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Versatile QUIC transport protocol implementation - feature "async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.11.0
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Versatile QUIC transport protocol implementation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(%{pkgname}/native-certs) = %{version}
Requires:       crate(%{pkgname}/runtime-tokio) = %{version}
Requires:       crate(%{pkgname}/tls-rustls) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-io
Summary:        Versatile QUIC transport protocol implementation - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/default) >= 0.3.19
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Versatile QUIC transport protocol implementation - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-proto-0.10/log) >= 0.10.2
Requires:       crate(quinn-udp-0.4/log) >= 0.4.0
Requires:       crate(tracing-0.1/log) >= 0.1.10
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-certs
Summary:        Versatile QUIC transport protocol implementation - feature "native-certs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-proto-0.10/native-certs) >= 0.10.2
Provides:       crate(%{pkgname}/native-certs) = %{version}

%description -n %{name}+native-certs
This metapackage enables feature "native-certs" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Versatile QUIC transport protocol implementation - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quinn-proto-0.10/ring) >= 0.10.2
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-async-std
Summary:        Versatile QUIC transport protocol implementation - feature "runtime-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-io) = %{version}
Requires:       crate(%{pkgname}/async-std) = %{version}
Provides:       crate(%{pkgname}/runtime-async-std) = %{version}

%description -n %{name}+runtime-async-std
This metapackage enables feature "runtime-async-std" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-tokio
Summary:        Versatile QUIC transport protocol implementation - feature "runtime-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/net) >= 1.28.1
Requires:       crate(tokio-1/rt) >= 1.28.1
Requires:       crate(tokio-1/sync) >= 1.28.1
Requires:       crate(tokio-1/time) >= 1.28.1
Provides:       crate(%{pkgname}/runtime-tokio) = %{version}

%description -n %{name}+runtime-tokio
This metapackage enables feature "runtime-tokio" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Versatile QUIC transport protocol implementation - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.21/quic) >= 0.21.0
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-rustls
Summary:        Versatile QUIC transport protocol implementation - feature "tls-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ring) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Requires:       crate(quinn-proto-0.10/tls-rustls) >= 0.10.2
Provides:       crate(%{pkgname}/tls-rustls) = %{version}

%description -n %{name}+tls-rustls
This metapackage enables feature "tls-rustls" for the Rust quinn crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
