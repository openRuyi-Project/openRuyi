# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-io
%global full_version 2.6.0
%global pkgname async-io-2

Name:           rust-async-io-2
Version:        2.6.0
Release:        %autorelease
Summary:        Rust crate "async-io"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-io
#!RemoteAsset:  sha256:456b8a8feb6f42d237746d4b3e9a178494627745c3c56c6ea55d92ba50d026fc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(concurrent-queue-2/default) >= 2.2.0
Requires:       crate(futures-io-0.3/std) >= 0.3.28
Requires:       crate(futures-lite-2) >= 2.0.0
Requires:       crate(parking-2/default) >= 2.0.0
Requires:       crate(polling-3/default) >= 3.4.0
Requires:       crate(rustix-1/fs) >= 1.0.7
Requires:       crate(rustix-1/net) >= 1.0.7
Requires:       crate(rustix-1/std) >= 1.0.7
Requires:       crate(slab-0.4/default) >= 0.4.2
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-io"

%package     -n %{name}+tracing
Summary:        Async I/O and timers - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.37
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust async-io crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
