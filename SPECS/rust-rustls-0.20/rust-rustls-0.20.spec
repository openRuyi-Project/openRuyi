# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls
%global full_version 0.20.9
%global pkgname rustls-0.20

Name:           rust-rustls-0.20
Version:        0.20.9
Release:        %autorelease
Summary:        Rust crate "rustls"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/rustls/rustls
#!RemoteAsset:  sha256:1b80e3dec595989ea8510028f30c408a4630db12c9cbb8de34203b89d6577e99
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ring-0.16/default) >= 0.16.20
Requires:       crate(sct-0.7/default) >= 0.7.0
Requires:       crate(webpki-0.22/alloc) >= 0.22.0
Requires:       crate(webpki-0.22/default) >= 0.22.0
Requires:       crate(webpki-0.22/std) >= 0.22.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/dangerous-configuration) = %{version}
Provides:       crate(%{pkgname}/quic) = %{version}
Provides:       crate(%{pkgname}/secret-extraction) = %{version}
Provides:       crate(%{pkgname}/tls12) = %{version}

%description
Source code for takopackized Rust crate "rustls"

%package     -n %{name}+default
Summary:        Modern TLS library written in Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/tls12) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Modern TLS library written in Rust - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/log) = %{version}
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "logging" feature.

%package     -n %{name}+rustversion
Summary:        Modern TLS library written in Rust - feature "rustversion" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustversion-1/default) >= 1.0.6
Provides:       crate(%{pkgname}/read-buf) = %{version}
Provides:       crate(%{pkgname}/rustversion) = %{version}

%description -n %{name}+rustversion
This metapackage enables feature "rustversion" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "read_buf" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
