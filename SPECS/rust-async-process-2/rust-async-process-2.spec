# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-process
%global full_version 2.5.0
%global pkgname async-process-2

Name:           rust-async-process-2
Version:        2.5.0
Release:        %autorelease
Summary:        Rust crate "async-process"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-process
#!RemoteAsset:  sha256:fc50921ec0055cdd8a16de48773bfeec5c972598674347252c0399676be7da75
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-channel-2/default) >= 2.0.0
Requires:       crate(async-io-2/default) >= 2.3.0
Requires:       crate(async-lock-3/default) >= 3.0.0
Requires:       crate(async-signal-0.2/default) >= 0.2.3
Requires:       crate(async-task-4/default) >= 4.7.0
Requires:       crate(blocking-1/default) >= 1.0.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(event-listener-5/default) >= 5.1.0
Requires:       crate(futures-lite-2/default) >= 2.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0
Requires:       crate(rustix-1/process) >= 1.0.0
Requires:       crate(rustix-1/std) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-process"

%package     -n %{name}+tracing
Summary:        Async interface for working with processes - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.40
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust async-process crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
