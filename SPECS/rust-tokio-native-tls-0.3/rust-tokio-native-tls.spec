# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-native-tls
%global full_version 0.3.1
%global pkgname tokio-native-tls-0.3

Name:           rust-tokio-native-tls-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "tokio-native-tls"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:bbae76ab933c85776efabc971569dd6119c580d8f5d448769dec1764bf796ef2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(native-tls-0.2/default) >= 0.2.14
Requires:       crate(tokio-1.0/default) >= 1.46.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "tokio-native-tls"

%package     -n %{name}+vendored
Summary:        TLS/SSL streams for Tokio using native-tls giving an implementation of TLS for nonblocking I/O streams - feature "vendored"
Requires:       crate(%{pkgname})
Requires:       crate(native-tls-0.2/vendored) >= 0.2.14
Provides:       crate(%{pkgname}/vendored)

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust tokio-native-tls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
