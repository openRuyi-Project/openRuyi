# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atspi-proxies
%global full_version 0.9.0
%global pkgname atspi-proxies-0.9

Name:           rust-atspi-proxies-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "atspi-proxies"
License:        Apache-2.0 OR MIT
URL:            https://github.com/odilia-app/atspi
#!RemoteAsset:  sha256:d2eebcb9e7e76f26d0bcfd6f0295e1cd1e6f33bedbc5698a971db8dc43d7751c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atspi-common-0.9) >= 0.9.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(zbus-5) >= 5.5.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "atspi-proxies"

%package     -n %{name}+async-std
Summary:        AT-SPI2 proxies to query or manipulate UI objects - feature "async-std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atspi-common-0.9/async-std) >= 0.9.0
Requires:       crate(zbus-5/async-io) >= 5.5.0
Provides:       crate(%{pkgname}/async-std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust atspi-proxies crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio
Summary:        AT-SPI2 proxies to query or manipulate UI objects - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atspi-common-0.9/tokio) >= 0.9.0
Requires:       crate(zbus-5/tokio) >= 5.5.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust atspi-proxies crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
