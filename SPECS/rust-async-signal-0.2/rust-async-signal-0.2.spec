# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-signal
%global full_version 0.2.14
%global pkgname async-signal-0.2

Name:           rust-async-signal-0.2
Version:        0.2.14
Release:        %autorelease
Summary:        Rust crate "async-signal"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-signal
#!RemoteAsset:  sha256:52b5aaafa020cf5053a01f2a60e8ff5dccf550f0f77ec54a4e47285ac2bab485
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-io-2/default) >= 2.0.0
Requires:       crate(async-lock-3/default) >= 3.3.0
Requires:       crate(atomic-waker-1/default) >= 1.1.1
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(futures-core-0.3/default) >= 0.3.26
Requires:       crate(futures-io-0.3/default) >= 0.3.26
Requires:       crate(rustix-1/process) >= 1.0.7
Requires:       crate(rustix-1/std) >= 1.0.7
Requires:       crate(signal-hook-registry-1/default) >= 1.4.0
Requires:       crate(slab-0.4/default) >= 0.4.8
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-console) >= 0.61.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-signal"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
