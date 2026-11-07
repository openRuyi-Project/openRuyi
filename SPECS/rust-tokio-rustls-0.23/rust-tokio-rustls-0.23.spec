# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-rustls
%global full_version 0.23.4
%global pkgname tokio-rustls-0.23

Name:           rust-tokio-rustls-0.23
Version:        0.23.4
Release:        %autorelease
Summary:        Rust crate "tokio-rustls"
License:        MIT OR Apache-2.0
URL:            https://github.com/tokio-rs/tls
#!RemoteAsset:  sha256:c43ee83903113e03984cb9e5cebe6c04a5116269e900e3ddba8f068a62adda59
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustls-0.20) >= 0.20.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(webpki-0.22/default) >= 0.22.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/early-data) = %{version}

%description
Source code for takopackized Rust crate "tokio-rustls"

%package     -n %{name}+dangerous-configuration
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "dangerous_configuration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.20/dangerous-configuration) >= 0.20.0
Provides:       crate(%{pkgname}/dangerous-configuration) = %{version}

%description -n %{name}+dangerous-configuration
This metapackage enables feature "dangerous_configuration" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/tls12) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.20/logging) >= 0.20.0
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls12
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "tls12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.20/tls12) >= 0.20.0
Provides:       crate(%{pkgname}/tls12) = %{version}

%description -n %{name}+tls12
This metapackage enables feature "tls12" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
