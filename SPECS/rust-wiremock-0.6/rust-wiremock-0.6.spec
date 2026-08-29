# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wiremock
%global full_version 0.6.5
%global pkgname wiremock-0.6

Name:           rust-wiremock-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "wiremock"
License:        MIT OR Apache-2.0
URL:            https://github.com/LukeMathWalker/wiremock-rs
#!RemoteAsset:  sha256:08db1edfb05d9b3c1542e521aea074442088292f00b5f28e435c714a98f85031
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(assert-json-diff-2/default) >= 2.0.2
Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(deadpool-0.12/default) >= 0.12.2
Requires:       crate(futures-0.3/default) >= 0.3.31
Requires:       crate(http-1/default) >= 1.3.0
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Requires:       crate(hyper-1/default) >= 1.7.0
Requires:       crate(hyper-1/full) >= 1.7.0
Requires:       crate(hyper-util-0.1/default) >= 0.1.0
Requires:       crate(hyper-util-0.1/http1) >= 0.1.0
Requires:       crate(hyper-util-0.1/http2) >= 0.1.0
Requires:       crate(hyper-util-0.1/server) >= 0.1.0
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(once-cell-1/default) >= 1.0.0
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(tokio-1/default) >= 1.47.1
Requires:       crate(tokio-1/macros) >= 1.47.1
Requires:       crate(tokio-1/net) >= 1.47.1
Requires:       crate(tokio-1/rt) >= 1.47.1
Requires:       crate(url-2/default) >= 2.5.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wiremock"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
