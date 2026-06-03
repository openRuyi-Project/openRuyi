# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name native-tls
%global full_version 0.2.14
%global pkgname native-tls-0.2

Name:           rust-native-tls-0.2
Version:        0.2.14
Release:        %autorelease
Summary:        Rust crate "native-tls"
License:        MIT OR Apache-2.0
URL:            https://github.com/sfackler/rust-native-tls
#!RemoteAsset:  sha256:87de3442987e9dbec73158d5c715e7ad9072fda936bb03d19d7fa10e00520f0e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.174
Requires:       crate(log-0.4/default) >= 0.4.27
Requires:       crate(openssl-0.10/default) >= 0.10.78
Requires:       crate(openssl-probe-0.1/default) >= 0.1.6
Requires:       crate(openssl-sys-0.9/default) >= 0.9.114
Requires:       crate(schannel-0.1/default) >= 0.1.27
Requires:       crate(security-framework-2.0/default) >= 2.11.1
Requires:       crate(security-framework-sys-2.0/default) >= 2.14.0
Requires:       crate(tempfile-3.0/default) >= 3.20.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "native-tls"

%package     -n %{name}+alpn
Summary:        Wrapper over a platform's native TLS implementation - feature "alpn"
Requires:       crate(%{pkgname})
Requires:       crate(security-framework-2.0/alpn) >= 2.11.1
Provides:       crate(%{pkgname}/alpn)

%description -n %{name}+alpn
This metapackage enables feature "alpn" for the Rust native-tls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored
Summary:        Wrapper over a platform's native TLS implementation - feature "vendored"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-0.10/vendored) >= 0.10.78
Provides:       crate(%{pkgname}/vendored)

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust native-tls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
