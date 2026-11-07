# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quinn-proto
%global full_version 0.10.6
%global pkgname quinn-proto-0.10

Name:           rust-quinn-proto-0.10
Version:        0.10.6
Release:        %autorelease
Summary:        Rust crate "quinn-proto"
License:        MIT OR Apache-2.0
URL:            https://github.com/quinn-rs/quinn
#!RemoteAsset:  sha256:141bf7dfde2fbc246bfd3fe12f2455aa24b0fbd9af535d8c86c7bd1381ff2b1a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(rand-0.8/default) >= 0.8.0
Requires:       crate(rustc-hash-1/default) >= 1.1.0
Requires:       crate(slab-0.4/default) >= 0.4.0
Requires:       crate(thiserror-1/default) >= 1.0.21
Requires:       crate(tinyvec-1/alloc) >= 1.1.0
Requires:       crate(tinyvec-1/default) >= 1.1.0
Requires:       crate(tracing-0.1/default) >= 0.1.10

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "quinn-proto"

%package     -n %{name}+arbitrary
Summary:        State machine for the QUIC transport protocol - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.1
Requires:       crate(arbitrary-1/derive) >= 1.0.1
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        State machine for the QUIC transport protocol - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(%{pkgname}/tls-rustls) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        State machine for the QUIC transport protocol - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/log) >= 0.1.10
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        State machine for the QUIC transport protocol - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ring-0.16/default) >= 0.16.7
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        State machine for the QUIC transport protocol - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.21/quic) >= 0.21.0
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-native-certs
Summary:        State machine for the QUIC transport protocol - feature "rustls-native-certs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-native-certs-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/native-certs) = %{version}
Provides:       crate(%{pkgname}/rustls-native-certs) = %{version}

%description -n %{name}+rustls-native-certs
This metapackage enables feature "rustls-native-certs" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "native-certs" feature.

%package     -n %{name}+tls-rustls
Summary:        State machine for the QUIC transport protocol - feature "tls-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ring) = %{version}
Requires:       crate(%{pkgname}/rustls) = %{version}
Provides:       crate(%{pkgname}/tls-rustls) = %{version}

%description -n %{name}+tls-rustls
This metapackage enables feature "tls-rustls" for the Rust quinn-proto crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
