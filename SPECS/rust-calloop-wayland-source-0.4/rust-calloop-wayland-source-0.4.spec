# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name calloop-wayland-source
%global full_version 0.4.1
%global pkgname calloop-wayland-source-0.4

Name:           rust-calloop-wayland-source-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "calloop-wayland-source"
License:        MIT
URL:            https://github.com/smithay/calloop-wayland-source
#!RemoteAsset:  sha256:138efcf0940a02ebf0cc8d1eff41a1682a46b431630f4c52450d6265876021fa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(calloop-0.14/default) >= 0.14.0
Requires:       crate(rustix-1/std) >= 1.0.7
Requires:       crate(wayland-backend-0.3/default) >= 0.3.0
Requires:       crate(wayland-client-0.31/default) >= 0.31.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "calloop-wayland-source"

%package     -n %{name}+log
Summary:        Wayland-rs client event source for callloop - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.19
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust calloop-wayland-source crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
