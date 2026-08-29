# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name native-tls
%global full_version 0.2.18
%global pkgname native-tls-0.2

Name:           rust-native-tls-0.2
Version:        0.2.18
Release:        %autorelease
Summary:        Rust crate "native-tls"
License:        MIT OR Apache-2.0
URL:            https://lib.rs/crates/native-tls
#!RemoteAsset:  sha256:465500e14ea162429d264d44189adc38b199b62b1c21eea9f69e4b73cb03bbf2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.170
Requires:       crate(log-0.4/default) >= 0.4.27
Requires:       crate(openssl-0.10/default) >= 0.10.75
Requires:       crate(openssl-probe-0.2/default) >= 0.2.1
Requires:       crate(openssl-sys-0.9/default) >= 0.9.111
Requires:       crate(schannel-0.1/default) >= 0.1.28
Requires:       crate(security-framework-3/default) >= 3.5.1
Requires:       crate(security-framework-sys-2/default) >= 2.15.0
Requires:       crate(tempfile-3/default) >= 3.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alpn-accept) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "native-tls"

%package     -n %{name}+alpn
Summary:        Wrapper over a platform's native TLS implementation - feature "alpn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(security-framework-3/alpn) >= 3.5.1
Provides:       crate(%{pkgname}/alpn) = %{version}

%description -n %{name}+alpn
This metapackage enables feature "alpn" for the Rust native-tls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored
Summary:        Wrapper over a platform's native TLS implementation - feature "vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-0.10/vendored) >= 0.10.75
Provides:       crate(%{pkgname}/vendored) = %{version}

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust native-tls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
