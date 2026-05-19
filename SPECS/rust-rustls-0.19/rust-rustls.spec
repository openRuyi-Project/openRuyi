# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls
%global full_version 0.19.1
%global pkgname rustls-0.19

Name:           rust-rustls-0.19
Version:        0.19.1
Release:        %autorelease
Summary:        Rust crate "rustls"
License:        Apache-2.0/ISC/MIT
URL:            https://github.com/ctz/rustls
#!RemoteAsset:  sha256:35edb675feee39aec9c99fa5ff985081995a06d594114ae14cbe797ad7b7a6d7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.13/default) >= 0.13.0
Requires:       crate(ring-0.16/default) >= 0.16.11
Requires:       crate(sct-0.6/default) >= 0.6.0
Requires:       crate(webpki-0.21/default) >= 0.21.0
Provides:       crate(rustls) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/dangerous-configuration)
Provides:       crate(%{pkgname}/quic)

%description
Source code for takopackized Rust crate "rustls"

%package     -n %{name}+log
Summary:        Modern TLS library written in Rust - feature "log" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/log)
Provides:       crate(%{pkgname}/logging)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "logging" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
