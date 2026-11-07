# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-socks
%global full_version 0.5.3
%global pkgname tokio-socks-0.5

Name:           rust-tokio-socks-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "tokio-socks"
License:        MIT
URL:            https://github.com/sticnarf/tokio-socks
#!RemoteAsset:  sha256:a7e2948f60dbe26b35f2c7fb74ac2854c1fddded0fe9d7548fcc674a246f7615
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1/default) >= 1.0.0
Requires:       crate(futures-util-0.3) >= 0.3.0
Requires:       crate(thiserror-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/tor) = %{version}

%description
Source code for takopackized Rust crate "tokio-socks"

%package     -n %{name}+futures-io
Summary:        Asynchronous SOCKS proxy support for Rust - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust tokio-socks crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Asynchronous SOCKS proxy support for Rust - feature "tokio" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust tokio-socks crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
