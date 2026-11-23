# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mio
%global full_version 0.8.11
%global pkgname mio-0.8

Name:           rust-mio-0.8
Version:        0.8.11
Release:        %autorelease
Summary:        Rust crate "mio"
License:        MIT
URL:            https://github.com/tokio-rs/mio
#!RemoteAsset:  sha256:a4a650543ca06a924e8b371db273b2756685faae30f8487da1b56505a8f78b0c
Source:         https://static.crates.io/crates/mio/0.8.11/download#/rust-mio-0.8-0.8.11.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.149
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "mio"

%package     -n %{name}+log
Summary:        Lightweight non-blocking I/O - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.8
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust mio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+net
Summary:        Lightweight non-blocking I/O - feature "net" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/net) = %{version}
Provides:       crate(%{pkgname}/os-poll) = %{version}
Provides:       crate(%{pkgname}/os-ext) = %{version}

%description -n %{name}+net
This metapackage enables feature "net" for the Rust mio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "os-poll" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
