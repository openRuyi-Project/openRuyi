# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-channel
%global full_version 2.5.0
%global pkgname async-channel-2

Name:           rust-async-channel-2
Version:        2.5.0
Release:        %autorelease
Summary:        Rust crate "async-channel"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-channel
#!RemoteAsset:  sha256:924ed96dd52d1b75e9c1a3e6275715fd320f5f9439fb5a4a11fa51f4221158d2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(concurrent-queue-2) >= 2.5.0
Requires:       crate(event-listener-strategy-0.5) >= 0.5.4
Requires:       crate(futures-core-0.3) >= 0.3.5
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.11
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "async-channel"

%package     -n %{name}+portable-atomic
Summary:        Async multi-producer multi-consumer channel - feature "portable-atomic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(concurrent-queue-2/portable-atomic) >= 2.5.0
Requires:       crate(event-listener-strategy-0.5/portable-atomic) >= 0.5.4
Requires:       crate(portable-atomic-1/require-cas) >= 1.0.0
Requires:       crate(portable-atomic-util-0.2/alloc) >= 0.2.0
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust async-channel crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Async multi-producer multi-consumer channel - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(concurrent-queue-2/std) >= 2.5.0
Requires:       crate(event-listener-strategy-0.5/std) >= 0.5.4
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust async-channel crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
