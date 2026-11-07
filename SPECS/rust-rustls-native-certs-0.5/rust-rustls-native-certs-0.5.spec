# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls-native-certs
%global full_version 0.5.0
%global pkgname rustls-native-certs-0.5

Name:           rust-rustls-native-certs-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "rustls-native-certs"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/ctz/rustls-native-certs
#!RemoteAsset:  sha256:5a07b7c1885bd8ed3831c289b7870b13ef46fe0e856d288c30d9cc17d75a2092
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(openssl-probe-0.1/default) >= 0.1.2
Requires:       crate(schannel-0.1/default) >= 0.1.15
Requires:       crate(security-framework-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rustls-native-certs"

%package     -n %{name}+rustls
Summary:        Rustls-native-certs allows rustls to use the platform native certificate store - feature "rustls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-0.19/default) >= 0.19.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust rustls-native-certs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
