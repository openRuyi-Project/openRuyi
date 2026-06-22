# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-global-executor
%global full_version 2.4.1
%global pkgname async-global-executor-2

Name:           rust-async-global-executor-2
Version:        2.4.1
Release:        %autorelease
Summary:        Rust crate "async-global-executor"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Keruspe/async-global-executor
#!RemoteAsset:  sha256:05b1b633a2115cd122d73b955eadd9916c18c8f510ec9cd1686404c60ad1c29c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-channel-2/default) >= 2.1.1
Requires:       crate(async-executor-1/default) >= 1.8.0
Requires:       crate(async-lock-3/default) >= 3.2.0
Requires:       crate(blocking-1/default) >= 1.5.0
Requires:       crate(futures-lite-2/default) >= 2.0.0
Requires:       crate(once-cell-1/default) >= 1.4.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "async-global-executor"

%package     -n %{name}+async-io
Summary:        Global executor built on top of async-executor and async-io - feature "async-io" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-io-2/default) >= 2.2.1
Provides:       crate(%{pkgname}/async-io) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+async-io
This metapackage enables feature "async-io" for the Rust async-global-executor crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio-crate
Summary:        Global executor built on top of async-executor and async-io - feature "tokio-crate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/tokio-crate) = %{version}

%description -n %{name}+tokio-crate
This metapackage enables feature "tokio-crate" for the Rust async-global-executor crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tokio" feature.

%package     -n %{name}+tokio02-crate
Summary:        Global executor built on top of async-executor and async-io - feature "tokio02-crate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-0.2/rt-core) >= 0.2.0
Provides:       crate(%{pkgname}/tokio02) = %{version}
Provides:       crate(%{pkgname}/tokio02-crate) = %{version}

%description -n %{name}+tokio02-crate
This metapackage enables feature "tokio02-crate" for the Rust async-global-executor crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tokio02" feature.

%package     -n %{name}+tokio03-crate
Summary:        Global executor built on top of async-executor and async-io - feature "tokio03-crate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-0.3/rt) >= 0.3.4
Requires:       crate(tokio-0.3/rt-multi-thread) >= 0.3.4
Provides:       crate(%{pkgname}/tokio03) = %{version}
Provides:       crate(%{pkgname}/tokio03-crate) = %{version}

%description -n %{name}+tokio03-crate
This metapackage enables feature "tokio03-crate" for the Rust async-global-executor crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tokio03" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
