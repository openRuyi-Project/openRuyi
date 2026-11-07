# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-rustls
%global full_version 0.24.1
%global pkgname tokio-rustls-0.24

Name:           rust-tokio-rustls-0.24
Version:        0.24.1
Release:        %autorelease
Summary:        Rust crate "tokio-rustls"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustls/tokio-rustls
#!RemoteAsset:  sha256:c28327cf380ac148141087fbfb9de9d7bd4e84ab5d2c28fbc911d753de8a7081
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustls-0.21) >= 0.21.0
Requires:       crate(tokio-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/early-data) = %{version}

%description
Source code for takopackized Rust crate "tokio-rustls"

%package     -n %{name}+dangerous-configuration
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "dangerous_configuration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.21/dangerous-configuration) >= 0.21.0
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
Requires:       crate(rustls-0.21/logging) >= 0.21.0
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+secret-extraction
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "secret_extraction"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.21/secret-extraction) >= 0.21.0
Provides:       crate(%{pkgname}/secret-extraction) = %{version}

%description -n %{name}+secret-extraction
This metapackage enables feature "secret_extraction" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls12
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "tls12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.21/tls12) >= 0.21.0
Provides:       crate(%{pkgname}/tls12) = %{version}

%description -n %{name}+tls12
This metapackage enables feature "tls12" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
