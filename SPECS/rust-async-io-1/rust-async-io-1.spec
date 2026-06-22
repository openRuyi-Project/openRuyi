# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-io
%global full_version 1.13.0
%global pkgname async-io-1

Name:           rust-async-io-1
Version:        1.13.0
Release:        %autorelease
Summary:        Rust crate "async-io"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-io
#!RemoteAsset:  sha256:0fc5b45d93ef0529756f812ca52e44c221b35341892d3dcc34132ac02f3dd2af
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-lock-2/default) >= 2.6.0
Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(concurrent-queue-2/default) >= 2.0.0
Requires:       crate(futures-lite-1/default) >= 1.11.0
Requires:       crate(log-0.4/default) >= 0.4.11
Requires:       crate(parking-2/default) >= 2.0.0
Requires:       crate(polling-2/default) >= 2.0.0
Requires:       crate(rustix-0.37/fs) >= 0.37.1
Requires:       crate(rustix-0.37/std) >= 0.37.1
Requires:       crate(slab-0.4/default) >= 0.4.2
Requires:       crate(socket2-0.4/all) >= 0.4.2
Requires:       crate(socket2-0.4/default) >= 0.4.2
Requires:       crate(waker-fn-1/default) >= 1.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-io"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
