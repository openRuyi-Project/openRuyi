# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-net
%global full_version 0.30.1
%global pkgname sequoia-net-0.30

Name:           rust-sequoia-net-0.30
Version:        0.30.1
Release:        %autorelease
Summary:        Rust crate "sequoia-net"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:75c0ea4f555b2b109fb39d6c5ebdb614945d82da0105957591adf4641e9cc3b2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(base64-0.21/default) >= 0.21.0
Requires:       crate(futures-util-0.3/default) >= 0.3.5
Requires:       crate(hickory-client-0.24/default) >= 0.24.0
Requires:       crate(hickory-resolver-0.24/default) >= 0.24.0
Requires:       crate(hickory-resolver-0.24/dnssec-openssl) >= 0.24.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(hyper-1/default) >= 1.0.0
Requires:       crate(hyper-1/http1) >= 1.0.0
Requires:       crate(hyper-1/http2) >= 1.0.0
Requires:       crate(hyper-tls-0.6/default) >= 0.6.0
Requires:       crate(libc-0.2/default) >= 0.2.66
Requires:       crate(percent-encoding-2/default) >= 2.1.0
Requires:       crate(reqwest-0.12/default) >= 0.12.0
Requires:       crate(sequoia-openpgp-2) >= 2.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(tokio-1/default) >= 1.13.1
Requires:       crate(tokio-1/macros) >= 1.13.1
Requires:       crate(url-2/default) >= 2.1.0
Requires:       crate(z-base-32-0.1/default) >= 0.1.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-net"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
