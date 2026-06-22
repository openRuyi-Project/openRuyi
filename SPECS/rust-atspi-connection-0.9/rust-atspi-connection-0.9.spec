# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atspi-connection
%global full_version 0.9.0
%global pkgname atspi-connection-0.9

Name:           rust-atspi-connection-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "atspi-connection"
License:        Apache-2.0 OR MIT
URL:            https://github.com/odilia-app/atspi/
#!RemoteAsset:  sha256:4193d51303d8332304056ae0004714256b46b6635a5c556109b319c0d3784938
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atspi-common-0.9/wrappers) >= 0.9.0
Requires:       crate(atspi-proxies-0.9) >= 0.9.0
Requires:       crate(futures-lite-2) >= 2.0.0
Requires:       crate(zbus-5) >= 5.5.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "atspi-connection"

%package     -n %{name}+async-std
Summary:        Method of connecting, querying, sending and receiving over AT-SPI - feature "async-std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atspi-common-0.9/async-std) >= 0.9.0
Requires:       crate(atspi-common-0.9/wrappers) >= 0.9.0
Requires:       crate(atspi-proxies-0.9/async-std) >= 0.9.0
Requires:       crate(zbus-5/async-io) >= 5.5.0
Provides:       crate(%{pkgname}/async-std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust atspi-connection crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio
Summary:        Method of connecting, querying, sending and receiving over AT-SPI - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atspi-common-0.9/tokio) >= 0.9.0
Requires:       crate(atspi-common-0.9/wrappers) >= 0.9.0
Requires:       crate(atspi-proxies-0.9/tokio) >= 0.9.0
Requires:       crate(zbus-5/tokio) >= 5.5.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust atspi-connection crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Method of connecting, querying, sending and receiving over AT-SPI - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/default) >= 0.1.37
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust atspi-connection crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
