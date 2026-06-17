# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name netlink-proto
%global full_version 0.12.0
%global pkgname netlink-proto-0.12

Name:           rust-netlink-proto-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "netlink-proto"
License:        MIT
URL:            https://github.com/rust-netlink/netlink-proto
#!RemoteAsset:  sha256:b65d130ee111430e47eed7896ea43ca693c387f097dd97376bffafbf25812128
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(log-0.4/default) >= 0.4.8
Requires:       crate(netlink-packet-core-0.8/default) >= 0.8.0
Requires:       crate(netlink-sys-0.8) >= 0.8.4
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "netlink-proto"

%package     -n %{name}+smol-socket
Summary:        Async netlink protocol - feature "smol_socket"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(netlink-sys-0.8/smol-socket) >= 0.8.4
Provides:       crate(%{pkgname}/smol-socket) = %{version}

%description -n %{name}+smol-socket
This metapackage enables feature "smol_socket" for the Rust netlink-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-socket
Summary:        Async netlink protocol - feature "tokio_socket" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(netlink-sys-0.8/tokio-socket) >= 0.8.4
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/tokio-socket) = %{version}

%description -n %{name}+tokio-socket
This metapackage enables feature "tokio_socket" for the Rust netlink-proto crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
