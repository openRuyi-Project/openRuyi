# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qcongestion
%global full_version 0.7.0
%global pkgname qcongestion-0.7

Name:           rust-qcongestion-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "qcongestion"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:c95adba81e48aa5347f5594401359f891c0d1e4c3228f6e5d2742d6fbc4ee738
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(qbase-0.7/default) >= 0.7.0
Requires:       crate(qevent-0.7/default) >= 0.7.0
Requires:       crate(rand-0.10/default) >= 0.10.0
Requires:       crate(thiserror-2/default) >= 2.0.20
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qcongestion"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
