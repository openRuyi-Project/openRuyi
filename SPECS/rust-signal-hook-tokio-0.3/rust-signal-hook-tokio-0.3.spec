# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name signal-hook-tokio
%global full_version 0.3.1
%global pkgname signal-hook-tokio-0.3

Name:           rust-signal-hook-tokio-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "signal-hook-tokio"
License:        Apache-2.0 OR MIT
URL:            https://github.com/vorner/signal-hook
#!RemoteAsset:  sha256:213241f76fb1e37e27de3b6aa1b068a2c333233b59cca6634f634b80a27ecf1e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(signal-hook-0.3/default) >= 0.3.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "signal-hook-tokio"

%package     -n %{name}+futures-core-0-3
Summary:        Tokio support for signal-hook - feature "futures-core-0_3" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-core-0-3) = %{version}
Provides:       crate(%{pkgname}/futures-v0-3) = %{version}

%description -n %{name}+futures-core-0-3
This metapackage enables feature "futures-core-0_3" for the Rust signal-hook-tokio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "futures-v0_3" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
