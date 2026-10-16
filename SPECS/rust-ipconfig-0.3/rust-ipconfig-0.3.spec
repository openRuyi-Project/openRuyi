# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ipconfig
%global full_version 0.3.4
%global pkgname ipconfig-0.3

Name:           rust-ipconfig-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "ipconfig"
License:        MIT OR Apache-2.0
URL:            https://github.com/liranringel/ipconfig
#!RemoteAsset:  sha256:4d40460c0ce33d6ce4b0630ad68ff63d6661961c48b6dba35e5a4d81cfb48222
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(socket2-0.6/default) >= 0.6.0
Requires:       crate(widestring-1/default) >= 1.0.2
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-registry) >= 0.61.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ipconfig"

%package     -n %{name}+computer
Summary:        Get network adapters information and network configuration for windows - feature "computer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-registry-0.6/default) >= 0.6.1
Requires:       crate(windows-result-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/computer) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+computer
This metapackage enables feature "computer" for the Rust ipconfig crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
