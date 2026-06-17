# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name blocking
%global full_version 1.6.2
%global pkgname blocking-1

Name:           rust-blocking-1
Version:        1.6.2
Release:        %autorelease
Summary:        Rust crate "blocking"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/blocking
#!RemoteAsset:  sha256:e83f8d02be6967315521be875afa792a316e28d57b5a2d401897e2a7921b7f21
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-channel-2/default) >= 2.0.0
Requires:       crate(async-task-4/default) >= 4.4.0
Requires:       crate(futures-io-0.3/std) >= 0.3.28
Requires:       crate(futures-lite-2) >= 2.0.0
Requires:       crate(piper-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "blocking"

%package     -n %{name}+tracing
Summary:        Thread pool for isolating blocking I/O in async programs - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.37
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust blocking crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
