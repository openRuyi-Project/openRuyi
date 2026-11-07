# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyper-tls
%global full_version 0.5.0
%global pkgname hyper-tls-0.5

Name:           rust-hyper-tls-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "hyper-tls"
License:        MIT OR Apache-2.0
URL:            https://hyper.rs
#!RemoteAsset:  sha256:d6183ddfa99b85da61a140bea0efc93fdf56ceaa041b37d553518030827f9905
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(hyper-0.14/client) >= 0.14.2
Requires:       crate(hyper-0.14/tcp) >= 0.14.2
Requires:       crate(native-tls-0.2/default) >= 0.2.1
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-native-tls-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hyper-tls"

%package     -n %{name}+vendored
Summary:        Default TLS implementation for use with hyper - feature "vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(native-tls-0.2/vendored) >= 0.2.1
Provides:       crate(%{pkgname}/vendored) = %{version}

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust hyper-tls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
