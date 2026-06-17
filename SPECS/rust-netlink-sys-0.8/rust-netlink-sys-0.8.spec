# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name netlink-sys
%global full_version 0.8.7
%global pkgname netlink-sys-0.8

Name:           rust-netlink-sys-0.8
Version:        0.8.7
Release:        %autorelease
Summary:        Rust crate "netlink-sys"
License:        MIT
URL:            https://github.com/rust-netlink/netlink-sys
#!RemoteAsset:  sha256:16c903aa70590cb93691bf97a767c8d1d6122d2cc9070433deb3bbf36ce8bd23
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.8.0
Requires:       crate(libc-0.2/default) >= 0.2.164
Requires:       crate(log-0.4/default) >= 0.4.8
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "netlink-sys"

%package     -n %{name}+async-io
Summary:        Netlink sockets, with optional integration with tokio - feature "async-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-io-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/async-io) = %{version}

%description -n %{name}+async-io
This metapackage enables feature "async-io" for the Rust netlink-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Netlink sockets, with optional integration with tokio - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.31
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust netlink-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio
Summary:        Netlink sockets, with optional integration with tokio - feature "mio" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-1/default) >= 1.0.0
Requires:       crate(mio-1/os-ext) >= 1.0.0
Requires:       crate(mio-1/os-poll) >= 1.0.0
Provides:       crate(%{pkgname}/mio) = %{version}
Provides:       crate(%{pkgname}/mio-socket) = %{version}

%description -n %{name}+mio
This metapackage enables feature "mio" for the Rust netlink-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "mio_socket" feature.

%package     -n %{name}+smol-socket
Summary:        Netlink sockets, with optional integration with tokio - feature "smol_socket"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-io) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Provides:       crate(%{pkgname}/smol-socket) = %{version}

%description -n %{name}+smol-socket
This metapackage enables feature "smol_socket" for the Rust netlink-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Netlink sockets, with optional integration with tokio - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/net) >= 1.41.1
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust netlink-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-socket
Summary:        Netlink sockets, with optional integration with tokio - feature "tokio_socket"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/tokio-socket) = %{version}

%description -n %{name}+tokio-socket
This metapackage enables feature "tokio_socket" for the Rust netlink-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
