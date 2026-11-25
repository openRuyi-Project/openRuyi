# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qtraversal
%global full_version 0.8.0
%global pkgname qtraversal-0.8

Name:           rust-qtraversal-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "qtraversal"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:f9e573c395a0b45f64659f0f6d4707a8bdd463a6195426d58e83c8e1ce955da6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(dashmap-6/default) >= 6.0.0
Requires:       crate(qbase-0.7/default) >= 0.7.0
Requires:       crate(qprotocol-0.7/default) >= 0.7.0
Requires:       crate(qtransport-0.1/default) >= 0.1.0
Requires:       crate(rand-0.10/default) >= 0.10.0
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
Source code for takopackized Rust crate "qtraversal"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
