# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mac_address
%global full_version 1.1.8
%global pkgname mac-address-1

Name:           rust-mac-address-1
Version:        1.1.8
Release:        %autorelease
Summary:        Rust crate "mac_address"
License:        MIT OR Apache-2.0
URL:            https://github.com/rep-nop/mac_address
#!RemoteAsset:  sha256:c0aeb26bf5e836cc1c341c8106051b573f1766dfa05aa87f0b98be5e51b02303
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(nix-0.29/default) >= 0.29.0
Requires:       crate(nix-0.29/net) >= 0.29.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/iphlpapi) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0
Requires:       crate(winapi-0.3/ws2def) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mac_address"

%package     -n %{name}+serde
Summary:        Cross-platform retrieval of a network interface MAC address - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.198
Requires:       crate(serde-1/derive) >= 1.0.198
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust mac_address crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
