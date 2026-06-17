# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wezterm-input-types
%global full_version 0.1.0
%global pkgname wezterm-input-types-0.1

Name:           rust-wezterm-input-types-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "wezterm-input-types"
License:        MIT
URL:            https://github.com/wez/wezterm
#!RemoteAsset:  sha256:7012add459f951456ec9d6c7e6fc340b1ce15d6fc9629f8c42853412c029e57e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.3.0
Requires:       crate(euclid-0.22/default) >= 0.22.0
Requires:       crate(lazy-static-1/default) >= 1.4.0
Requires:       crate(wezterm-dynamic-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "wezterm-input-types"

%package     -n %{name}+serde
Summary:        Config serialization for wezterm via dynamic json-like data values - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/rc) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wezterm-input-types crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
