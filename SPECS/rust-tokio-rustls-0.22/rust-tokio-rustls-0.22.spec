# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-rustls
%global full_version 0.22.0
%global pkgname tokio-rustls-0.22

Name:           rust-tokio-rustls-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "tokio-rustls"
License:        MIT OR Apache-2.0
URL:            https://github.com/tokio-rs/tls
#!RemoteAsset:  sha256:bc6844de72e57df1980054b38be3a9f4702aba4858be64dd700181a8a6d0e1b6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustls-0.19/default) >= 0.19.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(webpki-0.21/default) >= 0.21.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/early-data) = %{version}

%description
Source code for takopackized Rust crate "tokio-rustls"

%package     -n %{name}+dangerous-configuration
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls - feature "dangerous_configuration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.19/dangerous-configuration) >= 0.19.0
Provides:       crate(%{pkgname}/dangerous-configuration) = %{version}

%description -n %{name}+dangerous-configuration
This metapackage enables feature "dangerous_configuration" for the Rust tokio-rustls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
