# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qevent
%global full_version 0.7.0
%global pkgname qevent-0.7

Name:           rust-qevent-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "qevent"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:5a7c9bde6b05cb097c970655848bfcc20c1f1458c0272c0ff7bda7d38a2023ff
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(derive-builder-0.20/default) >= 0.20.0
Requires:       crate(derive-more-2/default) >= 2.0.0
Requires:       crate(derive-more-2/display) >= 2.0.0
Requires:       crate(derive-more-2/from) >= 2.0.0
Requires:       crate(derive-more-2/into) >= 2.0.0
Requires:       crate(enum-dispatch-0.3/default) >= 0.3.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Requires:       crate(qbase-0.7/default) >= 0.7.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(serde-with-3/default) >= 3.0.0
Requires:       crate(serde-with-3/hex) >= 3.0.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/io-std) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/raw-data) = %{version}
Provides:       crate(%{pkgname}/telemetry) = %{version}

%description
Source code for takopackized Rust crate "qevent"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
