# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atspi
%global full_version 0.25.0
%global pkgname atspi-0.25

Name:           rust-atspi-0.25
Version:        0.25.0
Release:        %autorelease
Summary:        Rust crate "atspi"
License:        Apache-2.0 OR MIT
URL:            https://github.com/odilia-app/atspi
#!RemoteAsset:  sha256:c83247582e7508838caf5f316c00791eee0e15c0bf743e6880585b867e16815c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atspi-common-0.9) >= 0.9.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/connection) = %{version}
Provides:       crate(%{pkgname}/proxies) = %{version}

%description
Source code for takopackized Rust crate "atspi"

%package     -n %{name}+async-std
Summary:        Pure-Rust, zbus-based AT-SPI2 protocol implementation - feature "async-std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/connection-async-std) = %{version}
Requires:       crate(%{pkgname}/proxies-async-std) = %{version}
Provides:       crate(%{pkgname}/async-std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust atspi crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+atspi-connection
Summary:        Pure-Rust, zbus-based AT-SPI2 protocol implementation - feature "atspi-connection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atspi-connection-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/atspi-connection) = %{version}

%description -n %{name}+atspi-connection
This metapackage enables feature "atspi-connection" for the Rust atspi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+atspi-proxies
Summary:        Pure-Rust, zbus-based AT-SPI2 protocol implementation - feature "atspi-proxies"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atspi-proxies-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/atspi-proxies) = %{version}

%description -n %{name}+atspi-proxies
This metapackage enables feature "atspi-proxies" for the Rust atspi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+connection-async-std
Summary:        Pure-Rust, zbus-based AT-SPI2 protocol implementation - feature "connection-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/connection) = %{version}
Requires:       crate(atspi-connection-0.9/async-std) >= 0.9.0
Provides:       crate(%{pkgname}/connection-async-std) = %{version}

%description -n %{name}+connection-async-std
This metapackage enables feature "connection-async-std" for the Rust atspi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+connection-tokio
Summary:        Pure-Rust, zbus-based AT-SPI2 protocol implementation - feature "connection-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/connection) = %{version}
Requires:       crate(atspi-connection-0.9/tokio) >= 0.9.0
Provides:       crate(%{pkgname}/connection-tokio) = %{version}

%description -n %{name}+connection-tokio
This metapackage enables feature "connection-tokio" for the Rust atspi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proxies-async-std
Summary:        Pure-Rust, zbus-based AT-SPI2 protocol implementation - feature "proxies-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proxies) = %{version}
Requires:       crate(atspi-proxies-0.9/async-std) >= 0.9.0
Provides:       crate(%{pkgname}/proxies-async-std) = %{version}

%description -n %{name}+proxies-async-std
This metapackage enables feature "proxies-async-std" for the Rust atspi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proxies-tokio
Summary:        Pure-Rust, zbus-based AT-SPI2 protocol implementation - feature "proxies-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proxies) = %{version}
Requires:       crate(atspi-proxies-0.9/tokio) >= 0.9.0
Provides:       crate(%{pkgname}/proxies-tokio) = %{version}

%description -n %{name}+proxies-tokio
This metapackage enables feature "proxies-tokio" for the Rust atspi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Pure-Rust, zbus-based AT-SPI2 protocol implementation - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/connection-tokio) = %{version}
Requires:       crate(%{pkgname}/proxies-tokio) = %{version}
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust atspi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Pure-Rust, zbus-based AT-SPI2 protocol implementation - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atspi-connection-0.9/tracing) >= 0.9.0
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust atspi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zbus
Summary:        Pure-Rust, zbus-based AT-SPI2 protocol implementation - feature "zbus"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zbus-5) >= 5.5.0
Provides:       crate(%{pkgname}/zbus) = %{version}

%description -n %{name}+zbus
This metapackage enables feature "zbus" for the Rust atspi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
