# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qprotocol
%global full_version 0.7.0
%global pkgname qprotocol-0.7

Name:           rust-qprotocol-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "qprotocol"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:8548c54dbd080cef9ed3a6e79819da3e178ad15c010f73bf2346594bac5a152f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(dashmap-6/default) >= 6.0.0
Requires:       crate(derive-more-2/default) >= 2.0.0
Requires:       crate(derive-more-2/display) >= 2.0.0
Requires:       crate(derive-more-2/into) >= 2.0.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(netdev-0.46/default) >= 0.46.0
Requires:       crate(nom-8/default) >= 8.0.0
Requires:       crate(qbase-0.7/default) >= 0.7.0
Requires:       crate(qresolve-0.9/default) >= 0.9.0
Requires:       crate(qudp-0.8/default) >= 0.8.0
Requires:       crate(thiserror-2/default) >= 2.0.20
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/test-ttl) = %{version}

%description
Source code for takopackized Rust crate "qprotocol"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
