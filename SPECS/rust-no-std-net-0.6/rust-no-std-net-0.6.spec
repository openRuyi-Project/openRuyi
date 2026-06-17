# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name no-std-net
%global full_version 0.6.0
%global pkgname no-std-net-0.6

Name:           rust-no-std-net-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "no-std-net"
License:        MIT
URL:            https://github.com/dunmatt/no-std-net
#!RemoteAsset:  sha256:43794a0ace135be66a25d3ae77d41b91615fb68ae937f904090203e81f755b65
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/i128) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-ip) = %{version}

%description
without the 'std'.
Source code for takopackized Rust crate "no-std-net"

%package     -n %{name}+serde
Summary:        Rust's std::net - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
without the 'std'.
This metapackage enables feature "serde" for the Rust no-std-net crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
