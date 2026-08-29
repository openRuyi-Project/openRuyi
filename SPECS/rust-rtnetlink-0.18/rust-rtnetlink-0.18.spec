# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rtnetlink
%global full_version 0.18.1
%global pkgname rtnetlink-0.18

Name:           rust-rtnetlink-0.18
Version:        0.18.1
Release:        %autorelease
Summary:        Rust crate "rtnetlink"
License:        MIT
URL:            https://github.com/rust-netlink/rtnetlink
#!RemoteAsset:  sha256:08fd15aa4c64c34d0b3178e45ec6dad313a9f02b193376d501668a7950264bb7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-0.3/default) >= 0.3.11
Requires:       crate(log-0.4/default) >= 0.4.8
Requires:       crate(netlink-packet-core-0.8/default) >= 0.8.0
Requires:       crate(netlink-packet-route-0.25/default) >= 0.25.0
Requires:       crate(netlink-proto-0.12) >= 0.12.0
Requires:       crate(netlink-sys-0.8/default) >= 0.8.0
Requires:       crate(nix-0.29/fs) >= 0.29.0
Requires:       crate(nix-0.29/mount) >= 0.29.0
Requires:       crate(nix-0.29/sched) >= 0.29.0
Requires:       crate(nix-0.29/signal) >= 0.29.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/test-as-root) = %{version}

%description
Source code for takopackized Rust crate "rtnetlink"

%package     -n %{name}+async-global-executor
Summary:        Manipulate linux networking resources via netlink - feature "async-global-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-global-executor-2/default) >= 2.0.2
Provides:       crate(%{pkgname}/async-global-executor) = %{version}

%description -n %{name}+async-global-executor
This metapackage enables feature "async-global-executor" for the Rust rtnetlink crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol-socket
Summary:        Manipulate linux networking resources via netlink - feature "smol_socket"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-global-executor) = %{version}
Requires:       crate(netlink-proto-0.12/smol-socket) >= 0.12.0
Provides:       crate(%{pkgname}/smol-socket) = %{version}

%description -n %{name}+smol-socket
This metapackage enables feature "smol_socket" for the Rust rtnetlink crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Manipulate linux networking resources via netlink - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.1
Requires:       crate(tokio-1/rt) >= 1.0.1
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust rtnetlink crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-socket
Summary:        Manipulate linux networking resources via netlink - feature "tokio_socket" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(netlink-proto-0.12/tokio-socket) >= 0.12.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/tokio-socket) = %{version}

%description -n %{name}+tokio-socket
This metapackage enables feature "tokio_socket" for the Rust rtnetlink crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
