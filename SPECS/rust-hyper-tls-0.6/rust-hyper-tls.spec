# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyper-tls
%global full_version 0.6.0
%global pkgname hyper-tls-0.6

Name:           rust-hyper-tls-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "hyper-tls"
License:        MIT OR Apache-2.0
URL:            https://hyper.rs
#!RemoteAsset:  sha256:70206fc6890eaca9fde8a0bf71caa2ddfc9fe045ac9e5c70df101a7dbde866e0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1.0/default) >= 1.11.1
Requires:       crate(http-body-util-0.1/default) >= 0.1.3
Requires:       crate(hyper-1.0/default) >= 1.6.0
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.14
Requires:       crate(hyper-util-0.1/default) >= 0.1.14
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.14
Requires:       crate(native-tls-0.2/default) >= 0.2.14
Requires:       crate(tokio-1.0/default) >= 1.46.0
Requires:       crate(tokio-native-tls-0.3/default) >= 0.3.1
Requires:       crate(tower-service-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "hyper-tls"

%package     -n %{name}+alpn
Summary:        Default TLS implementation for use with hyper - feature "alpn"
Requires:       crate(%{pkgname})
Requires:       crate(native-tls-0.2/alpn) >= 0.2.14
Provides:       crate(%{pkgname}/alpn)

%description -n %{name}+alpn
This metapackage enables feature "alpn" for the Rust hyper-tls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored
Summary:        Default TLS implementation for use with hyper - feature "vendored"
Requires:       crate(%{pkgname})
Requires:       crate(native-tls-0.2/vendored) >= 0.2.14
Provides:       crate(%{pkgname}/vendored)

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust hyper-tls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
