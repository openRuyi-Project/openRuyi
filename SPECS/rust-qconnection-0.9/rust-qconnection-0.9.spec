# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qconnection
%global full_version 0.9.0
%global pkgname qconnection-0.9

Name:           rust-qconnection-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "qconnection"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:3ab6cf9495670da09b9d610eecb66ea10b1dde3f519ad5975fd1bb1d02b3bfbf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(qbase-0.7/default) >= 0.7.0
Requires:       crate(qcongestion-0.7/default) >= 0.7.0
Requires:       crate(qprotocol-0.7/default) >= 0.7.0
Requires:       crate(qrecovery-0.7/default) >= 0.7.0
Requires:       crate(qresolve-0.9/default) >= 0.9.0
Requires:       crate(qtls-0.1/default) >= 0.1.0
Requires:       crate(qtransport-0.1/default) >= 0.1.0
Requires:       crate(qtraversal-0.8/default) >= 0.8.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qconnection"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
